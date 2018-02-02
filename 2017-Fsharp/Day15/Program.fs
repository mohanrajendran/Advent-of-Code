open Day15

module Program = 
    let genAstart = 722L
    let genBstart = 354L
    let [<EntryPoint>] main _ = 
        printfn "Part 1:- %d\nPart 2:- %d"
                (numPairs genAstart genBstart)
                (restrictedNumPairs genAstart genBstart)
        0
        
