module Day11

let parseInput (input: string) =
    input.Split([|','|])
    |> Seq.ofArray

type Coordinate = {x: int; y: int}

let move (location: Coordinate) (direction: string) =
    match direction with
    | "ne" -> {location with x = location.x + 1; y = location.y + 1}
    | "n"  -> {location with y = location.y + 1}
    | "nw" -> {location with x = location.x - 1}
    | "sw" -> {location with x = location.x - 1; y = location.y - 1}
    | "s"  -> {location with y = location.y - 1}
    | "se" -> {location with x = location.x + 1}
    | _ -> failwithf "unknown direction %s" direction

let distanceFromOrigin (location: Coordinate) =
    max (location.x |> abs) (location.y |> abs)

let hexDistance (input: string) =
    input
    |> parseInput
    |> Seq.fold move {x = 0; y = 0}
    |> distanceFromOrigin

let maxHexDistance (input: string) = 
    input
    |> parseInput
    |> Seq.scan move {x = 0; y = 0}
    |> Seq.map distanceFromOrigin
    |> Seq.max