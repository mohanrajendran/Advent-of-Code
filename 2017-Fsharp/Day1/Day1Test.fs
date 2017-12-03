module Day1Test

open System
open Xunit
open FsUnit.Xunit
open Day1

[<Fact>]
let ``1234 gets parsed``() =
    parse "1234"
    |> should equal [1;2;3;4]

[<Theory>]
[<InlineData("1122", 3)>]
[<InlineData("1111", 4)>]
[<InlineData("1234", 0)>]
[<InlineData("91212129", 9)>]
let ``captcha1 works correctly for test data`` (input: string, output: int) =
    captcha1 input
    |> should equal output

[<Theory>]
[<InlineData("1212", 6)>]
[<InlineData("1221", 0)>]
[<InlineData("123425", 4)>]
[<InlineData("123123", 12)>]
[<InlineData("12131415", 4)>]
let ``captcha2 works correctly for test data`` (input: string, output: int) =
    captcha2 input
    |> should equal output