import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, _877_cache_now, logger, console
from utils import support
from datetime import datetime
from itertools import cycle

#Set day/year global variables
DAY:int = 6 #datetime.now().day
YEAR:int = 2024 #datetime.now().year

def problemsolver(grid:list, part:int):
    def find_start():
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "^":
                    return x, y
    
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

    DIRS = cycle([(-1, 0), (0, 1), (1, 0),(0, -1)])
    dx, dy = next(DIRS)
    x, y = find_start()
    visited = set()
    onpatrol = True
    while onpatrol:
        if not onboard((x + dx, y + dy)):
            visited.add((x + dx, y + dy))
            onpatrol = False
        elif grid[x + dx][y + dy] == "#":
            dx, dy = next(DIRS)
        else:
            visited.add((x, y))
            x += dx
            y += dy

    if part == 1:
        return len(visited)
    if part == 2:
        return "butthead"

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
    assert testcase == 41, f"Test case A failed returned:{testcase}"
    #Solve puzzle with full dataset
    answerA = problemsolver(data, 1)
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
    testcase = problemsolver(testdata, 2)
    #Assert testcase
    assert testcase == 6, f"Test case B failed returned:{testcase}"
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
    resultB = part_B()
    logger.info(f"part B solution: \n{resultB}\n")
    # support.submit_answer(DAY, YEAR, 2, resultB)

    #Recurse lines of code
    LOC = support.recurse_dir(f'./scripts/day{DAY}/')
    logger.info(f"Lines of code \n{LOC}")

    #Delete the cache after submission
    _877_cache_now(".cache", False)
    
if __name__ == "__main__":
    main()

########################################################
#Notes
#Part A Notes
#
# Well this onee.... i dunno.  feels like dfs but I might be able to just count the unique path positions
# Only rule is that when you hit a # block, you have to turn 90deg to the right. 
#
#Part B
#Now... we have to find a way to place objects that will create infinite loops (ie -time paradoxes in the story)
#Being that we nromally try to avoid infinite loops in programming, this will be interesting to trap.
#
#Idea 1
    #As we're iterating through, count the number of turns to make a loop.  
    #Once we get to 3 turns, put an obstruction NSEW and test for if the loop is infinite?

#Idea 2
    #Throw computer out window

#Idea 2 is looking better to me