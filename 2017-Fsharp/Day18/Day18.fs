module Day18
open System.Text.RegularExpressions
open System.Collections.Generic
open Xunit.Abstractions

type Value = Direct of int64 | Indirect of char

type Instruction = 
    | Snd of (Value)
    | Set of (Value * Value)
    | Add of (Value * Value)
    | Mul of (Value * Value)
    | Mod of (Value * Value)
    | Rcv of (Value)
    | Jgz of (Value * Value)

type ProgramStatus = {registers: Map<char, int64>; pc: int64; lastPlayedFreq: int64}

let convertToValue (v: string) =
    match System.Int64.TryParse(v) with
    | (true, i) -> Direct (i)
    | _         -> Indirect (v.[0])

let (|InstrMatcher|_|) (pattern: string) (instruction: string) =
    let m = Regex.Match(instruction.Trim(), pattern)
    if m.Success
    then 
        [1..m.Groups.Count-1]
        |> List.map (fun i -> m.Groups.[i].Value |> convertToValue)
        |> Some
    else None

let parseInstruction (instruction: string) = 
    match instruction with
    | InstrMatcher @"^snd ([a-z0-9\-]+)$" v              -> Snd v.[0]
    | InstrMatcher @"^set ([a-z0-9\-]) ([a-z0-9\-]+)$" v -> Set (v.[0], v.[1])
    | InstrMatcher @"^add ([a-z0-9\-]) ([a-z0-9\-]+)$" v -> Add (v.[0], v.[1])
    | InstrMatcher @"^mul ([a-z0-9\-]) ([a-z0-9\-]+)$" v -> Mul (v.[0], v.[1])
    | InstrMatcher @"^mod ([a-z0-9\-]) ([a-z0-9\-]+)$" v -> Mod (v.[0], v.[1])
    | InstrMatcher @"^rcv ([a-z0-9\-]+)$" v              -> Rcv v.[0]
    | InstrMatcher @"^jgz ([a-z0-9\-]) ([a-z0-9\-]+)$" v -> Jgz (v.[0], v.[1])
    | _ -> failwithf "Unknown instruction %s" instruction

let getValue (status: ProgramStatus) (value: Value) =
    match value with
    | Direct   v -> v
    | Indirect v ->
        match status.registers.TryFind v with
        | Some i -> i
        | None   -> 0L

let setValue (address: Value) (value: int64) (status: ProgramStatus) =
    match address with
    | Indirect a -> {status with registers = status.registers |> Map.add a value}
    | _          -> failwith "Assigning to direct address"

let incrementPc (status: ProgramStatus) =
    {status with pc = status.pc + 1L}

let applyProgram (status: ProgramStatus) (instructions: Instruction[]) =
    let rec applyHelper status =
        let instr = instructions.[status.pc |> int]
        match instr with
        | Snd X      ->
            {status with lastPlayedFreq = X |> getValue status} |> incrementPc |> applyHelper
        | Set (X, Y) ->
            let newValue = Y |> getValue status
            status |> setValue X newValue |> incrementPc |> applyHelper
        | Add (X, Y) ->
            let newValue = (X |> getValue status) + (Y |> getValue status) 
            status |> setValue X newValue|> incrementPc |> applyHelper
        | Mul (X, Y) ->
            let newValue = (X |> getValue status) * (Y |> getValue status) 
            status |> setValue X newValue|> incrementPc |> applyHelper
        | Mod (X, Y) ->
            let newValue = (X |> getValue status) % (Y |> getValue status) 
            status |> setValue X newValue|> incrementPc |> applyHelper
        | Rcv X      ->
            let flag = X |> getValue status
            if flag = 0L
            then status |> incrementPc |> applyHelper
            else status.lastPlayedFreq
        | Jgz (X, Y) -> 
            let flag = X |> getValue status
            let offset = if flag > 0L then (Y |> getValue status) else 1L
            {status with pc = status.pc + offset} |> applyHelper
    applyHelper status

let firstRecoveredFrequency (input: string[]) =
    input
    |> Array.map parseInstruction
    |> applyProgram {registers = Map.empty; pc = 0L; lastPlayedFreq = 0L}

let applyConcurrently (status: ProgramStatus) 
                      (instructions: Instruction[]) 
                      (sourceQueue: Queue<int64>) 
                      (sinkQueue: Queue<int64>) =
    let rec applyHelper sentSoFar status =
        let instr = instructions.[status.pc |> int]
        match instr with
        | Snd X      ->
            sinkQueue.Enqueue (X |> getValue status)
            status |> incrementPc |> applyHelper (sentSoFar + 1L)
        | Set (X, Y) ->
            let newValue = Y |> getValue status
            status |> setValue X newValue |> incrementPc |> applyHelper sentSoFar
        | Add (X, Y) ->
            let newValue = (X |> getValue status) + (Y |> getValue status) 
            status |> setValue X newValue|> incrementPc |> applyHelper sentSoFar
        | Mul (X, Y) ->
            let newValue = (X |> getValue status) * (Y |> getValue status) 
            status |> setValue X newValue|> incrementPc |> applyHelper sentSoFar
        | Mod (X, Y) ->
            let newValue = (X |> getValue status) % (Y |> getValue status) 
            status |> setValue X newValue|> incrementPc |> applyHelper sentSoFar
        | Rcv X      ->
            if sourceQueue.Count = 0
            then (sentSoFar, status)
            else 
                let value = sourceQueue.Dequeue()
                status |> setValue X value |> incrementPc |> applyHelper sentSoFar
        | Jgz (X, Y) -> 
            let flag = X |> getValue status
            let offset = if flag > 0L then (Y |> getValue status) else 1L
            {status with pc = status.pc + offset} |> applyHelper sentSoFar
    applyHelper 0L status

let rec runConcurrently (p0Status: ProgramStatus)
                        (p1Status: ProgramStatus)
                        (p0Queue: Queue<int64>)
                        (p1Queue: Queue<int64>)
                        (p1Sent: int64)
                        (instructions: Instruction[]) =
    if p0Queue.Count = 0 && p1Queue.Count = 0
    then p1Sent
    else if p0Queue.Count <> 0
    then
        let (_ ,newP0Status) = applyConcurrently p0Status instructions p0Queue p1Queue
        runConcurrently newP0Status p1Status p0Queue p1Queue p1Sent instructions
    else
       let (newP1Sent, newP1Status) = applyConcurrently p1Status instructions p1Queue p0Queue
       runConcurrently p0Status newP1Status p0Queue p1Queue (p1Sent + newP1Sent) instructions 

let numSendCalled (input: string[]) =
    let instructions = input |> Array.map parseInstruction
    let p0Queue = new Queue<int64>()
    let p1Queue = new Queue<int64>()

    let p0Status = {registers = Map.empty |> Map.add 'p' 0L; pc = 0L; lastPlayedFreq = 0L}
    let p1Status = {registers = Map.empty |> Map.add 'p' 1L; pc = 0L; lastPlayedFreq = 0L}

    let (_, p0Status) = applyConcurrently p0Status instructions p0Queue p1Queue
    let (p1Sent, p1Status) = applyConcurrently p1Status instructions p1Queue p0Queue

    runConcurrently p0Status p1Status p0Queue p1Queue p1Sent instructions