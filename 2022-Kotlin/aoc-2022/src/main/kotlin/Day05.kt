class Crates(lines: List<String>) {
    fun applyMoves1() {
        moves.forEach { (count, from, to) ->
            repeat(count) {
                stacks[to]!!.addLast(stacks[from]!!.removeLast())
            }
        }
    }

    fun applyMoves2() {
        moves.forEach { (count, from, to) ->
            val temp = ArrayDeque<Char>()
            repeat(count) {
                temp.addLast(stacks[from]!!.removeLast())
            }
            repeat(count) {
                stacks[to]!!.addLast(temp.removeLast())
            }
        }
    }

    fun getTop(): String {
        return (1..stacks.size).map { stacks[it]!!.last() }.joinToString("")
    }

    private val stacks: Map<Int, ArrayDeque<Char>>
    private val moves: List<Triple<Int, Int, Int>>

    init {
        stacks = mutableMapOf()
        var i = 0
        // Parse stacks
        while (lines[i].contains('[')) {
            var j = 0
            while (j < lines[i].length) {
                if (lines[i][j] == '[') {
                    val idx = 1 + j / 4
                    if (!stacks.containsKey(idx)) {
                        stacks[idx] = ArrayDeque()
                    }
                    stacks[idx]!!.addFirst(lines[i][j + 1])
                }
                j += 1
            }
            i++
        }

        // Skip next two lines
        i += 2

        moves = mutableListOf()
        while (i < lines.size) {
            val s = lines[i].split(" ")
            val count = s[1].toInt()
            val from = s[3].toInt()
            val to = s[5].toInt()
            moves.add(Triple(count, from, to))
            i += 1
        }
    }
}

fun main() {

    fun part1(input: List<String>): String {
        val c = Crates(input)
        c.applyMoves1()
        return c.getTop()
    }

    fun part2(input: List<String>): String {
        val c = Crates(input)
        c.applyMoves2()
        return c.getTop()
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day05_test")
    check(part1(testInput) == "CMZ")
    check(part2(testInput) == "MCD")

    val input = readInput("Day05_input")
    part1(input).println()
    part2(input).println()
}