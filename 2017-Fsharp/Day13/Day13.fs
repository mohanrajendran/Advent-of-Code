module Day13

let parseLine (line: string) = 
    line.Split([|':'|])
    |> Array.map int
    |> (fun a -> (a.[0], a.[1]))

let caught (startingTime: int) (depth: int, range: int) =
    (startingTime + depth) % ((range-1) * 2) = 0

let score (depth: int, range: int) =
    depth * range

let severityScore (input: string array) =
    input
    |> Array.map parseLine
    |> Array.filter (caught 0)
    |> Array.sumBy score
    
let safeDelay (parsed: (int*int)[]) (delay: int) =
    Array.tryFind (caught delay) parsed = None

let delayTime (input: string array) =
    let parsed = input |> Array.map parseLine

    Seq.initInfinite id
    |> Seq.find (safeDelay parsed)

