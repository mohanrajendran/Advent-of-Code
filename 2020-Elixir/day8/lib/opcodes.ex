defmodule Opcodes do
  defp parseInstruction(entry) do
    [op, val] =
      entry
      |> String.split(" ", trim: true)

    {value, ""} = Integer.parse(val)

    case op do
      "nop" -> {:nop, value}
      "acc" -> {:acc, value}
      "jmp" -> {:jmp, value}
    end
  end

  defp alterInstructions(pos, instructions) do
    instructions
    |> Enum.with_index()
    |> Enum.map(fn {{op, val}, idx} ->
      cond do
        idx != pos -> {op, val}
        op == :nop -> {:jmp, val}
        op == :jmp -> {:nop, val}
        true -> {op, val}
      end
    end)
  end

  defp nextState(instruction, {pc, acc}) do
    case instruction do
      {:nop, _val} -> {pc + 1, acc}
      {:acc, val} -> {pc + 1, acc + val}
      {:jmp, val} -> {pc + val, acc}
    end
  end

  defp terminates(instructions, visited, {pc, acc}) do
    cond do
      MapSet.member?(visited, pc) ->
        {false, acc}

      pc >= length(instructions) ->
        {true, acc}

      true ->
        next = nextState(Enum.at(instructions, pc), {pc, acc})
        terminates(instructions, MapSet.put(visited, pc), next)
    end
  end

  def opcodes1(contents) do
    {false, acc} =
      contents
      |> String.split("\n", trim: true)
      |> Enum.map(&parseInstruction/1)
      |> terminates(MapSet.new(), {0, 0})

    acc
  end

  def opcodes2(contents) do
    instructions =
      contents
      |> String.split("\n", trim: true)
      |> Enum.map(&parseInstruction/1)

    {true, acc} =
      0..length(instructions)
      |> Enum.map(&alterInstructions(&1, instructions))
      |> Enum.map(&terminates(&1, MapSet.new(), {0, 0}))
      |> Enum.find(&elem(&1, 0))

    acc
  end

  def main(_args) do
    {:ok, contents} = File.read("input.txt")
    IO.puts("part 1: #{opcodes1(contents)}")
    IO.puts("part 2: #{opcodes2(contents)}")
  end
end
