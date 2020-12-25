defmodule Xmas do
  defp isSum({window, target}) do
    numsMap = MapSet.new(window)

    window
    |> Enum.any?(&MapSet.member?(numsMap, target - &1))
  end

  defp invalidNumber(numbers, window) do
    numbers
    |> Enum.chunk_every(window, 1, :discard)
    |> Enum.zip(numbers |> Enum.drop(window))
    |> Enum.reject(&isSum/1)
    |> Enum.at(0)
    |> elem(1)
  end

  defp contiguousSum(target, numbers) do
    numRange =
      2..length(numbers)
      |> Enum.flat_map(&(numbers |> Enum.chunk_every(&1, 1, :discard)))
      |> Enum.find(&(Enum.sum(&1) == target))

    Enum.min(numRange) + Enum.max(numRange)
  end

  def xmas1(contents, window) do
    contents
    |> String.split("\n", trim: true)
    |> Enum.map(&String.to_integer/1)
    |> invalidNumber(window)
  end

  def xmas2(contents, window) do
    numbers =
      contents
      |> String.split("\n", trim: true)
      |> Enum.map(&String.to_integer/1)

    numbers
    |> invalidNumber(window)
    |> contiguousSum(numbers)
  end

  def main(_args) do
    {:ok, contents} = File.read("input.txt")
    IO.puts("part 1: #{xmas1(contents, 25)}")
    IO.puts("part 2: #{xmas2(contents, 25)}")
  end
end
