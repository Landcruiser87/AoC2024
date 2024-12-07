import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, _877_cache_now, logger, console
from utils import support
from datetime import datetime
from itertools import cycle
from collections import deque

#Set day/year global variables
DAY:int = 6 #datetime.now().day
YEAR:int = 2024 #datetime.now().year

def problemsolver(grid:list, part:int):
    def find_start(target:str="^"):
        res = []
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == target:
                    if part == 2 and target == ".":
                        res.append((x, y))
                    else:
                        return x, y
        return res
    
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
    ox, oy = x, y
    odx, ody = dx, dy
    
    if part == 2:
        pounds = deque(find_start("."))
        px, py = pounds.popleft()
        paradoxes = 0
    else:
        px, py = (-1, -1)

    while onpatrol:
        #First check to see if we've stepped off the board.  Finish criteria
        if not onboard((x + dx, y + dy)):
            #Add the last step out
            if part == 1:
                visited.add((x + dx, y + dy))
                break
            else:
                x, y = ox, oy
                dx, dy = odx, ody
                px, py = pounds.popleft()
                continue

        if grid[x + dx][y + dy] == "#" or (x + dx, y + dy) == (px, py):
            dx, dy = next(DIRS)

        elif (x + dx, y + dy, dx, dy) in visited:
            #Idea here is if it finds a position its already seen (the pound
            #positions) it will have hit an infinite loop because the previous
            #if statement won't trigger a turn.
            paradoxes += 1
            if not len(pounds) > 0:
                break
        else:
            if part == 1:
                visited.add((x, y))
            else:
                visited.add((x, y, dx, dy))
            x += dx
            y += dy

    if part == 1:
        return len(visited)
    if part == 2:
        return paradoxes

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
#Being that we nromally try to avoid infinite loops in programming, this will be hard af to trap.
#
#Idea 1
    #As we're iterating through, count the number of turns to make a loop.  
    #Once we get to 3 turns, put an obstruction NSEW and test for if the loop is infinite?

#Idea 2
    #Throw computer out window

#Idea 2 is looking better to me

#Idea 3
    #Sooo instead of trying to find infinites.  we need to generate them. 
    #To do that, we'll have a deque of every other starting point in the grid (periods) as a possible pound sign. 
    #If the loop returns to that point, we will know that we reached an infinite loop
    #because that spot will already be in the visited set.  
    #Problem is,  I need to add the correct directional component (dx, dy) and I can't quite see how to do that yet. 
