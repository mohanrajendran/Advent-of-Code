module Day11Test

open System
open Xunit
open FsUnit.Xunit
open Day11

[<Theory>]
[<InlineData("ne,ne,ne", 3)>]
[<InlineData("ne,ne,sw,sw", 0)>]
[<InlineData("ne,ne,s,s", 2)>]
[<InlineData("se,sw,se,sw,sw", 3)>]
let ``hexDistance works on test data`` (input: string, output: int) =
    hexDistance input
    |> should equal output