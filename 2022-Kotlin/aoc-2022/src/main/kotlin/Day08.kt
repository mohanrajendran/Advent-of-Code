fun main() {
    fun parse(input: List<String>): Array<IntArray> {
        return input.map { line ->
            line.trim().toCharArray().map { it.toString().toInt() }.toIntArray()
        }.toTypedArray()
    }

    fun part1(input: List<String>): Int {
        val grid = parse(input)
        val visible = mutableSetOf<Pair<Int, Int>>()

        for (y in grid.indices) {
            var minSoFar = -1
            for (x in grid[0].indices) {
                if (grid[y][x] > minSoFar) {
                    visible.add(y to x)
                    minSoFar = grid[y][x]
                }
            }

            minSoFar = -1
            for (x in grid[0].indices.reversed()) {
                if (grid[y][x] > minSoFar) {
                    visible.add(y to x)
                    minSoFar = grid[y][x]
                }
            }
        }

        for (x in grid[0].indices) {
            var minSoFar = -1
            for (y in grid.indices) {
                if (grid[y][x] > minSoFar) {
                    visible.add(y to x)
                    minSoFar = grid[y][x]
                }
            }

            minSoFar = -1
            for (y in grid.indices.reversed()) {
                if (grid[y][x] > minSoFar) {
                    visible.add(y to x)
                    minSoFar = grid[y][x]
                }
            }
        }

        return visible.size
    }

    fun getScenicScore(grid: Array<IntArray>, ty: Int, tx: Int): Int {
        var rightScore = 0
        for (y in (ty + 1 until grid.size)) {
            rightScore += 1
            if (grid[y][tx] >= grid[ty][tx]) {
                break
            }
        }

        var leftScore = 0
        for (y in (ty - 1 downTo 0)) {
            leftScore += 1
            if (grid[y][tx] >= grid[ty][tx]) {
                break
            }
        }

        var downScore = 0
        for (x in (tx + 1 until grid[0].size)) {
            downScore += 1
            if (grid[ty][x] >= grid[ty][tx]) {
                break
            }
        }

        var upScore = 0
        for (x in (tx - 1 downTo 0)) {
            upScore += 1
            if (grid[ty][x] >= grid[ty][tx]) {
                break
            }
        }

        return rightScore * leftScore * upScore * downScore
    }

    fun part2(input: List<String>): Int {
        val grid = parse(input)

        var max = 0
        for (x in grid[0].indices) {
            for (y in grid.indices) {
                max = max.coerceAtLeast(getScenicScore(grid, x, y))
            }
        }

        return max
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day08_test")
    check(part1(testInput) == 21)
    check(part2(testInput) == 8)

    val input = readInput("Day08_input")
    part1(input).println()
    part2(input).println()
}