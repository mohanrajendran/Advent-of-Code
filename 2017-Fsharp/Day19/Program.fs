open Day19

module Program = 
    let [<EntryPoint>] main _ = 
        let input = 
            System.IO.File.ReadAllLines("input.txt")

        printfn "Part 1:- %s\nPart 2:- %d"
                (traversedLetters input)
                (traversedDistance input)
        0
        
