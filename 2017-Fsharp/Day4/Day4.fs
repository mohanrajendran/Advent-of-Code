module Day4

let allDistinctByKey (items: string[]) (key: string -> 'a) = 
    let dedup = Array.distinctBy key items
    Array.length dedup = Array.length items

let validPassphrase1 (line: string) =
    allDistinctByKey (line.Split([|' '; '\t'|])) id

let countOfValidPassphrase1 (lines: string seq) =
    lines
    |> Seq.filter validPassphrase1
    |> Seq.length

let anagramKey (line: string) =
    line
    |> Seq.sort
    |> Seq.toArray

let validPassphrase2 (line: string) =
    allDistinctByKey (line.Split([|' '; '\t'|])) anagramKey

let countOfValidPassphrase2 (lines: string seq) =
    lines
    |> Seq.filter validPassphrase2
    |> Seq.length