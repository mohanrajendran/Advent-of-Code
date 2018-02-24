module Day19
open System

type Direction = Left | Right | Up | Down

let rec traverse (grid: char[][]) (x: int, y: int) (direction: Direction) = 
    let validPos (x: int, y: int) =
        x >= 0 && x < grid.Length && y >= 0 && y < grid.[0].Length && grid.[x].[y] <> ' '

    let nextDirections (direction: Direction) =
        match direction with
        | Left -> [Left; Up; Down]
        | Right -> [Right; Up; Down]
        | Up -> [Up; Left; Right]
        | Down -> [Down; Left; Right]

    let nextPosition (x: int, y: int) (direction: Direction) =
        match direction with
        | Left -> (x, y-1)
        | Right -> (x, y+1)
        | Up -> (x-1, y)
        | Down -> (x+1, y)
    
    seq {
        let c = grid.[x].[y]
        yield c

        // Next position
        let nextDirection = 
            direction
            |> nextDirections
            |> List.tryFind (fun d -> d |> nextPosition (x,y) |> validPos)
    
        match nextDirection with
        | None -> ()
        | Some direction -> yield! traverse grid (direction |> nextPosition (x,y)) direction
    }

let parseAndTraverse (input: string[]) =
    let splitInput =
        input
        |> Array.map Seq.toArray
    let startingColumn = 
        splitInput.[0]
        |> Array.findIndex (fun c -> c = '|')

    traverse splitInput (0, startingColumn) Down

let traversedLetters (input: string[]) =
    input
    |> parseAndTraverse
    |> Seq.filter (fun c -> List.contains c ['A'..'Z'])
    |> String.Concat

let traversedDistance (input: string[]) =
    input
    |> parseAndTraverse
    |> Seq.length