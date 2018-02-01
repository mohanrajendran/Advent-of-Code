module Day14Test

open System
open Xunit
open FsUnit.Xunit
open Day14

let testInput = "flqrgnkx"

[<Fact>]
let ``numBitsSet works on test data`` () =
    testInput
    |> numBitsSet
    |> should equal 8108

[<Fact>]
let ``numRegions works on test data`` () =
    testInput
    |> numRegions
    |> should equal 1242