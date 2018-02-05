open Day18

module Program = 
    let [<EntryPoint>] main _ = 
        let input = 
            System.IO.File.ReadAllLines("input.txt")

        printfn "Part 1:- %d\nPart 2:- %d"
                (firstRecoveredFrequency input)
                (numSendCalled input)
        0
        
