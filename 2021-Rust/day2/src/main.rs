use std::fs::File;
use std::io::{self,BufRead};

fn main() {
    println!("part1:- {}", part1(read_input("input.txt")));
    println!("part1:- {}", part2(read_input("input.txt")));
}

enum Direction {
    Forward,
    Down,
    Up
}

pub struct Movement{
    direction: Direction,
    distance: u32
}

pub fn read_input(filename: &str) -> Vec<Movement> {
    let file = File::open(filename).unwrap();
    let lines = io::BufReader::new(file).lines();

    lines
    .map(|x| read_line(x.unwrap()))
    .collect()
}

fn read_line(line: String) -> Movement {
    let mut s = line.split_whitespace();
    let m = match s.next().unwrap() {
        "forward" => Direction::Forward,
        "down" => Direction::Down,
        "up" => Direction::Up,
        _ => panic!("Unexpected direction")
    };
    let d = s.next().unwrap().parse::<u32>().unwrap();

    
    Movement{direction: m, distance: d}
}

pub fn part1(input: Vec<Movement>) -> u32 {
    let mut depth = 0;
    let mut horizontal = 0;

    for movement in input {
        match movement.direction {
            Direction::Forward => horizontal = horizontal + movement.distance,
            Direction::Down => depth = depth + movement.distance,
            Direction::Up => depth = depth - movement.distance
        }
    }

    depth * horizontal
}

pub fn part2(input: Vec<Movement>) -> u32 {
    let mut depth = 0;
    let mut horizontal = 0;
    let mut aim = 0;

    for movement in input {
        match movement.direction {
            Direction::Forward => {
                horizontal = horizontal + movement.distance;
                depth = depth + aim * movement.distance;
            },
            Direction::Down => aim = aim + movement.distance,
            Direction::Up => aim = aim - movement.distance
        }
    }

    depth * horizontal
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_sample() {
        let test_input = read_input("test.txt");
        assert_eq!(part1(test_input), 150);
    }

    #[test]
    fn part2_sample() {
        let test_input = read_input("test.txt");
        assert_eq!(part2(test_input), 900);
    }
}
