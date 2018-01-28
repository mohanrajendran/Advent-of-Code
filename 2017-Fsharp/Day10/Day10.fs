module Day10

let parseToInts (shifts: string) =
    shifts.Split([|','|])
    |> Seq.map int

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

let shiftMult (circleLength: int) (shifts: string) =
    let initialChain = { numbers = {0 .. circleLength-1} |> Seq.toArray; index = 0; skipSize = 0}

    shifts 
    |> parseToInts
    |> Seq.fold processKnot initialChain
    |> (fun c -> c.numbers.[0] * c.numbers.[1])

let parseToChars (key: string) =
    key
    |> List.ofSeq
    |> List.map int

let rec repeatSequence (n: int) (s: seq<'a>) =
    match n with
    | 1 -> seq{ yield! s }
    | _ -> seq{ yield! s; yield! repeatSequence (n-1) s}

let compressKnot (chain: Chain) =
    chain.numbers
    |> Array.chunkBySize 16
    |> Array.map (Array.reduce (^^^) >> (fun n -> n.ToString("x2")))
    |> String.concat ""

let knotHash (key: string) =
    let initialChain = { numbers = {0 .. 255} |> Seq.toArray; index = 0; skipSize = 0}

    Seq.concat [key |> parseToChars; [17; 31; 73; 47; 23]]
    |> repeatSequence 64
    |> Seq.fold processKnot initialChain
    |> compressKnot