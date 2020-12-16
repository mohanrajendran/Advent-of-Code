defmodule DeclarationsTest do
  use ExUnit.Case
  doctest Declarations

  test "declarations1 test" do
    {:ok, contents} = File.read("test/test.txt")
    assert Declarations.declarations1(contents) == 11
  end

  test "declarations2 test" do
    {:ok, contents} = File.read("test/test.txt")
    assert Declarations.declarations2(contents) == 6
  end
end
