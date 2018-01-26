module Day9

type StreamState = {groupDepth: int; garbageMode: bool; commentPrev: bool; cumulativeScore: int}
let emptyState = {groupDepth = 0; garbageMode = false; commentPrev = false; cumulativeScore = 0}

let processGroups (state: StreamState) (ch: char) = 
    if state.commentPrev
    then { state with commentPrev = false}
    else if state.garbageMode
    then 
        match ch with
        | '>' -> { state with garbageMode = false }
        | '!' -> { state with commentPrev = true }
        | _   -> state
    else
        match ch with
        | '<' -> { state with garbageMode = true }
        | '{' -> { state with groupDepth = state.groupDepth + 1}
        | '}' -> { state with groupDepth = state.groupDepth - 1; 
                              cumulativeScore = state.cumulativeScore + state.groupDepth}
        | _   -> state

let groupSize (line: string) =
    line
    |> Seq.fold processGroups emptyState
    |> (fun s -> s.cumulativeScore)

let processGarbage (state: StreamState) (ch: char) =
    if state.commentPrev
    then { state with commentPrev = false}
    else if state.garbageMode
    then 
        match ch with
        | '>' -> { state with garbageMode = false }
        | '!' -> { state with commentPrev = true }
        | _   -> { state with cumulativeScore = state.cumulativeScore + 1}
    else
        match ch with
        | '<' -> { state with garbageMode = true }
        | _   -> state 

let garbageSize (line: string) =
    line
    |> Seq.fold processGarbage emptyState
    |> (fun s -> s.cumulativeScore)