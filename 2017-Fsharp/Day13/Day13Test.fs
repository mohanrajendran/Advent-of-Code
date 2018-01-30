module Day13Test

open System
open Xunit
open FsUnit.Xunit
open Day13

let testInput = "0: 3
1: 2
4: 4
6: 4"

[<Fact>]
let ``severityScore works on test data`` () =
    testInput.Split([|'\n'|])
    |> severityScore
    |> should equal 24

[<Fact>]
let ``safeDelay works on test data`` () =
    testInput.Split([|'\n'|])
    |> delayTime
    |> should equal 10