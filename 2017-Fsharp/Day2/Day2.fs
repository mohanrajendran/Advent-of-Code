module Day2

let parse (lines: string): int[][] =
    lines.Split([|'\n'|])
    |> Array.map (fun line -> line.Split([|' '; '\t'|])
                              |> Array.map int)

let lineChecksum1 (parsedLine: int[]): int =
        Array.max(parsedLine) - Array.min(parsedLine)
let checksum1 (input: string): int =
    input
    |> parse
    |> Array.sumBy lineChecksum1

let evenlyDivisible (v1: int, v2: int): bool =
    v1 <> v2 && (v2 % v1 = 0 || (v1 % v2 = 0))

let allPairs (l1: int[], l2: int[]): seq<int * int> =
    seq {
        for v1 in l1 do
            for v2 in l2 do
                yield (v1, v2)
    }

let lineChecksum2 (parsedLine: int[]): int =
    allPairs(parsedLine, parsedLine)
    |> Seq.find (evenlyDivisible)
    |> (fun (v1, v2) -> if v1 > v2 then v1/v2 else v2/v1)

let checksum2 (input: string): int =
    input
    |> parse
    |> Array.sumBy lineChecksum2