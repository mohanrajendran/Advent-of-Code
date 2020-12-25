defmodule XmasTest do
  use ExUnit.Case
  doctest Xmas

  test "Xmas1 test" do
    {:ok, contents} = File.read("test/test.txt")
    assert Xmas.xmas1(contents, 5) == 127
  end

  test "Xmas2 test" do
    {:ok, contents} = File.read("test/test.txt")
    assert Xmas.xmas2(contents, 5) == 62
  end
end
