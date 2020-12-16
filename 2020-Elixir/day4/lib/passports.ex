defmodule Passports do
  defp requiredFieldsPresent(entries) do
    required_fields = ~w(byr iyr eyr hgt hcl ecl pid)

    fields = entries
    |> Enum.flat_map(&(String.split(&1, " ")))
    |> Enum.map(&(List.first(String.split(&1, ":"))))
    |> MapSet.new()

    required_fields |> Enum.all?(&(MapSet.member?(fields, &1)))
  end

  defp numberIsValid(year, min, max) do
    if year == nil do
      false
    end
    case Integer.parse(year) do
     {year, ""} -> year >= min && year <= max
     _ -> false
    end
  end

  defp heightIsValid(ht) do
    fields = Regex.named_captures(~r/^(?<value>\d+)(?<unit>(in)|(cm))$/, ht)
    cond do
      fields == nil -> false
      fields["unit"] == "cm" -> numberIsValid(fields["value"], 150, 193)
      fields["unit"] == "in" -> numberIsValid(fields["value"], 59, 76)
      true -> false
    end
  end

  defp hairColorIsValid(color) do
    Regex.match?(~r/^#[0-9a-f]{6}$/, color)
  end

  defp eyeColorIsValid(color) do
    ~w(amb blu brn gry grn hzl oth)
    |> MapSet.new()
    |> MapSet.member?(color)
  end

  defp passportIdIsValid(id) do
    Regex.match?(~r/^\d{9}$/, id)
  end

  defp fieldIsValid({key, value}) do
    case {key, value} do
      {"byr", year} -> numberIsValid(year, 1920, 2002)
      {"iyr", year} -> numberIsValid(year, 2010, 2020)
      {"eyr", year} -> numberIsValid(year, 2020, 2030) 
      {"hgt", height} -> heightIsValid(height)
      {"hcl", color} -> hairColorIsValid(color)
      {"ecl", color} -> eyeColorIsValid(color)
      {"pid", id} -> passportIdIsValid(id)
      {"cid", _} -> true
      _ -> false
    end
  end

  defp fieldsAreValid(entries) do
    entries
    |> Enum.flat_map(&(String.split(&1, " ")))
    |> Enum.map(&(String.split(&1, ":")))
    |> Enum.map(&({Enum.at(&1, 0), Enum.at(&1, 1)}))
    |> Enum.all?(&fieldIsValid/1)
  end

  def passports1(contents) do
    contents
    |> String.split("\n", trim: false)
    |> Enum.chunk_while([], fn element, acc -> 
      if String.length(element) != 0 do
        {:cont, acc ++ [element]}
      else
        {:cont, acc, []}
      end
    end, fn acc -> {:cont, acc, []} end)
    |> Enum.count(&requiredFieldsPresent/1)
  end

  def passports2(contents) do
    contents
    |> String.split("\n", trim: false)
    |> Enum.chunk_while([], fn element, acc -> 
      if String.length(element) != 0 do
        {:cont, acc ++ [element]}
      else
        {:cont, acc, []}
      end
    end, fn acc -> {:cont, acc, []} end)
    |> Enum.filter(&requiredFieldsPresent/1)
    |> Enum.count(&fieldsAreValid/1)
  end

  def main(_args) do
    {:ok, contents} = File.read("input.txt")
    IO.puts "part 1: #{passports1(contents)}"
    IO.puts "part 2: #{passports2(contents)}"
  end
end
