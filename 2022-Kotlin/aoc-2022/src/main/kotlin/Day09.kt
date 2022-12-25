fun main() {
    fun move(h: Pair<Int, Int>, dir: String): Pair<Int, Int> {
        val (hx, hy) = h
        return when (dir) {
            "R" -> hx + 1 to hy
            "L" -> hx - 1 to hy
            "U" -> hx to hy + 1
            "D" -> hx to hy - 1
            else -> hx to hy
        }
    }

    fun follow(t: Pair<Int, Int>, h: Pair<Int, Int>): Pair<Int, Int> {
        val lToh = h.first - t.first to h.second - t.second
        val (tx, ty) = t
        return when (lToh) {
            0 to 2 -> tx to ty + 1
            0 to -2 -> tx to ty - 1
            2 to 0 -> tx + 1 to ty
            -2 to 0 -> tx - 1 to ty
            2 to 1, 1 to 2, 2 to 2 -> tx + 1 to ty + 1
            -2 to 1, -1 to 2, -2 to 2 -> tx - 1 to ty + 1
            2 to -1, 1 to -2, 2 to -2 -> tx + 1 to ty - 1
            -2 to -1, -1 to -2, -2 to -2 -> tx - 1 to ty - 1
            else -> tx to ty
        }
    }

    fun part1(input: List<String>): Int {
        val visited = mutableSetOf<Pair<Int, Int>>()
        var h = 0 to 0
        var t = 0 to 0
        visited.add(t)

        for (line in input) {
            val s = line.trim().split(" ")
            val dir = s[0]
            val distance = s[1].toInt()

            for (d in 1..distance) {
                h = move(h, dir)
                t = follow(t, h)
                visited.add(t)
            }
        }
        return visited.size
    }

    fun part2(input: List<String>): Int {
        val visited = mutableSetOf<Pair<Int, Int>>()
        val points = mutableListOf<Pair<Int, Int>>()
        repeat(10) {
            points.add(0 to 0)
        }
        visited.add(points.last())

        var idx = 0
        for (line in input) {
            val s = line.trim().split(" ")
            val dir = s[0]
            val distance = s[1].toInt()
            idx += 1

            for (d in 1..distance) {
                points[0] = move(points[0], dir)
                for (i in 1 until 10) {
                    points[i] = follow(points[i], points[i - 1])
                }
                visited.add(points.last())
            }
        }

        return visited.size
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day09_test")
    val testInput2 = readInput("Day09_test2")
    check(part1(testInput) == 13)
    check(part2(testInput) == 1)
    check(part2(testInput2) == 36)

    val input = readInput("Day09_input")
    part1(input).println()
    part2(input).println()
}