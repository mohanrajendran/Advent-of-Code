import java.util.*

fun main() {
    data class File(val name: String, val size: Long)
    data class Dir(
        val name: String,
        val subDirs: MutableMap<String, Dir> = mutableMapOf(),
        val files: MutableList<File> = mutableListOf()
    ) {
        private var sizeCache = Optional.empty<Long>()
        fun getTotalSize(): Long {
            if (sizeCache.isEmpty) {
                sizeCache = Optional.of(subDirs.values.sumOf { it.getTotalSize() } + files.sumOf { it.size })
            }
            return sizeCache.get()
        }

        fun accumulate(p: (Dir) -> Boolean): List<Dir> {
            val rec = subDirs.values.flatMap { it.accumulate(p) }
            return if (p(this)) {
                rec + this
            } else {
                rec
            }
        }
    }

    fun parse(input: List<String>): Dir {
        val rootDir = Dir("/")
        val dirStack = Stack<Dir>()

        dirStack.add(rootDir)
        var idx = 0
        while (idx < input.size) {
            val curDir = dirStack.last()
            val s = input[idx].split(" ")
            when (s[1]) {
                "cd" -> {
                    when (val dir = s[2]) {
                        "/" -> {
                            dirStack.clear()
                            dirStack.add(rootDir)
                        }

                        ".." -> dirStack.pop()
                        else -> dirStack.add(curDir.subDirs[dir]!!)
                    }
                    idx += 1
                }

                "ls" -> {
                    idx += 1
                    while (idx < input.size && !input[idx].startsWith("$")) {
                        val (first, second) = input[idx].split(" ")
                        when (first) {
                            "dir" -> curDir.subDirs[second] = Dir(second)
                            else -> curDir.files.add(File(second, first.toLong()))
                        }
                        idx += 1
                    }
                }

                else -> {
                    idx += 1
                }
            }
        }

        return rootDir
    }

    fun part1(input: List<String>): Long {
        val rootDir = parse(input)

        return rootDir
            .accumulate { it.getTotalSize() <= 100000L }
            .sumOf { it.getTotalSize() }
    }

    fun part2(input: List<String>): Long {
        val rootDir = parse(input)

        val requiredSpace = rootDir.getTotalSize() - 40000000
        return rootDir
            .accumulate { it.getTotalSize() >= requiredSpace }
            .minByOrNull { it.getTotalSize() }!!
            .getTotalSize()
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day07_test")
    check(part1(testInput) == 95437L)
    check(part2(testInput) == 24933642L)

    val input = readInput("Day07_input")
    part1(input).println()
    part2(input).println()
}