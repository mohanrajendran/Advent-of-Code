open Day3

module Program = 
    let [<EntryPoint>] main _ = 
        let input = 312051
        printfn "Part 1:- %d\nPart 2:- %d"
                (ulam1 input)
                (ulam2 input)
        0
