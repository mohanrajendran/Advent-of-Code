module Day9Test

open System
open Xunit
open FsUnit.Xunit
open Day9

[<Theory>]
[<InlineData("{}", 1)>]
[<InlineData("{{{}}}", 6)>]
[<InlineData("{{},{}}", 5)>]
[<InlineData("{{{},{},{{}}}}", 16)>]
[<InlineData("{<a>,<a>,<a>,<a>}", 1)>]
[<InlineData("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9)>]
[<InlineData("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9)>]
[<InlineData("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3)>]
let ``groupSize works on testData`` (input: string, output: int) =
    input
    |> groupSize
    |> should equal output

[<Theory>]
[<InlineData("<>", 0)>]
[<InlineData("<random characters>", 17)>]
[<InlineData("<<<<>", 3)>]
[<InlineData("<{!>}>", 2)>]
[<InlineData("<!!>", 0)>]
[<InlineData("<!!!>>", 0)>]
[<InlineData("<{o\"i!a,<{i<a>", 10)>]
let ``garbageSize works on testData`` (input: string, output: int) =
    input
    |> garbageSize
    |> should equal output