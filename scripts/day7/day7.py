import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, _877_cache_now, logger, console
from utils import support
from datetime import datetime
from itertools import combinations as cb
from collections import deque
from itertools import product

#Set day/year global variables
DAY:int = 7 #datetime.now().day
YEAR:int = 2024 #datetime.now().year

def problemsolver(arr:list, part:int):
    def parse_input(arr:list):
        calibrations = {}
        for line in arr:
            total, part = line.split(":")
            calibrations[int(total)] = part.split()
        return calibrations
    
    def recursive_add(input:str, n_idx:int=0, total:int=0):
        if n_idx < len(input):
            nons = [idx for idx, x in enumerate(input) if not x.isnumeric()]
            if len(nons) > 1:
                pass
            total = eval(input[:nons[1]])
            #start here tomorrow.  recursion always hurts
            recursive_add(input[n_idx:], n_idx, total)
        
    cals = parse_input(arr)    
    test_vals = []
    operators = ["+", "*"]
    for test_val, parts in cals.items():
        possibles = product(operators, repeat=len(parts) - 1)
        for possible in possibles:
            part_one = parts[0]
            for num, op in zip(parts[1:], possible):
                part_one += op + num
                weirdmath = recursive_add(part_one)
                if test_val == weirdmath:
                    logger.info(f"Adding:{test_val}")
                    test_vals.append(test_val)

        #gameplan is to check all values 
        #for possible combinations. 
        #can't rearrange. numbers just + or *
        return sum(test_vals)
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
    assert testcase == 3749, f"Test case A failed returned:{testcase}"
    # logger.info(f"Test case:{testcase} pass for part A")
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