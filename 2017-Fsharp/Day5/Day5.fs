module Day5

let rec numSteps1 (curLoc: int, steps: int) (instructions: int[]) = 
    if curLoc < 0 || curLoc >= Array.length instructions
    then steps
    else
        let movement = instructions.[curLoc]
        Array.set instructions curLoc (movement + 1)
        instructions
        |> numSteps1(curLoc + movement, steps+1)

let escape1 (input: string[]) =
    input
    |> Array.map int
    |> numSteps1(0, 0)

let rec numSteps2 (curLoc: int, steps: int) (instructions: int[]) = 
    if curLoc < 0 || curLoc >= Array.length instructions
    then steps
    else
        let movement = instructions.[curLoc]
        if movement < 3
        then Array.set instructions curLoc (movement + 1)
        else Array.set instructions curLoc (movement - 1)
        instructions
        |> numSteps2(curLoc + movement, steps+1)

let escape2 (input: string[]) =
    input
    |> Array.map int
    |> numSteps2(0, 0)