defmodule BagsTest do
  use ExUnit.Case
  doctest Bags

  test "Bags1 test" do
    {:ok, contents} = File.read("test/test.txt")
    assert Bags.bags1(contents) == 4
  end

  test "Bags2 test1" do
    {:ok, contents} = File.read("test/test.txt")
    assert Bags.bags2(contents) == 32
  end

  test "Bags2 test2" do
    {:ok, contents} = File.read("test/test2.txt")
    assert Bags.bags2(contents) == 126
  end
end
