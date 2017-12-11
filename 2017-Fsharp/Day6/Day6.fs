module Day6

let parse (input: string) =
    input.Split([|' '; '\t'|])
    |> Array.map int
    |> Array.toList
    |> List.indexed

let redistribute (numberedBlocks: (int * int) list) =
    let blockLen = numberedBlocks.Length
    let maximumBlock =
        numberedBlocks
        |> List.maxBy snd
    let increaseForAll = (snd maximumBlock) / blockLen
    let extraBlocks = (snd maximumBlock) % blockLen
    //printfn "%A %d %d" (numberedBlocks |> List.map snd) increaseForAll extraBlocks
    numberedBlocks
    |> List.map 
        (fun (idx, mem) -> 
                if idx = (fst maximumBlock)
                then (idx, increaseForAll)
                else if (idx + blockLen - (fst maximumBlock) - 1) % blockLen < extraBlocks
                then (idx, mem + increaseForAll + 1)
                else (idx, mem + increaseForAll))

let rec redistributeUntilRepeat1 (seenSoFar: Set<List<int>>) (currentBlock: (int * int) list) =
    let nextBlock = redistribute currentBlock
    let nextBlockList = nextBlock |> List.map snd
    if seenSoFar.Contains nextBlockList
    then seenSoFar.Count + 1
    else (redistributeUntilRepeat1 (seenSoFar.Add nextBlockList) nextBlock)
    
let loopSize1 (input: string) = 
    input
    |> parse
    |> redistributeUntilRepeat1 Set.empty

let rec redistributeUntilRepeat2 (seenSoFar: Map<List<int>, int>) (currentBlock: (int * int) list) =
    let nextBlock = redistribute currentBlock
    let nextBlockList = nextBlock |> List.map snd
    if seenSoFar.ContainsKey nextBlockList
    then seenSoFar.Count + 1 - (seenSoFar |> Map.find nextBlockList)
    else (redistributeUntilRepeat2 (seenSoFar |> Map.add nextBlockList (seenSoFar.Count + 1)) nextBlock)

let loopSize2 (input: string) = 
    input
    |> parse
    |> redistributeUntilRepeat2 Map.empty