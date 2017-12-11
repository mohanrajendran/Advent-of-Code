open Day6

module Program = 
    let [<EntryPoint>] main _ = 
        let input = "4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5"
        printfn "Part 1:- %d\nPart 2:- %d"
                (loopSize1 input)
                (loopSize2 input)
        0
