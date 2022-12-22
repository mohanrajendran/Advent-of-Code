enum class RPS(val score: Int) {
    ROCK(1),
    PAPER(2),
    SCISSORS(3);

    companion object {
        fun outcome(opponent: RPS, self: RPS): Outcome {
            return when (opponent to self) {
                PAPER to ROCK, ROCK to SCISSORS, SCISSORS to PAPER -> Outcome.LOSE
                ROCK to PAPER, PAPER to SCISSORS, SCISSORS to ROCK -> Outcome.WIN
                else -> Outcome.DRAW
            }
        }

        fun self(opponent: RPS, outcome: Outcome): RPS {
            return when (outcome) {
                Outcome.DRAW -> opponent
                Outcome.WIN -> when (opponent) {
                    ROCK -> PAPER
                    PAPER -> SCISSORS
                    SCISSORS -> ROCK
                }

                Outcome.LOSE -> when (opponent) {
                    ROCK -> SCISSORS
                    SCISSORS -> PAPER
                    PAPER -> ROCK
                }
            }
        }
    }
}

enum class Outcome(val score: Int) {
    WIN(6),
    DRAW(3),
    LOSE(0)
}

fun main() {
    val choices = mapOf(
        "A" to RPS.ROCK,
        "B" to RPS.PAPER,
        "C" to RPS.SCISSORS,
        "X" to RPS.ROCK,
        "Y" to RPS.PAPER,
        "Z" to RPS.SCISSORS
    )

    val outcomes = mapOf(
        "X" to Outcome.LOSE,
        "Y" to Outcome.DRAW,
        "Z" to Outcome.WIN
    )

    fun getScore(opponent: RPS, self: RPS): Int {
        return RPS.outcome(opponent, self).score + self.score
    }

    fun part1(input: List<String>): Int {
        return input.sumOf { line ->
            val (opponent, self) = line.trim().split(" ").map { choices[it]!! }
            getScore(opponent, self)
        }
    }

    fun part2(input: List<String>): Int {
        return input.sumOf { line ->
            val (opp, out) = line.trim().split(" ")
            val opponent = choices[opp]!!
            val outcome = outcomes[out]!!
            getScore(opponent, RPS.self(opponent, outcome))
        }
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day02_test")
    check(part1(testInput) == 15)
    check(part2(testInput) == 12)

    val input = readInput("Day02_input")
    part1(input).println()
    part2(input).println()
}