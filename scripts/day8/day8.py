import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, _877_cache_now, logger, console
from utils import support
from datetime import datetime
from collections import deque
from itertools import combinations

#Set day/year global variables
DAY:int = 8 #datetime.now().day
YEAR:int = 2024 #datetime.now().year

def problemsolver(grid:list, part:int):
    def parse_input():
        antenna = {}
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] != ".":
                    if not grid[x][y] in antenna.keys():
                        antenna[grid[x][y]] = set()
                    antenna[grid[x][y]].add((x,y))
        return antenna
    
    def onboard(point:tuple) -> bool:
        x = point[0]
        y = point[1]
        height, width  = len(grid), len(grid[0])
        if (x < 0) | (x >= height):
            return False
        elif (y < 0) | (y >= width):
            return False
        else:
            return True
    def check_one(x1:int, y1:int, x2:int, y2:int, dx:int, dy:int):
        poundtown = manual["#"]
        #SW -> NE
        anti_1 = (x1 + dx, y1 - dy)
        anti_2 = (x2 - dx, y2 + dy)
        if onboard(anti_1) and onboard(anti_2) and (anti_1 in poundtown) and (anti_2 in poundtown):
            return True
        
    def check_two(x1:int, y1:int, x2:int, y2:int, dx:int, dy:int):
        poundtown = manual["#"]
        #NW -> SE
        anti_3 = (x1 - dx, y1 + dy)
        anti_4 = (x2 + dx, y2 - dy)
        if onboard(anti_3) and onboard(anti_4) and (anti_3 in poundtown) and (anti_4 in poundtown):
            return True

    manual = parse_input()
    positions = 0
    #create the antinodes and then check which locations exist in the antenna["#"] dict
    for ant_type, locs in manual.items():
        if ant_type != "#":
            ant_pile = deque(list(combinations(locs, 2)))
            while ant_pile:
                #Get the point pair
                p1, p2 = ant_pile.popleft()
                #find the diagonals
                x1, y1 = p1
                x2, y2 = p2
                dx = abs(x2 - x1)
                dy = abs(y2 - y1)
                if check_one(x1, y1, x2, y2, dx, dy):
                    positions += 1
                if check_two(x1, y1, x2, y2, dx, dy):
                    positions += 1

    return positions

    #Needs
      #1.Function for identifying the different type of antennas. 
      #2.Function that can determine if there is a straight line. No clue here. 
      #3.Data Container..  
        #Dict of sets?  Sounds fun. 
      #Our job is to count the number of locations that could contain an antinode. 
      #So we need validation functions


@log_time
def part_A():
    logger.info("Solving part A")
    #to check your cache status when you need cache nooooow
    #call J.... G.... WENTWORTH. 
    _877_cache_now() #Lol. I blame myself
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 1)
    # console.log(f"{tellstory}")
    # [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problemsolver(testdata, 1)
    #Assert testcase
    assert testcase == 14, f"Test case A failed returned:{testcase}"
    # logger.info(f"Test case:{testcase} pass for part A")
    #Solve puzzle with full dataset
    answerA = "" #problemsolver(data, 1)
    return answerA

@log_time
def part_B():
    logger.info("Solving part B")
    #Check cache status
    _877_cache_now()
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 2)
    # console.log(f"{tellstory}")
    # [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = "" #problemsolver(testdata, 2)
    #Assert testcase
    assert testcase == "", f"Test case B failed returned:{testcase}"
    # logger.info(f"Test case:{testcase} pass for part B")
    #Solve puzzle with full dataset
    answerB = "" #problemsolver(data, 2)
    return answerB

def main():
    global data
    data = support.pull_inputdata(DAY, YEAR)

    #Solve part A
    resultA = part_A()
    logger.info(f"part A solution: \n{resultA}\n")
    # support.submit_answer(DAY, YEAR, 1, resultA)

    #Solve part B
    # resultB = part_B()
    # logger.info(f"part B solution: \n{resultB}\n")
    # # support.submit_answer(DAY, YEAR, 2, resultB)

    # #Recurse lines of code
    # LOC = support.recurse_dir(f'./scripts/day{DAY}/')
    # logger.info(f"Lines of code \n{LOC}")

    #Delete the cache after submission
    _877_cache_now(".cache", False)
    
if __name__ == "__main__":
    main()

########################################################
#Notes
#Part A Notes

#In particular, an antinode occurs at any point that is perfectly in line with
#two antennas of the same frequency
    #but only when one of the antennas is twice as far away as the other

# oooo Antenna town!  This one sounds quite fun and I think we're going to have
# to do some diagonal raycasting.  Still dont' quite understand how to draw
# the antinodes yet. 
# if a node is drawn, the exact opposite delta difference in distance is wehre
# to place an antinode. 


#freqs can be 
#1. single lowercase letter
#2. single uppercase letter
#3. digit
