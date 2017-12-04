open Day3

module Program = 
    let [<EntryPoint>] main _ = 
        let input = 312051
        printfn "Part 1:- %d"
                (ulam input)
        0
