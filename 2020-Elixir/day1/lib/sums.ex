defmodule Sums do
  def sums1(contents) do
    nums = contents
    |> String.split("\n", trim: true)
    |> Enum.map(&String.to_integer/1) 

    numsMap = MapSet.new(nums)

    n1 = nums
    |> Enum.filter(&(MapSet.member?(numsMap, 2020 - &1)))
    |> Enum.at(0)

    n1 * (2020 - n1)
  end

  def sums2(contents) do
    nums = contents
    |> String.split("\n", trim: true)
    |> Enum.map(&String.to_integer/1) 

    numsMap = MapSet.new(nums)

    {n1, n2} = 
      nums
      |> Enum.flat_map(&(for v2 <- nums, do: {&1, v2}))
      |> Enum.filter(fn {v1, v2} -> MapSet.member?(numsMap, 2020 - v1 - v2) end)
      |> Enum.at(0)

    n1 * n2 * (2020 - n1 - n2)
  end

  def main(_args) do
    {:ok, contents} = File.read("input.txt")
    IO.puts "part 1: #{sums1(contents)}"
    IO.puts "part 2: #{sums2(contents)}"
  end
end