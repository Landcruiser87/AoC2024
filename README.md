## 🎄 Advent of Code 2024 🎄

These are my solutions for the [Advent of Code 2024](https://adventofcode.com/2024) challenges. Huge thanks to [anze3db](https://github.com/anze3db) for his excellent [AOC](https://github.com/anze3db/adventofcode/tree/main) python framework. I borrowed alot of his code in the effort to create a more streamlined AOC experience for myself.  Thank you!


### Setup TODO 

First export your cookie session with AOC with the google chrome developer tools  (Literally just go copy it)
Then make a folder in your root titled `secret` and create a text file within called `cookie.txt`.  
The .gitignore will ignore all text files / (and other formats) so it won't get loaded into github. 

### ⭐🎄 Results 🎄⭐

| Day | Stars | Solution | Name | Speed Part 1 | Speed Part 2 | LOC |
| :--- | :----- | :---- | :---------------------------------------------------------------- | ----- | ----- | --- |
| 01  | ⭐⭐ | [Day1](https://github.com/Landcruiser87/AoC2024/blob/main/scripts/day1/day1.py) |[Historian Hysteria](https://adventofcode.com/2024/day/1) | 25 ms | 35 ms | 57 |
| 02  | ⭐⭐ | [Day2](https://github.com/Landcruiser87/AoC2024/blob/main/scripts/day2/day2.py) |[Red-Nosed Reports](https://adventofcode.com/2024/day/2) | 53 ms | 166 ms | 71 |
| 03  | ⭐⭐ | [Day3](https://github.com/Landcruiser87/AoC2024/blob/main/scripts/day3/day3.py) |[Mull it over](https://adventofcode.com/2024/day/3) | 28 ms | 37 ms | 100 |
| 04  | ⭐⭐ | [Day4](https://github.com/Landcruiser87/AoC2024/blob/main/scripts/day4/day4.py) |[Ceres Search](https://adventofcode.com/2024/day/4) |  82 ms | 46 ms | 127 |
| 05  | ⭐⭐ | [Day5](https://github.com/Landcruiser87/AoC2024/blob/main/scripts/day5/day5.py) |[Print Queue](https://adventofcode.com/2024/day/5) |  42 ms | 62 ms | 85 |
| 06  | ⭐ | [Day6](https://github.com/Landcruiser87/AoC2024/blob/main/scripts/day6/day6.py) |[Guard Gallivant](https://adventofcode.com/2024/day/6) |   ms |  ms |  |
| 07  | ⭐⭐ | [Day7](https://github.com/Landcruiser87/AoC2024/blob/main/scripts/day7/day7.py) |[Bridge Repair](https://adventofcode.com/2024/day/7) |  6.25 sec | 5.9 MIN :joy: | 108 |
| 08  |  | [Day8](https://github.com/Landcruiser87/AoC2024/blob/main/scripts/day8/day8.py) |[Resonant Collinearity](https://adventofcode.com/2024/day/8) |  ms | ms | 10 |
#### For next year

- [ ] Make a function that captures the output and updates the results table in the README. SORCERY :mage: :magic_wand: 
- [ ] Make a TUI to view and navigate the leaderboard.
    - It looks like you can request a Json payload every 15 minutes (900 seconds) for public and private leaderboards.  Could write to a JSON configs file in utils with last timestamp accessed. easier to maintain that way. Not sure cacheing would help here as we would want immediate leaderboard updates.  
