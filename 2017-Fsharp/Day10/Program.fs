open Day10

module Program = 
    let input = "212,254,178,237,2,0,1,54,167,92,117,125,255,61,159,164"
    let [<EntryPoint>] main _ = 
        printfn "Part 1:- %d\nPart 2:- %s" 
                (shiftMult 256 input)
                (knotHash input)
        0
        
