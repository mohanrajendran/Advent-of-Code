open Day4

module Program = 
    let [<EntryPoint>] main _ = 
        let input = 
            System.IO.File.ReadLines("input.txt")

        printfn "Part 1:- %d\nPart 2:- %d"
                (countOfValidPassphrase1 input)
                (countOfValidPassphrase2 input)
        0
