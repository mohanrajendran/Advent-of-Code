fun main() {
    fun chunkTillEmpty(input: List<String>): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        var temp = mutableListOf<Int>()
        for (i in input) {
            if (i.isEmpty()) {
                result.add(temp)
                temp = mutableListOf<Int>()
            } else {
                temp.add(i.toInt())
            }
        }
        result.add(temp)
        return result
    }

    fun part1(input: List<String>): Int {
        return chunkTillEmpty(input).maxOf { it.sum() }
    }

    fun part2(input: List<String>): Int {
        return chunkTillEmpty(input).map { it.sum() }.sortedDescending().take(3).sum()
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day01_test")
    check(part1(testInput) == 24000)
    check(part2(testInput) == 45000)

    val input = readInput("Day01_input")
    part1(input).println()
    part2(input).println()
}