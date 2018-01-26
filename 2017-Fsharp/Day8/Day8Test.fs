module Day8Test

open System
open Xunit
open FsUnit.Xunit
open Day8

let testInput = "b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"

[<Fact>]
let ``maxRegisterValue works on test data`` () =
    testInput.Split([|'\n'|])
    |> maxRegisterValue
    |> should equal 1

[<Fact>]
let ``maxEverRegisterValue works on test data`` () =
    testInput.Split([|'\n'|])
    |> maxEverRegisterValue
    |> should equal 10