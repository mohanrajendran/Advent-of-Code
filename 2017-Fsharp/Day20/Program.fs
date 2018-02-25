open Day20

module Program = 
    let [<EntryPoint>] main _ = 
        let input = 
            System.IO.File.ReadAllLines("input.txt")

        printfn "Part 1:- %d"
                (closestParticle input)
        0
        
