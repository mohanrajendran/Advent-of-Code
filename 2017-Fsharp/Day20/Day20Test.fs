module Day20Test

open System
open Xunit
open FsUnit.Xunit
open Day20

let testInput1 = "p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>"

[<Fact>]
let ``closestParticle works on test data`` () =
    testInput1.Split([|'\n'|])
    |> closestParticle
    |> should equal 0
    
let testInput2 = "p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>
p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>
p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>
p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>"

[<Fact>]
let ``uncollidedParticles works on test data`` () =
    testInput2.Split([|'\n'|])
    |> uncollidedParticles
    |> should equal 1