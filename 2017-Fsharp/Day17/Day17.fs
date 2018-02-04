module Day17
open System

type CircularBuffer = {buffer: int list; headIdx: int}
let startingBuffer = {buffer = [0]; headIdx = 0}

let insertIntoBuffer (stepSize: int) (buffer: CircularBuffer) (value: int) =
    let curIdx = buffer.headIdx
    let nextIdx = 1 + (curIdx + stepSize) % buffer.buffer.Length
    let (head, tail) = buffer.buffer |> List.splitAt nextIdx
    {buffer = head @ [value] @ tail; headIdx = nextIdx}

let after2017 (buffer: CircularBuffer) =
    buffer.buffer |> List.item ((buffer.headIdx + 1) % buffer.buffer.Length)

let itemAfter2017 (stepSize: int) =
    {1..2017}
    |> Seq.fold (insertIntoBuffer stepSize) startingBuffer
    |> after2017

type RestrictedBuffer = {secondDigit: int; length: int; headIdx: int}
let startingRestrictedBuffer = {secondDigit = -1; length = 1; headIdx = 0}

let insertIntoRestrictedBuffer (stepSize: int) (buffer: RestrictedBuffer) (value: int) =
    let curIdx = buffer.headIdx
    let nextIdx = 1 + (curIdx + stepSize) % buffer.length
    if nextIdx = 1
    then {secondDigit = value; length = buffer.length + 1; headIdx = nextIdx}
    else {buffer with length = buffer.length + 1; headIdx = nextIdx}

let itemAfter0 (stepSize: int) =
    {1..50000000}
    |> Seq.fold (insertIntoRestrictedBuffer stepSize) startingRestrictedBuffer
    |> fun b -> b.secondDigit