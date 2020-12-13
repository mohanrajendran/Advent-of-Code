defmodule SeatsTest do
  use ExUnit.Case
  doctest Seats

  test "seats1 test" do
    {:ok, contents} = File.read("test/test.txt")
    assert Seats.seats1(contents) == 820
  end
end
