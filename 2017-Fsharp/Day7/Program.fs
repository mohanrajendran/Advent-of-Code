open Day7

module Program = 
    let [<EntryPoint>] main _ = 
        let input = 
            System.IO.File.ReadAllLines("input.txt")
            |> Array.toSeq

        printfn "Part 1:- %s\nPart 2:- %d"
                (bottomProgram input)
                (balancedProgramWeight input)
        0
