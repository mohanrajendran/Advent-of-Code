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
let ``steps works correctly for test data`` (input: int, output: int) =
    ulam input
    |> should equal output