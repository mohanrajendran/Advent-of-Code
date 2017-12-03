module Day2Test

open System
open Xunit
open FsUnit.Xunit
open Day2

[<Fact>]
let ``Checksum1 calculated on test case`` () =
    let testInput = @"5 1 9 5
7 5 3
2 4 6 8"
    checksum1 testInput
    |> should equal 18

[<Fact>]
let ``Checksum2 calculated on test case`` () =
    let testInput = @"5 9 2 8
9 4 7 3
3 8 6 5"
    checksum2 testInput
    |> should equal 9