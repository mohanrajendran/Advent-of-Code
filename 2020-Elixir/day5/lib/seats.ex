defmodule Seats do
  defp traverseSeats(minRange, maxRange, pass) do
    if pass == "" do
      minRange
    else
      mid = Integer.floor_div(minRange + maxRange, 2)
      case String.next_grapheme(pass) do
        {dir, rest} when dir in ["F", "L"] -> traverseSeats(minRange, mid, rest)
        {dir, rest} when dir in ["B", "R"] -> traverseSeats(mid, maxRange, rest)
        _ -> minRange
      end
    end
  end

  defp getSeatNumber(pass) do
    traverseSeats(1, 1024, pass)
  end

  defp validLeftSeat({left, right}) do
    left >= 8 && right <= 1017 && right - left == 2
  end

  def seats1(contents) do
    contents
    |> String.split("\n", trim: true)
    |> Enum.map(&getSeatNumber/1)
    |> Enum.max
  end

  def seats2(contents) do
    seats = contents
    |> String.split("\n", trim: true)
    |> Enum.map(&getSeatNumber/1)
    |> Enum.sort(&(&1 <= &2))
    
    leftSeat = Enum.zip(seats, Enum.drop(seats, 1))
    |> Enum.find(&validLeftSeat/1)
    |> elem(0)

    leftSeat + 1
  end

  def main(_args) do
    {:ok, contents} = File.read("input.txt")
    IO.puts "part 1: #{seats1(contents)}"
    IO.puts "part 1: #{seats2(contents)}"
  end
end
