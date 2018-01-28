module Day12
open System.Text.RegularExpressions

let parseToAdjacencyMap (mapSoFar: Map<int, int list>) (line: string) =
    let pattern = @"^(?<fromNode>\d+) <-> (?<toNodes>(\d+, )*\d+)$"
    let re = Regex.Match(line.Trim(), pattern, RegexOptions.None)
    let fromNode = re.Groups.["fromNode"].Value |> int
    let toNodes = re.Groups.["toNodes"].Value.Split([|','|]) 
                  |> Array.map int
                  |> Array.toList

    mapSoFar |> Map.add fromNode toNodes

let rec visitedNodes (toVisit: int list, visited: Set<int>) (adjacencyMap: Map<int, int list>) =
    if toVisit.IsEmpty
    then visited
    else
        let currentNode = toVisit.Head
        let newVisited  = visited |> Set.add currentNode
        let newToVisit = 
            adjacencyMap 
            |> Map.find currentNode
            |> List.filter (fun nextNode -> newVisited |> Set.contains nextNode |> not)
            |> List.append toVisit.Tail
        visitedNodes (newToVisit, newVisited) adjacencyMap

let numConnected (origin: int) (input: string array) = 
    input
    |> Array.fold parseToAdjacencyMap Map.empty
    |> visitedNodes ([origin], Set.empty)
    |> Set.count

let rec visitAllNodes (toVisit: Set<int>, groupsSoFar: int) (adjacencyMap: Map<int, int list>) =
    if toVisit.IsEmpty
    then groupsSoFar
    else
        let firstNode = toVisit |> Set.toSeq |> Seq.head
        let nodesInGroup = visitedNodes ([firstNode], Set.empty) adjacencyMap
        let nodesToVisit = Set.difference toVisit nodesInGroup
        visitAllNodes (nodesToVisit, groupsSoFar + 1) adjacencyMap 

let numGroups (input: string array) =
    let adjacencyMap = 
        input
        |> Array.fold parseToAdjacencyMap Map.empty
    visitAllNodes (adjacencyMap |> Map.toSeq |> Seq.map fst |> Set.ofSeq, 0) adjacencyMap
    
    