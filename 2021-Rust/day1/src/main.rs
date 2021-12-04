use std::fs::File;
use std::io::{self,BufRead};

fn main() {
    println!("part1:- {}", part1(read_input("input.txt")));
    println!("part1:- {}", part2(read_input("input.txt")));
}

pub fn read_input(filename: &str) -> Vec<u32> {
    let file = File::open(filename).unwrap();
    let lines = io::BufReader::new(file).lines();

    lines
    .map(|x| x.unwrap().parse::<u32>().unwrap())
    .collect()
}

pub fn part1(input: Vec<u32>) -> usize {
    input.windows(2)
    .filter(|x| x[1] > x[0])
    .count()
}

pub fn part2(input: Vec<u32>) -> usize {
    input.windows(4)
    .filter(|x| x[3] > x[0])
    .count()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_sample() {
        let test_input = read_input("test.txt");
        assert_eq!(part1(test_input), 7);
    }

    #[test]
    fn part2_sample() {
        let test_input = read_input("test.txt");
        assert_eq!(part2(test_input), 5);
    }
}
