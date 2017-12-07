module Day4Test

open System
open Xunit
open FsUnit.Xunit
open Day4

[<Theory>]
[<InlineData("aa bb cc dd ee", true)>]
[<InlineData("aa bb cc dd aa", false)>]
[<InlineData("aa bb cc dd aaa", true)>]
let ``validPassphrase1 is checked correctly`` (input: string, output: bool) =
    validPassphrase1 input
    |> should equal output

[<Theory>]
[<InlineData("abcde fghij", true)>]
[<InlineData("abcde xyz ecdab", false)>]
[<InlineData("a ab abc abd abf abj", true)>]
[<InlineData("iiii oiii ooii oooi oooo", true)>]
[<InlineData("oiii ioii iioi iiio", false)>]
let ``validPassphrase2 is checked correctly`` (input: string, output: bool) =
    validPassphrase2 input
    |> should equal output