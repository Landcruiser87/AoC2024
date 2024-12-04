import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, _877_cache_now, logger, console
from utils import support
from datetime import datetime
from collections import deque

#Set day/year global variables
DAY:int = datetime.now().day
YEAR:int = datetime.now().year
DIRLIST = [
    (-1, -1), (-1, 0), (-1, 1),  #one row up
    (0, -1), (0, 1),             #left and right of POI
    (1, -1), (1, 0), (1, 1)      #one row down
]

def problemsolver(grid:list, part:int):
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
    
    def dfs(grid:int, x:int, y:int, word:str, index:int, visited:set):
        #First check terminate conditions
        #1. If its on the board
        cond1 = not onboard((x, y))
        if cond1:
            return False

        #2. If we've already visited
        cond2 = (x, y) in visited
        #3. If if the grid letter is not equal to the next index
        cond3 = grid[x][y] != word[index]
        
        if cond2 | cond3:
            return False
        
        #Separate term to see if we've found the word
        if index == len(word) - 1:
            return True
        
        visited.add((x, y))

        for dx, dy in DIRLIST:
            if dfs(grid, x + dx, y + dy, word, index + 1, visited):
                return True
        
        visited.remove((x,y))
        return False

    count = 0
    searchterm = "XMAS"
    visited = set()
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "X":
                if dfs(grid, x, y, searchterm, 0, visited):
                    count += 1
    
    return count
        
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
    assert testcase == 18, "Test case A failed"
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
    assert testcase == "", "Test case B failed"
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
#Today we're helping with a word puzzle.
#Main Goal
    #Count all the words of XMAS in the puzzle. 
#Conditions:
    #The word search allows for movement in these directions
        #-horizontal
        #-vertical
        #-diagonal
        #-backwards
        #-overlapping
#
#Initial idea
#Find all the X locations (aka starts) in the grid
#Have an iterative scan in all 8 directions around a particular point. 
#Run it in a DFS search
#Must haves
    #I will need to test if its on the board
    #I will probably need to use a cycle to make sure
    #my progression stays correct. 