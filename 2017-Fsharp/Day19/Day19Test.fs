module Day19Test

open System
open Xunit
open FsUnit.Xunit
open Day19

let testInput = "     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ "

[<Fact>]
let ``traversedLetters works on test data`` () =
    testInput.Split([|'\n'|])
    |> traversedLetters
    |> should equal "ABCDEF"

[<Fact>]
let ``traversedDistance works on test data`` () =
    testInput.Split([|'\n'|])
    |> traversedDistance
    |> should equal 38
