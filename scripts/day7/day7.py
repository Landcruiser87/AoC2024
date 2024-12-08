import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, _877_cache_now, logger, console
from utils import support
from datetime import datetime
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
    
    def domath(left:str, right:str, operator:str):
        if operator == "*":
            return int(left) * int(right)
        elif operator == "+":
            return int(left) + int(right)
        
    def recursive_add(mathstr:str, n_idx:int=0, total:int=0):
        #Exit criteria
        if n_idx >= len(mathstr):
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
            if total != 0:
                left = str(total)
            else:
                left = samp[:op_id] 
            #Grab the right
            right = samp[op_id+1:] #i think i need the next op id here.  
            #Do some weird fuckin math
            total = domath(left, right, samp[op_id])
            #select next operator index to start from
            n_idx = op_id
        #If string has only one operator
        elif len(ops) == 1:
            op_id = ops.pop()
            if total != 0:
                left = str(total)
            else:
                left = mathstr[:op_id]
            right = mathstr[op_id+1:]
            total = domath(left, right, mathstr[op_id])
            #Boot it over the length limit.
            n_idx += len(mathstr)
        
        return recursive_add(mathstr[n_idx+1:], n_idx, total)
        
    cals = parse_input(arr)    
    test_vals = set()
    operators = ["+", "*"]
    longest = max([len(str(x)) for x in cals.keys()]) - 1
    for test_val, parts in cals.items():
        possibles = product(operators, repeat=len(parts))
        for possible in possibles:
            equation = parts[0]
            for num, op in zip(parts[1:], possible):
                equation += op + num
                # logger.warning(f"{equation}")
            wrong_math = recursive_add(equation)
            if test_val == wrong_math:
                logger.info(f"Equation: {test_val:<{longest}}=={equation}")
                test_vals.add(test_val)

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
    fails = [8400518384267]
    if resultA in fails:
        logger.warning(f"Answer already submitted\nAnswer: {resultA}")
        exit()
    else:
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
#
# Ok.  Sooooo these damn elephants.  have been stealing mathematical operations in the elfs calibrations !  I KNOW RIGHT?
# We've got two lists of numbers.  One is the test calibration total.  The other is a list of numbers that could be added or multiplied together 
# to equal the test calibration total. 
# Our job..  is to find which of those calibrations are valid (aka total == eval of equation)
# First idea is to recursively split the string on its operators.  
# Passing test cases but first submission is too low.
# 
#8400518384267 is too low