module Day10Test

open System
open Xunit
open FsUnit.Xunit
open Day10

let testInput = "3,4,1,5"

[<Fact>]
let ``shiftMult works on test data`` () =
    testInput
    |> shiftMult 5
    |> should equal 12

[<Theory>]
[<InlineData("", "a2582a3a0e66e6e86e3812dcb672a272")>]
[<InlineData("AoC 2017", "33efeb34ea91902bb2f59c9920caa6cd")>]
[<InlineData("1,2,3", "3efbe78a8d82f29979031a4aa0b16a9d")>]
[<InlineData("1,2,4", "63960835bcdc130f0b66d7ff4f6a5a8e")>]
let ``knotHash works on test data`` (key: string, hash: string) =
    knotHash key
    |> should equal hash
