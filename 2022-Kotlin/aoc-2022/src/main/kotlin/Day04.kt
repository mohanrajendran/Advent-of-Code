fun main() {
    fun subsumes(line: String): Boolean {
        val (first, second) = line.split(",")
        val (firstStart, firstEnd) = first.split("-").map { it.toInt() }
        val (secondStart, secondEnd) = second.split("-").map { it.toInt() }

        return (firstStart in (secondStart..secondEnd) && firstEnd in (secondStart..secondEnd))
                || (secondStart in (firstStart..firstEnd) && secondEnd in (firstStart..firstEnd))
    }

    fun overlaps(line: String): Boolean {
        val (first, second) = line.split(",")
        val (firstStart, firstEnd) = first.split("-").map { it.toInt() }
        val (secondStart, secondEnd) = second.split("-").map { it.toInt() }

        return (firstStart in (secondStart..secondEnd) || firstEnd in (secondStart..secondEnd))
                || (secondStart in (firstStart..firstEnd) || secondEnd in (firstStart..firstEnd))
    }

    fun part1(input: List<String>): Int {
        return input.count { subsumes(it) }
    }

    fun part2(input: List<String>): Int {
        return input.count { overlaps(it) }
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day04_test")
    check(part1(testInput) == 2)
    check(part2(testInput) == 4)

    val input = readInput("Day04_input")
    part1(input).println()
    part2(input).println()
}