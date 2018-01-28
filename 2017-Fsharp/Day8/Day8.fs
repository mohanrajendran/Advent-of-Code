module Day8
open System.Text.RegularExpressions

type parsedExpression = {reg1: string; op: string; delta: int; reg2: string; comp: string; value: int}

let parse (line: string) = 
    let pattern = @"^(?<reg1>\w+) (?<op>inc|dec) (?<delta>-?\d+) if (?<reg2>\w+) (?<comp><=|<|==|>|>=|!=) (?<value>-?\d+)"
    let re = Regex.Match(line, pattern, RegexOptions.None)
    let reg1 = re.Groups.["reg1"].Value
    let op =  re.Groups.["op"].Value
    let delta = re.Groups.["delta"].Value |> int
    let reg2 = re.Groups.["reg2"].Value
    let comp = re.Groups.["comp"].Value
    let value = re.Groups.["value"].Value |> int
    {reg1 = reg1; op = op; delta = delta; reg2 = reg2; comp = comp; value = value}

let getRegisterValue (registers: Map<string, int>) (reg: string) =
    match registers |> Map.tryFind reg with
    | Some(v) -> (v, registers)
    | None    -> (0, registers |> Map.add reg 0)

let processCommand (registers: Map<string, int>) (command: parsedExpression) =
    let (reg1Val, registers1) = command.reg1 |> getRegisterValue registers
    let (reg2Val, registers2) = command.reg2 |> getRegisterValue registers1

    let condSuccess = 
        match command.comp with
        | "<"  -> reg2Val < command.value
        | "<=" -> reg2Val <= command.value
        | "==" -> reg2Val = command.value
        | ">=" -> reg2Val >= command.value
        | ">"  -> reg2Val > command.value
        | "!=" -> reg2Val <> command.value
        | comp -> failwithf "unknowm op %s" comp
    if condSuccess
    then
        let reg1New =
            match command.op.ToLower() with
            | "inc" -> reg1Val + command.delta
            | "dec" -> reg1Val - command.delta
            | comp  -> failwithf "unknown comp %s" comp
        registers2 |> Map.add command.reg1 reg1New
    else registers2

let registerMax (registers: Map<string, int>) =
    registers
    |> Map.toSeq
    |> Seq.map snd
    |> Seq.max

let maxRegisterValue (input: string seq) =
    input
    |> Seq.map parse
    |> Seq.fold processCommand Map.empty
    |> registerMax

let maxEverRegisterValue (input: string seq) =
    input
    |> Seq.map parse
    |> Seq.scan processCommand Map.empty
    |> Seq.skip 1
    |> Seq.map registerMax
    |> Seq.max