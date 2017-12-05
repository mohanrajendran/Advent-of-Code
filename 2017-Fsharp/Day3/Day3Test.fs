module Day3Test

open System
open Xunit
open FsUnit.Xunit
open Day3

[<Theory>]
[<InlineData(1, 0)>]
[<InlineData(12, 3)>]
[<InlineData(23, 2)>]
[<InlineData(1024, 31)>]
let ``ulam1 works correctly for test data`` (input: int, output: int) =
    ulam1 input
    |> should equal output

[<Theory>]
[<InlineData(1, 2)>]
[<InlineData(3, 4)>]
[<InlineData(50, 54)>]
[<InlineData(300, 304)>]
let ``ulam2 works correctly for test data`` (input: int, output: int) =
    ulam2 input
    |> should equal output
