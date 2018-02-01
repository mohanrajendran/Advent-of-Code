open Day14

module Program = 
    let input = "stpzcrnm"
    let [<EntryPoint>] main _ = 
        printfn "Part 1:- %d\nPart 2:- %d"
                (numBitsSet input)
                (numRegions input)
        0
        
