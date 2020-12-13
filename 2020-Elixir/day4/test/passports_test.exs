defmodule PassportsTest do
  use ExUnit.Case
  doctest Passports

  test "passports1 test" do
    {:ok, contents} = File.read("test/test.txt")
    assert Passports.passports1(contents) == 2
  end

  test "passports2 valid test" do
    {:ok, contents} = File.read("test/test_valid.txt")
    assert Passports.passports2(contents) == 4
  end

  test "passports2 invalid test" do
    {:ok, contents} = File.read("test/test_invalid.txt")
    assert Passports.passports2(contents) == 0
  end
end
