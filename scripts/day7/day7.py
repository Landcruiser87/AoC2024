import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, _877_cache_now, logger, console
from utils import support
from datetime import datetime
from itertools import product
import numpy as np

#Set day/year global variables
DAY:int = 7 #datetime.now().day
YEAR:int = 2024 #datetime.now().year

def problemsolver(arr:list, part:int):
    def parse_input(arr:list):
        calibrations = {}
        for line in arr:
            total, part = line.strip().split(":")
            calibrations[total] = part.strip().split()
        return calibrations
        
    def recursive_add(mathstr:str, n_idx:int=0, total:int=0):
        #Exit criteria
        if n_idx > len(mathstr):
            return total
        #Find all the operators        
        ops = [idx for idx, x in enumerate(mathstr) if not x.isnumeric()]
        #If string has two or more operators. 
        if len(ops) > 1:
            #Grab the operator id
            op_id = ops.pop(0)
            #subselect the evaluation string ie - up to next operator
            samp = mathstr[:ops[0]]
            #Grab the left aka, current sum 
            if total == 0:
                left = samp[:op_id] 
            else:
                left = str(total)
            #Grab the right
            right = samp[op_id+1:] #i think i need the next op id here.  
            #Do some weird fuckin math
            total = domath(int(left), int(right), samp[op_id])
            #select next operator index to start from
            n_idx = op_id

        #If string has only one operator left.  (the rightmost)
        elif len(ops) == 1:
            op_id = ops.pop()
            if total == 0:
                left = mathstr[:op_id]
            else:
                left = str(total)
            right = mathstr[op_id+1:]
            total = domath(int(left), int(right), mathstr[op_id])
            #Index the next operator forward
            n_idx += op_id 
            #Could be in my exit routine here.  might be skipping something
        
        return recursive_add(mathstr[n_idx+1:], n_idx, total)
    
    def domath(left:int, right:int, operator:str):
        if operator == "*":
            left *= right
        elif operator == "+":
            left += right
        elif operator == "|":
            left = int(str(left) + str(right))
        return left
        
    cals = parse_input(arr)    
    test_vals = 0
    if part == 2:
        operators = ["+", "*", "|"]
    else:
        operators = ["+", "*"]
    farts = [(len(str(x)),x) for x in cals.keys()]
    farts = sorted(farts, key=lambda x:x[0], reverse=True)
    # logger.warning(f"Longest key = {farts[0]}")
    longest = farts[0][0]
    for test_val, parts in cals.items():
        for possible in product(operators, repeat=len(parts)-1):
            equation = parts[0]
            for num, op in zip(parts[1:], possible):
                equation += op + num
            if part == 1:
                assert " ".join(parts) == equation.replace("*", " ").replace("+", " ")
            elif part == 2:
                assert " ".join(parts) == equation.replace("*", " ").replace("+", " ").replace("|", " ")
            wrong_math = recursive_add(equation)
            if np.int64(test_val) == wrong_math:
                logger.warning(f"Equation: {test_val:<{longest}}== {equation}")
                test_vals += np.int64(test_val)
                break

    return test_vals

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
    console.log(f"{tellstory}")
    # [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problemsolver(testdata, 2)
    #Assert testcase
    assert testcase == 11387, f"Test case B failed returned:{testcase}"
    # logger.info(f"Test case:{testcase} pass for part B")
    #Solve puzzle with full dataset
    answerB = problemsolver(data, 2)
    return answerB

def main():
    global data
    data = support.pull_inputdata(DAY, YEAR)

    #Solve part A
    resultA = part_A()
    fails = [8400518384267]
    if resultA in fails:
        logger.warning(f"Answer already submitted\nAnswer: {resultA}")
        exit()
    else:
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
# Ok.  Sooooo these damn elephants.  have been stealing mathematical operations in the elfs calibrations !  I KNOW RIGHT?
# We've got two lists of numbers.  One is the test calibration total.  The other is a list of numbers that could be added or multiplied together 
# to equal the test calibration total. 
# Our job..  is to find which of those calibrations are valid (aka total == eval of equation)
# First idea is to recursively split the string on its operators.  
# Passing test cases but first submission is too low.
# 
