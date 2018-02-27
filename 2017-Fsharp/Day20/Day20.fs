module Day20
open System
open System.Text.RegularExpressions

type Vec3 = 
    {x: int; y: int; z: int}

    static member (+) (v1: Vec3, v2: Vec3) =
        {x = v1.x + v2.x; y = v1.y + v2.y; z = v1.z + v2.z} 
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

let removeCollided (particles: Particle[]) =
    let collidedLocations =
        particles
        |> Array.groupBy (fun p -> p.P)
        |> Array.filter (fun (_, p) -> p.Length <> 1)
        |> Array.map fst

    particles
    |> Array.filter (fun p -> collidedLocations |> Array.contains p.P |> not)

let moveParticle (particle: Particle) =
    {particle with V = particle.V + particle.A; 
                   P = particle.P + particle.V + particle.A}

let oneStep (particles: Particle[]) =
    particles 
    |> removeCollided 
    |> Array.map moveParticle

let uncollidedParticles (input: string[]) =
    let particles =
        input
        |> Array.map parseLine

    [0..1000]
    |> List.fold (fun particles _ -> particles |> oneStep) particles
    |> Array.length