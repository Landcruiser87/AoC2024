import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, _877_cache_now, logger, console
from utils import support
from datetime import datetime
from rich.text import Text
from rich.table import Table

#Set day/year global variables
DAY:int = 4 #datetime.now().day
YEAR:int = 2024 #datetime.now().year
DIRLIST = [
    (-1, -1), (-1, 0), (-1, 1),  #one row up
    (0, -1), (0, 1),             #left and right of POI
    (1, -1), (1, 0), (1, 1)      #one row down
]

def problemsolver(grid:list, part:int):
    # def print_grid(x:int, y:int):
    #     console.clear()
    #     table = Table(show_header=False, show_lines=False, box=None)
    #     [table.add_column(justify="center") for x in range(len(grid[0]))]
        
    #     for idx, row in enumerate(grid):
    #         trow = []
    #         for idy, val in enumerate(row):
    #             if idx == x and idy == y: 
    #                 trow.append(Text(val, style="bold red"))
    #             else:
    #                 trow.append(val)
    #         table.add_row(*trow)
    #     console.print(table)
    #     time.sleep(1)

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
    
    def is_xmas(grid:int, x:int, y:int, delt:tuple=None, word:list=None):
        #Terminate conditions
        #Check to see if we've reached the end of XMAS
        if len(word) == 0:
            return True

        #2.See if its on the board
        if not onboard((x, y)):
            return False

        #3. If if the grid letter is not equal to the next index
        if grid[x][y] != word[0]:
            return False
        
        if part == 1:
            return is_xmas(grid, x+delt[0], y+delt[1], delt, word[1:])
        elif part == 2:
            return True

    def look_for_xmas(grid, x, y, searchterm):
        count = 0
        for delt in DIRLIST:
            if is_xmas(grid, x, y, delt, list(searchterm)):
                count += 1
        return count
    
    def look_diag(grid, x, y, i, j):
        return is_xmas(grid, x + i[0], y + i[1], word="M") and is_xmas(grid, x + j[0], y + j[1], word="S")

    def look_for_mas(grid, x, y):
        #Check each corner of the A for the rest of MAS
        cond1 = look_diag(grid, x, y, (-1, -1), (+1, +1)) or look_diag(grid, x, y, (+1, +1), (-1, -1)) 
        cond2 = look_diag(grid, x, y, (-1, +1), (+1, -1)) or look_diag(grid, x, y, (+1, -1), (-1, +1))
        if cond1 and cond2:
            return True
        else:
            return False
    
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if part == 1:
                if grid[x][y] == "X":
                    count += look_for_xmas(grid, x, y, "XMAS")
            elif part == 2:
                if grid[x][y] == "A":
                    if look_for_mas(grid, x, y):
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
    assert testcase == 18, f"Test case A failed returned:{testcase}"
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
    assert testcase == 9, f"Test case B failed returned:{testcase}"
    #Solve puzzle with full dataset
    answerB = problemsolver(data, 2)
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
    _877_cache_now(".cache", True)
    
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

#Adjust lines 
#170 -> -3
#174 -> -1