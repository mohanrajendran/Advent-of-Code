module Day6Test

open System
open Xunit
open FsUnit.Xunit
open Day6

[<Fact>]
let ``loopSize1 works on test data`` () =
    loopSize1 "0 2 7 0"
    |> should equal 5

[<Fact>]
let ``loopSize2 works on test data`` () =
    loopSize2 "0 2 7 0"
    |> should equal 4
