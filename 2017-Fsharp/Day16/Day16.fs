module Day16
open System.Text.RegularExpressions

type Move = 
    | Spin of int
    | Exchange of (int*int)
    | Partner of (char*char)

let parseMove (move: string) =
    let spinMatch = Regex.Match(move.Trim(), @"^s(\d+)$")
    let exchangeMatch = Regex.Match(move.Trim(), @"^x(\d+)\/(\d+)$")
    let partnerMatch = Regex.Match(move.Trim(), @"^p(\w)\/(\w)$")

    if spinMatch.Success
    then Spin (spinMatch.Groups.[1].Value |> int)
    else if exchangeMatch.Success
    then Exchange (exchangeMatch.Groups.[1].Value |> int, exchangeMatch.Groups.[2].Value |> int)
    else if partnerMatch.Success
    then Partner (partnerMatch.Groups.[1].Value.[0], partnerMatch.Groups.[2].Value.[0])
    else failwithf "Unknown move %s" move

let applySpin (programs: char list) (X: int) =
    let progLen = programs.Length
    let (first, rest) = programs |> List.splitAt (progLen - X)
    List.append rest first

let applyPartner (programs: char list) (progA: char, progB: char) =
    programs
    |> List.map (fun prog -> if prog = progA then progB 
                             else if prog = progB then progA 
                             else prog)

let applyExchange (programs: char list) (A:int, B: int) =
    let progA = programs.Item A
    let progB = programs.Item B

    applyPartner (programs) (progA, progB)

let applyMove (program: char list) (move: Move) =
    match move with 
    | Spin X -> applySpin program X
    | Exchange v -> applyExchange program v
    | Partner v -> applyPartner program v

let concatProgram (program: char list) =
    program
    |> Seq.map string
    |> String.concat ""

let afterDance (program: char list) (moves: string) =
    moves.Split([|','|])
    |> Seq.ofArray
    |> Seq.map parseMove
    |> Seq.fold applyMove program
    |> concatProgram

let rec cycleLength (program: char list) (seenSoFar: Set<string>) (moves: Move seq) =
    let newProgram = 
        moves 
        |> Seq.fold applyMove program 
    let concat = newProgram |> concatProgram
    if seenSoFar |> Set.contains concat
    then seenSoFar.Count
    else cycleLength newProgram (seenSoFar |> Set.add concat) moves

let rec repeatSequence (n: int) (s: seq<'a>) =
    match n with
    | 1 -> seq{ yield! s }
    | _ -> seq{ yield! s; yield! repeatSequence (n-1) s}

let afterLongDance (program: char list) (moves: string) =
    let parsedMoves = moves.Split([|','|]) |> Seq.ofArray |> Seq.map parseMove
    let cycleLen = 
        parsedMoves
        |> cycleLength program Set.empty
    
    parsedMoves
    |> repeatSequence (1000000000 % cycleLen)
    |> Seq.fold applyMove program
    |> concatProgram
