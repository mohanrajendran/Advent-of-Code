defmodule Bags do
  defp parseContents(content) do
    if content == "no other bags" do
      []
    else
      content
      |> String.split(", ", trim: true)
      |> Enum.map(&(Regex.named_captures(~r/^(?<count>\d+) (?<color>\w+ \w+) bags?$/, &1)))
    end
  end

  defp parseEntry(line) do
    entry = Regex.named_captures(~r/^(?<container>\w+ \w+) bags contain (?<content>.*).$/, line)
    Map.replace(entry, "content", parseContents(Map.get(entry, "content")))
  end

  defp collectParent(entry) do
    entry["content"]
    |> Enum.map(&({&1["color"], [entry["container"]]}))
    |> Map.new
  end

  defp collectAncestors(parents, color) do
    if !Map.has_key?(parents, color) do
      MapSet.new([color])
    else
      Map.get(parents, color)
      |> Enum.reduce(MapSet.new([color]), fn entry, acc -> MapSet.union(acc, collectAncestors(parents, entry)) end)
    end
  end

  defp childrenCount(entries, color) do
    Map.get(entries, color, [])
    |> Enum.map(&(elem(Integer.parse(&1["count"]),0) * (1 + childrenCount(entries, &1["color"]))))
    |> Enum.sum
  end

  def bags1(contents) do
    contents
    |> String.split("\n", trim: true)
    |> Enum.map(&parseEntry/1)
    |> Enum.map(&collectParent/1)
    |> Enum.reduce(fn entry, acc ->
      Map.merge(entry, acc, fn _k, l1, l2 -> l1 ++ l2 end)
    end)
    |> collectAncestors("shiny gold")
    |> MapSet.delete("shiny gold")
    |> MapSet.size
  end

  def bags2(contents) do
    contents
    |> String.split("\n", trim: true)
    |> Enum.map(&parseEntry/1)
    |> Enum.map(&{&1["container"], &1["content"]})
    |> Map.new
    |> childrenCount("shiny gold")
  end

  def main(_args) do
    {:ok, contents} = File.read("input.txt")
    IO.puts "part 1: #{bags1(contents)}"
    IO.puts "part 2: #{bags2(contents)}"
  end
end
