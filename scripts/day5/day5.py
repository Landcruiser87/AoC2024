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

def problemsolver(arr:list, part:int):
    def parse_input(arr:list):
        rules = {}
        splitidx = arr.index("")
        ruleset = arr[:splitidx]
        orders = arr[splitidx+1:]
        orders = [order.split(",") for order in orders]
        orders = [list(map(int, order)) for order in orders]
        for rule in ruleset:
            left, right = rule.split("|")
            left, right = int(left), int(right)
            if left in rules.keys():
                rules[left].append(right)
            else:
                rules[left] = [right]

        return rules, orders
    
    # def follow_rules():
    #     pass

    def in_order(rules:dict, orders:list):
        for idx, testloc in enumerate(orders):
            pagerules = rules.get(testloc)
            if pagerules:
                for rule in pagerules:
                    if rule in order:
                        if not idx < order.index(rule):
                            return False
        return True

    rules, orders = parse_input(arr)
    middles = []
    for order in orders:
        if in_order(rules, order):
            middles.append(order[len(order)//2])

    return sum(middles)


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
    assert testcase == 143, f"Test case A failed returned:{testcase}"
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
    assert testcase == 123, f"Test case B failed returned:{testcase}"
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
    _877_cache_now(".cache", False)
    
if __name__ == "__main__":
    main()

########################################################
#Notes
#Part A Notes
#Looks like we have some manual updates that are incorrectly printing 
#new pages must be printed in a  specific order.  
#the notation (our input) is in X|Y
#main rule
    #X must be printed at some point before Y
    
#Ok so this is tricky but i think doable with minimal libraries. 

# Rule 1
    #Our first input is a bunch of instructions that tell us 
    #if an update includes both page X and Y.  
    #Then X ust be printed before Y at some point
    #[x] - Collapse those into a dict of lists

# Rule 2
    #Rule 1 helps us establish the rules of order.  The second portion of the input
    #has the desired printed pages.  
    #Our job is to see which lines are in the correct order. 

# Rule 3 
    #Of the rulesets in part 2 that are in order.  Add up the middle numbers of each sequence. 
    #Must mean they're all odd lengthed?