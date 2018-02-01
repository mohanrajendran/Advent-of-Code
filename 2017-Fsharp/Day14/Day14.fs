module Day14

type Chain = { numbers: int array; index: int; skipSize: int }

let processKnot (chain: Chain) (knotWidth: int) =
    {0 .. knotWidth/2-1}
    |> Seq.iter (fun i -> let i1 = (chain.index + i) % chain.numbers.Length
                          let i2 = (chain.index + knotWidth - 1 - i) % chain.numbers.Length
                          let temp = chain.numbers.[i1]
                          chain.numbers.[i1] <- chain.numbers.[i2]
                          chain.numbers.[i2] <- temp)

    {chain with index = (chain.index + knotWidth + chain.skipSize) % chain.numbers.Length;
                skipSize = chain.skipSize + 1}

let parseToChars (key: string) =
    key
    |> List.ofSeq
    |> List.map int

let rec repeatSequence (n: int) (s: seq<'a>) =
    match n with
    | 1 -> seq{ yield! s }
    | _ -> seq{ yield! s; yield! repeatSequence (n-1) s}

let countOnes (num: int) = 
    let rec countOnesHelper (num: int) (count: int) = 
        if num = 0
        then count
        else countOnesHelper (num &&& (num-1)) (count + 1)
    countOnesHelper num 0

let compressAndCount (chain: Chain) =
    chain.numbers
    |> Array.chunkBySize 16
    |> Array.sumBy (Array.reduce (^^^) >> countOnes)

let knotHash (key: string) =
    let initialChain = { numbers = {0 .. 255} |> Seq.toArray; index = 0; skipSize = 0}

    Seq.concat [key |> parseToChars; [17; 31; 73; 47; 23]]
    |> repeatSequence 64
    |> Seq.fold processKnot initialChain

let numBitsSet (key: string) = 
    {0 .. 127}
    |> Seq.sumBy (fun n -> (sprintf "%s-%d" key n) |> knotHash |> compressAndCount)

let hexToBin (hex: char) = 
    match hex with
    | '0' -> [0;0;0;0]
    | '1' -> [0;0;0;1]
    | '2' -> [0;0;1;0]
    | '3' -> [0;0;1;1]
    | '4' -> [0;1;0;0]
    | '5' -> [0;1;0;1]
    | '6' -> [0;1;1;0]
    | '7' -> [0;1;1;1]
    | '8' -> [1;0;0;0]
    | '9' -> [1;0;0;1]
    | 'A' -> [1;0;1;0]
    | 'B' -> [1;0;1;1]
    | 'C' -> [1;1;0;0]
    | 'D' -> [1;1;0;1]
    | 'E' -> [1;1;1;0]
    | 'F' -> [1;1;1;1]
    | _   -> failwithf "Unknown hex digit %c" hex

let toGridRow (chain: Chain) =
    chain.numbers
    |> Array.chunkBySize 16
    |> Array.map (Array.reduce (^^^) >> (fun n -> n.ToString("X2")))
    |> String.concat ""
    |> Seq.collect hexToBin
    |> Array.ofSeq

let rec traverse (grid: int[][]) (x:int ,y:int) =
    if x < 0 || x > 127 || y < 0 || y > 127 || grid.[x].[y] <> 1
    then ()
    else
        grid.[x].[y] <- 2
        [(0,-1); (0, 1); (1,0); (-1, 0)]
        |> Seq.iter (fun (dx, dy) -> traverse grid (x+dx, y+dy))

let numRegions (key: string) =
    let grid = 
        {0 .. 127}
        |> Seq.map (fun n -> (sprintf "%s-%d" key n) |> knotHash |> toGridRow)
        |> Seq.toArray
    seq {
        for x in {0 .. 127} do
            for y in {0 .. 127} do
                yield (x, y)
    }
    |> Seq.map (fun (x,y) ->
        if grid.[x].[y] = 1
        then
            traverse grid (x,y)
            Some 1
        else None)
    |> Seq.choose id
    |> Seq.sum