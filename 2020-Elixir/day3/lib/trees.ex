defmodule Trees do
  defp traverse(contents, right, down) do
    contents
    |> String.split("\n", trim: true)
    |> Enum.take_every(down)
    |> Enum.with_index(0)
    |> Enum.map(fn {row, i} -> String.at(row, rem(0+right*i, String.length(row))) end)
    |> Enum.filter(&(&1 == "#"))
    |> Enum.count()
  end

  def trees1(contents) do
    contents
    |> traverse(3, 1)
  end

  def trees2(contents) do
    [{1,1}, {3,1}, {5,1}, {7,1}, {1,2}]
    |> Enum.reduce(1, fn {right, down}, acc -> traverse(contents, right, down) * acc end)
  end

  def main(_args) do
    {:ok, contents} = File.read("input.txt")
    IO.puts "part 1: #{trees1(contents)}"
    IO.puts "part 2: #{trees2(contents)}"
  end
end