module Day16Test

open System
open Xunit
open FsUnit.Xunit
open Day16

let testInput = "s1,x3/4,pe/b"

[<Fact>]
let ``afterDance works on test data`` () =
    testInput
    |> afterDance ['a'..'e']
    |> should equal "baedc"