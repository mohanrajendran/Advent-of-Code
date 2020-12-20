defmodule OpcodesTest do
  use ExUnit.Case
  doctest Opcodes

  test "Opcodes1 test" do
    {:ok, contents} = File.read("test/test.txt")
    assert Opcodes.opcodes1(contents) == 5
  end

  test "Opcodes2 test" do
    {:ok, contents} = File.read("test/test.txt")
    assert Opcodes.opcodes2(contents) == 8
  end
end
