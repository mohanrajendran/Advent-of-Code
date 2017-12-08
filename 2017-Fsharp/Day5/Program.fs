open Day5

module Program = 
    let [<EntryPoint>] main _ = 
        let input = 
            System.IO.File.ReadLines("input.txt")
            |> Seq.toArray

        printfn "Part 1:- %d\nPart 2:- %d"
                (escape1 input)
                (escape2 input)
        0
