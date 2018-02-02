module Day15Test

open System
open Xunit
open FsUnit.Xunit
open Day15

let testGenA = 65L
let testGenB = 8921L

[<Fact>]
let ``numPairs works on test data`` () =
    numPairs testGenA testGenB
    |> should equal 588

[<Fact>]
let ``restrictedNumPairs works on test data`` () =
    restrictedNumPairs testGenA testGenB
    |> should equal 309