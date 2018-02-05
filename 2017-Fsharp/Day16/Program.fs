open Day16

module Program = 
    let [<EntryPoint>] main _ = 
        let input = 
            System.IO.File.ReadLines("input.txt") |> Seq.head

        printfn "Part 1:- %s\nPart 2:- %s"
                (afterDance ['a'..'p'] input)
                (afterLongDance ['a'..'p'] input)
        0
        
