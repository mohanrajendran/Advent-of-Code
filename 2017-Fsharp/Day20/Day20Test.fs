module Day20Test

open System
open Xunit
open FsUnit.Xunit
open Day20

let testInput = "p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>"

[<Fact>]
let ``closestParticle works on test data`` () =
    testInput.Split([|'\n'|])
    |> closestParticle
    |> should equal 0
    