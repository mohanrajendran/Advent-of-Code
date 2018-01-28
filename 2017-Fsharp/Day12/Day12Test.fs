module Day12Test

open System
open Xunit
open FsUnit.Xunit
open Day12

let testInput = "0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"

[<Fact>]
let ``numConnected works on test data`` () =
    testInput.Split([|'\n'|])
    |> numConnected 0
    |> should equal 6

[<Fact>]
let ``numGroups works on test data`` () =
    testInput.Split([|'\n'|])
    |> numGroups
    |> should equal 2
