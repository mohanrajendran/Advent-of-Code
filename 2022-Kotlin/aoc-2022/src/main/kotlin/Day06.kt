fun main() {

    fun firstMarker(line: String, numMarkers: Int): Int {
        val prev = ArrayDeque<Char>()
        var idx = 0
        while (idx < numMarkers) {
            prev.addLast(line[idx])
            idx += 1
        }

        while (prev.toSet().size != numMarkers) {
            prev.removeFirst()
            prev.addLast(line[idx])
            idx += 1
        }

        return idx
    }

    fun part1(input: List<String>): List<Int> {
        return input.map { firstMarker(it,4) }
    }

    fun part2(input: List<String>): List<Int> {
        return input.map { firstMarker(it,14) }
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day06_test")
    check(part1(testInput) == listOf(7, 5, 6, 10, 11))
    check(part2(testInput) == listOf(19, 23, 23, 29, 26))

    val input = readInput("Day06_input")
    part1(input)[0].println()
    part2(input)[0].println()
}