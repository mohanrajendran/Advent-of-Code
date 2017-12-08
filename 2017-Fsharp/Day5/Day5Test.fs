module Day5Test

open System
open Xunit
open FsUnit.Xunit
open Day5

[<Fact>]
let ``escape1 works on test data`` () = 
    escape1 [|"0"; "3"; "0"; "1"; "-3"|]
    |> should equal 5

[<Fact>]
let ``escape2 works on test data`` () = 
    escape2 [|"0"; "3"; "0"; "1"; "-3"|]
    |> should equal 10