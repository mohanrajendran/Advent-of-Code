open Day8

module Program = 
    let [<EntryPoint>] main _ = 
        let input = 
            System.IO.File.ReadAllLines("input.txt")

        printfn "Part 1:- %d\nPart 2:- %d"
                (maxRegisterValue input)
                (maxEverRegisterValue input)
        0
