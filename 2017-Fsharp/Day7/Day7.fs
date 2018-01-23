module Day7
open System.Text.RegularExpressions
open System

type ParsedNode = {name: string; weight: int; children: string list;}

let parseLine(line: string): ParsedNode =
    let pattern = @"^(?<name>\w+) \((?<weight>\d+)\)( -> (?<children>[\w, ]+))?"
    let re = Regex.Match(line, pattern, RegexOptions.IgnoreCase)
    let name = re.Groups.["name"].Value
    let weight = re.Groups.["weight"].Value |> int
    let children = re.Groups.["children"].Value.Split([|", "|], StringSplitOptions.RemoveEmptyEntries)
                   |> Seq.toList
    {name = name; weight = weight; children = children }

let nodeNames(parsedNodes: ParsedNode seq) =
    parsedNodes
    |> Seq.map (fun n -> n.name)

let childSet(parsedNodes: ParsedNode seq) =
    parsedNodes
    |> Seq.collect (fun n -> n.children)

let bottomProgram(input: string seq) = 
    let parsedNodes = input |> Seq.map parseLine
    let allNodeNames = parsedNodes |> nodeNames
    let childNodeNames = parsedNodes |> childSet

    allNodeNames
    |> Seq.find (fun name -> not (Seq.contains name childNodeNames))

type balancedResult = {result: int option; nodeWeight: int; cumulativeWeight: int}

let rec balancedProgram (programMap: Map<string, ParsedNode>) (nodeName: string) =
    let node = programMap |> Map.find nodeName
    let childBalance = node.children |> List.map (balancedProgram programMap)

    // Check if child already contains result
    let childResults = 
        childBalance
        |> List.map (fun n -> n.result)
        |> List.choose id
    if childResults.Length = 1
    then {result = Some(childResults.[0]); nodeWeight = -1; cumulativeWeight = -1}
    else 
        let childWeights =
            childBalance
            |> List.map (fun n -> n.cumulativeWeight)
        // Check if a weight is different
        let groupedChildrenByWeight = 
            childBalance
            |> List.groupBy (fun n -> n.cumulativeWeight)
            |> List.sortBy snd
        if groupedChildrenByWeight.Length <> 2
        then {result = None; nodeWeight = node.weight; cumulativeWeight = node.weight + (childWeights |> List.sum)}
        else 
            let expectedWeight =
                groupedChildrenByWeight.[1]
                |> snd
                |> List.head
                |> (fun n -> n.cumulativeWeight)
            let oddChild = 
                groupedChildrenByWeight.[0] 
                |> snd 
                |> List.head
            let balancedWeight = oddChild.nodeWeight - (oddChild.cumulativeWeight - expectedWeight)
            {result = Some(balancedWeight); nodeWeight = -1; cumulativeWeight = -1}

let balancedProgramWeight(input: string seq) =
    let rootName = input |> bottomProgram
    let parsedNodeMap = 
        input 
        |> Seq.map (parseLine >> fun n -> (n.name, n))
        |> Map.ofSeq

    match (balancedProgram parsedNodeMap rootName).result with
    | Some(res) -> res
    | None -> -1