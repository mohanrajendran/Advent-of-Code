open Day13

module Program = 
    let [<EntryPoint>] main _ = 
        let input = 
            System.IO.File.ReadAllLines("input.txt")

        printfn "Part 1:- %d\nPart2:- %d"
                (severityScore input)
                (delayTime input)
        0
        
