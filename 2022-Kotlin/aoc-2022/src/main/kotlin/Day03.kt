fun main() {
    fun getScore(ch: Char): Int {
        return when (ch) {
            in ('a'..'z') -> 1 + ch.code - 'a'.code
            in ('A'..'Z') -> 27 + ch.code - 'A'.code
            else -> throw Exception("Unknown char $ch")
        }
    }

    fun getScore(line: String): Int {
        val len = line.length
        val firstItems = line.substring(0, len / 2).toCharArray().toSet()
        val secondItems = line.substring(len / 2).toCharArray().toSet()
        return getScore(firstItems.intersect(secondItems).first())
    }

    fun getGroupScore(group: List<String>): Int {
        val firstItems = group[0].toCharArray().toSet()
        val secondItems = group[1].toCharArray().toSet()
        val thirdItems = group[2].toCharArray().toSet()
        return getScore(firstItems.intersect(secondItems).intersect(thirdItems).first())
    }

    fun part1(input: List<String>): Int {
        return input.sumOf { getScore(it) }
    }

    fun part2(input: List<String>): Int {
        return input.chunked(3).sumOf { getGroupScore(it) }
    }


    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day03_test")
    check(part1(testInput) == 157)
    check(part2(testInput) == 70)

    val input = readInput("Day03_input")
    part1(input).println()
    part2(input).println()
}