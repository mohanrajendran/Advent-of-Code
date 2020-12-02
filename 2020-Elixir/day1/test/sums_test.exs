defmodule SumsTest do
  use ExUnit.Case
  doctest Sums

  test "sums1 test" do
    {:ok, contents} = File.read("test/test.txt")
    assert Sums.sums1(contents) == 514579
  end

  test "sums2 test" do
    {:ok, contents} = File.read("test/test.txt")
    assert Sums.sums2(contents) == 241861950
  end
end
