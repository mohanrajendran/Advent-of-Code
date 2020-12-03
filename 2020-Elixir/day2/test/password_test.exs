defmodule PasswordTest do
  use ExUnit.Case
  doctest Password

  test "password1 test" do
    {:ok, contents} = File.read("test/test.txt")
    assert Password.password1(contents) == 2
  end

  test "password2 test" do
    {:ok, contents} = File.read("test/test.txt")
    assert Password.password2(contents) == 1
  end
end
