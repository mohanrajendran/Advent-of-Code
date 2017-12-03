module Day1 

    let parse (input: string): int list =
        input
        |> Seq.map (string >> int)
        |> Seq.toList

    let captcha1 (input: string): int =
        let parsed = parse input
        let values = List.append parsed [List.head(parsed)]
        values
        |> Seq.pairwise
        |> Seq.sumBy (fun (a,b) -> if a = b then a else 0)
        
    let captcha2 (input: string): int =
        let parsed = parse input
        let halfLen = (List.length parsed) / 2
        let offset = List.append (List.skip halfLen parsed) (List.take halfLen parsed)

        List.zip parsed offset
        |> Seq.sumBy (fun (a,b) -> if a = b then a else 0)