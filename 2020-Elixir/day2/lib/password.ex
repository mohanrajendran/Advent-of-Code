defmodule Password do
  def password1(contents) do
    contents
    |> String.split("\n", trim: true)
    |> Enum.map(&(Regex.named_captures(~r/^(?<min>\d+)-(?<max>\d+) (?<letter>\w): (?<password>\w+)$/, &1))) 
    |> Enum.count(fn(v) ->
      {min_req, ""} = Integer.parse(v["min"])
      {max_req, ""} = Integer.parse(v["max"])

      count = v["password"] 
              |> String.graphemes 
              |> Enum.count(fn(c) -> c == v["letter"] end)
      
      count >= min_req && count <= max_req
    end)
  end

  def password2(contents) do
    contents
    |> String.split("\n", trim: true)
    |> Enum.map(&(Regex.named_captures(~r/^(?<first>\d+)-(?<second>\d+) (?<letter>\w): (?<password>\w+)$/, &1))) 
    |> Enum.count(fn(v) ->
      {first, ""} = Integer.parse(v["first"])
      {second, ""} = Integer.parse(v["second"])

      (String.at(v["password"], first-1) == v["letter"] && String.at(v["password"], second-1) != v["letter"]) ||
      (String.at(v["password"], first-1) != v["letter"] && String.at(v["password"], second-1) == v["letter"]) 
    end)
  end

  def main(_args) do
    {:ok, contents} = File.read("input.txt")
    IO.puts "part 1: #{password1(contents)}"
    IO.puts "part 2: #{password2(contents)}"
  end
end
