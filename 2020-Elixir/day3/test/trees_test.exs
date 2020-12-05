defmodule TreesTest do
  use ExUnit.Case
  doctest Trees

  test "trees1 test" do
    {:ok, contents} = File.read("test/test.txt")
    assert Trees.trees1(contents) == 7
  end

  test "trees2 test" do
    {:ok, contents} = File.read("test/test.txt")
    assert Trees.trees2(contents) == 336
  end

end
