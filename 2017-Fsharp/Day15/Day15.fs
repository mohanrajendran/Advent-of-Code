module Day15
open Xunit.Sdk

let makeGenerator (start: int64) (factor: int64)=
    let mutable value = start
    seq {
        while true do
            value <- ((value * factor) % 2147483647L)
            yield value
    }

let numPairs (genAStart: int64) (genBStart: int64) =
    let genA = makeGenerator genAStart 16807L 
    let genB = makeGenerator genBStart 48271L 

    Seq.zip genA genB
    |> Seq.take 40000000
    |> Seq.filter (fun (a,b) -> (a &&& 65535L) = (b &&& 65535L))
    |> Seq.length

let restrictedNumPairs (genAStart: int64) (genBStart: int64) =
    let genA = makeGenerator genAStart 16807L 
               |> Seq.filter (fun a -> a &&& 3L = 0L)
    let genB = makeGenerator genBStart 48271L 
               |> Seq.filter (fun b -> b &&& 7L = 0L)

    Seq.zip genA genB
    |> Seq.take 5000000
    |> Seq.filter (fun (a,b) -> (a &&& 65535L) = (b &&& 65535L))
    |> Seq.length