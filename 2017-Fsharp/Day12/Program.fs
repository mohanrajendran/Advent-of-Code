open Day12

module Program = 
    let [<EntryPoint>] main _ = 
        let input = 
            System.IO.File.ReadAllLines("input.txt")

        printfn "Part 1:- %d\nPart 2:- %d"
                (numConnected 0 input)
                (numGroups input)
        0
        
