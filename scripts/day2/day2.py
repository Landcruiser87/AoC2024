import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, _877_cache_now, logger, console
from utils import support
from datetime import datetime
import numpy as np

#Set day/year global variables
DAY:int = 2 #datetime.now().day
YEAR:int = 2024 #datetime.now().year

def test_one(row:list) -> tuple:
    diffs = np.diff(row)
    test1 = bool(np.all(diffs > 0) | np.all(diffs < 0))
    return test1, diffs

def test_two(diffs:np.array) -> np.array:
    locs = np.where((abs(diffs) < 1) | abs(diffs) > 3)[0]
    return locs.size == 0

def check_requirements(row:list, part:int) -> bool:
    test1, diffs = test_one(row)
    test2 = test_two(diffs)
    #First check to see if the report is safe. If it is, return True
    if test1 & test2:
        return True
    else:
        if part == 1:
            #If part 1 and either condition is false.  Return False
            return False
        elif part == 2:
            #If its not safe, remove each level and re-run test_one and test_two
            #to check if its safe.
            for idx in range(len(row)):
                temprow = row.copy()
                temprow.pop(idx)
                test1, diffs = test_one(temprow)
                test2 = test_two(diffs)
                if test1 & test2:
                    return True
            return False

def problemsolver(arr:list, part:int) -> int:
    safezone = 0
    for row in arr:
        row = [int(x) for x in row.split()]
        if check_requirements(row, part):
            safezone += 1
    return safezone

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
    assert testcase == 2, "Test case A failed"
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
    assert testcase == 4, "Test case B failed"
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
#Now we are looking in a nuclear power plant (Ironic that nuclear power is back
#in the story, just as people are starting to accept it for our power hungry LLM
#training!) We can't find the historian here, but the elves there would like us
#to take alook at some odd reports.  Our puzzle input, are one of many reports.
#One report is one line, and each line is separated a list of number reffered
#too as levels.
#Our goal:
#Deem which reports are safe.  
# **If all levels are increasing or decreasing** Check Monotocity
# **Any two levels differ by at least one and at most 3**
# We need to report how many of these levels are safe.  

#Part B Notes
#Now we can allow one bad case to get through on the second test. 
#Should be a simple adjustment but proving difficult. 
#I went wrong here by checking if there was only 1 removal for every
#possible index in the temprow.  Apparently its if any line can be
#made safe with one level removal it still counts as safe.  Not all
#of the level combinations.  
