module Day3

type Direction = Left | Up | Right | Down

let move (x:int, y: int) (direction: Direction) =
    match direction with
    | Right -> (x+1, y)
    | Up -> (x, y+1)
    | Left -> (x-1, y)
    | Down -> (x, y-1)

let steps: seq<Direction> = 
    let moveSteps (numSteps: int) =
        if numSteps % 2 = 1
        then List.append (List.replicate numSteps Right) (List.replicate numSteps Up)
        else List.append (List.replicate numSteps Left) (List.replicate numSteps Down)
    
    Seq.initInfinite id
    |> Seq.collect moveSteps

let positions: seq<int * int> =
    steps
    |> Seq.scan move (0,0)

let distance (x: int, y: int): int =
    abs(x) + abs(y)

let ulam1 (port: int) = 
    Seq.item (port - 1) positions
    |> distance

let neighbors (x: int, y: int) =
    [(0,1); (1,0); (0,-1); (-1,0); (1,-1); (-1,1); (1,1); (-1,-1)]
    |> List.map (fun (xm, ym) -> (x+xm, y+ym))

let sumAndAdd (calculated: Map<int*int, int>) (location: int*int) =
    let summands = 
        neighbors location
        |> List.choose (fun (neighbor) -> calculated |> Map.tryFind neighbor)
    let s =
        if List.isEmpty summands
        then 1
        else List.sum summands
    calculated |> Map.add location s

let ulam2 (limit: int): int =
    let calculated = 
        positions
        |> Seq.scan sumAndAdd Map.empty
        |> Seq.skip 1
    Seq.zip calculated positions
    |> Seq.map (fun (c, p) -> Map.find p c)
    |> Seq.find (fun (v) -> v > limit)