open Day9

module Program = 
    let [<EntryPoint>] main _ = 
        let input = 
            System.IO.File.ReadAllText("input.txt")

        printfn "Part 1:- %d\nPart 2:- %d"
                (groupSize input)
                (garbageSize input)
        0
        
