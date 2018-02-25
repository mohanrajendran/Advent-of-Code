module Day20
open System
open System.Text.RegularExpressions

type Vec3 = {x: int; y: int; z: int}
type Particle = {P: Vec3; V: Vec3; A: Vec3}

let manhattanDistance (pos: Vec3) =
    Math.Abs(pos.x) + Math.Abs(pos.y) + Math.Abs(pos.z)

let parseLine (line: string) = 
    let pattern = @"^p=<(\-?\d+),(\-?\d+),(\-?\d+)>, v=<(\-?\d+),(\-?\d+),(\-?\d+)>, a=<(\-?\d+),(\-?\d+),(\-?\d+)>$"
    let m = Regex.Match(line.Trim(), pattern)
    let nums = 
        [|1..m.Groups.Count-1|]
        |> Array.map (fun i -> m.Groups.[i].Value |> int)
    {P = {x = nums.[0]; y = nums.[1]; z = nums.[2]};
     V = {x = nums.[3]; y = nums.[4]; z = nums.[5]};
     A = {x = nums.[6]; y = nums.[7]; z = nums.[8]}}

let closestParticle (input: string[]) =
    input
    |> Array.map parseLine
    |> Array.mapi (fun i p -> (i, p.A |> manhattanDistance))
    |> Array.minBy snd
    |> fst