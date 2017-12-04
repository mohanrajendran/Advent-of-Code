module Day3

let distance (x: int, y: int): int =
    abs(x) + abs(y)

let perfectOddSquareBelow (x: int): int =
    let rec helper (v: int): int =
        if v*v <= x
        then helper(v+2)
        else v-2
    helper (1)

let ulam (port: int): int =
    let squareBelow = perfectOddSquareBelow port
    let offset = port - (squareBelow * squareBelow)
    if offset = 0
    then distance (squareBelow / 2, squareBelow / 2)
    else
        let width = squareBelow + 1
        let moves = offset % width
        distance (squareBelow / 2 + 1, squareBelow / 2 - (moves - 1))