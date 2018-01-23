module Day7Test

open System
open Xunit
open FsUnit.Xunit
open Day7

let testInput = "pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"

[<Fact>]
let ``bottomProgram works on test data`` () =
    testInput.Split([|'\n'|])
    |> bottomProgram
    |> should equal "tknk"

[<Fact>]
let ``balancedProgramWeight works on test data`` () =
    testInput.Split([|'\n'|])
    |> balancedProgramWeight
    |> should equal 60