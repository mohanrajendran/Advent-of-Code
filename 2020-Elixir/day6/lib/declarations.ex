defmodule Declarations do
  defp numAnswers(entries) do
    entries
    |> Enum.flat_map(&String.graphemes/1)
    |> MapSet.new()
    |> MapSet.size()
  end

  defp numCommonAnswers(entries) do
    entries
    |> Enum.map(&String.graphemes/1)
    |> Enum.map(&MapSet.new/1)
    |> Enum.reduce(&MapSet.intersection/2)
    |> MapSet.size()
  end

  def declarations1(contents) do
    contents
    |> String.split("\n", trim: false)
    |> Enum.chunk_while([], fn element, acc -> 
      if String.length(element) != 0 do
        {:cont, acc ++ [element]}
      else
        {:cont, acc, []}
      end
    end, fn acc -> {:cont, acc, []} end)
    |> Enum.map(&numAnswers/1)
    |> Enum.sum()
  end

  def declarations2(contents) do
    contents
    |> String.split("\n", trim: false)
    |> Enum.chunk_while([], fn element, acc -> 
      if String.length(element) != 0 do
        {:cont, acc ++ [element]}
      else
        {:cont, acc, []}
      end
    end, fn acc -> {:cont, acc, []} end)
    |> Enum.map(&numCommonAnswers/1)
    |> Enum.sum()
  end

  def main(_args) do
    {:ok, contents} = File.read("input.txt")
    IO.puts "part 1: #{declarations1(contents)}"
    IO.puts "part 2: #{declarations2(contents)}"
  end
end
