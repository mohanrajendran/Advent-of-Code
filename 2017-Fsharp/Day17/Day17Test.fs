module Day17Test

open System
open Xunit
open FsUnit.Xunit
open Day17

[<Fact>]
let ``itemAfter2017 works on test input`` () =
    itemAfter2017 3
    |> should equal 638