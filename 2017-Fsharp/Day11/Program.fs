open Day11
open System

module Program = 
    let [<EntryPoint>] main _ = 
        let input = 
            System.IO.File.ReadAllText("input.txt")
        printfn "Part 1:- %d\nPart 2:- %d" 
                (hexDistance input)
                (maxHexDistance input)

        0