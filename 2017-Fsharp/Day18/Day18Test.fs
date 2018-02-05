module Day18Test

open System
open Xunit
open FsUnit.Xunit
open Day18

let testInput1 = "set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"

[<Fact>]
let ``firstRecoveredFrequency works on test data`` () =
    testInput1.Split([|'\n'|])
    |> firstRecoveredFrequency
    |> should equal 4L

let testInput2 = "snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"

[<Fact>]
let ``numSendCalled works on test data`` () =
    testInput2.Split([|'\n'|])
    |> numSendCalled
    |> should equal 3L
