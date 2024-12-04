import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.support import log_time, _877_cache_now, logger, console
from utils import support
from collections import deque
import time

#Set day/year global variables
DAY:int = 3 #datetime.now().day
YEAR:int = 2024 #datetime.now().year

def get_indexes(mainstr:str, searchterm:str):
    res = []
    idx  = mainstr.find(searchterm)
    while idx != -1:
        res.append(idx)
        idx = mainstr.find(searchterm, idx + 1)
    return res

def exe_mul(inst:str):
    s1, s2 = inst[4:-1].split(",")
    return (int(s1)*int(s2))

def is_valid(command:str, start:int, end:int):
    while True:
        #If the next char is a comma or isnumeric()
        if (command[end] == ",") | (command[end].isnumeric()):
            end += 1
        #If the next char is an end parenthesis AND it has a comma in it)
        elif (command[end] == ")") & ("," in command[start:end]):
            end += 1
            break
        else:
            break

    if command[start:end][-1] == ")":
        return end, True
    else:
        return end, False

def problemsolver(command:str, part:int):
    instructions = []
        #get rid of apostrophies and forward slashes for no fuckery
    for badactor in ["'", "/"]:
        command = command.replace(badactor, "")

    #Make a deque for all the indices of "mul(" we want to analyze
    indexes = deque(get_indexes(command, "mul("))
    if part == 2:
        #If its part 2 grab all the dos and dont indices
        do = get_indexes(command, "do()")
        dont = get_indexes(command, "dont()")

    while len(indexes) > 0:
        start = indexes.popleft()
        end = start + 4
        end, valid = is_valid(command, start, end)
        if valid:
            if part == 1:
                res = exe_mul(command[start:end])
                instructions.append(res)
            elif part == 2:
                # console.log(f"{command[start:end]}")
                if "dont()" in command[:end]:
                    dontfilt = list(filter(lambda x:x < end, dont))
                    dotest = "do()" in command[dontfilt[-1]:end]
                    if dotest:
                        dofilt = list(filter(lambda x:x < end, do))
                        dofind = command[dofilt[-1]:end]
                        # console.log(f"[white]{command[:dofilt[-1]]}[bold green]{dofind}[white]{command[end:]}")
                        res = exe_mul(command[start:end])
                        instructions.append(res)
                    # else:
                        # console.log(f"[white]{command[:dontfilt[-1]]}[bold red]{command[dontfilt[-1]:dontfilt[-1]+6]}[bold red]{command[dontfilt[-1]+6:end]}[white]{command[end:]}")
                else:
                    # console.log(f"[white]{command[:start]}[bold purple]{command[start:end]}[white]{command[end:]}")
                    res = exe_mul(command[start:end])
                    instructions.append(res)

    return sum(instructions)
        

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
    assert testcase == 161, "Test case A failed"
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
    assert testcase == 48, "Test case B failed"
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
    support.submit_answer(DAY, YEAR, 2, resultB)

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
#Not too bad today.  We've got computer instructions that are garbled and need some 
#help with decoding.  Our input is a giant string that has mul instructions 
#buried in them. Our task is to pull out those instructinos, multiply the values,
# and add them all up.
#
#Correct format
# 
#mul(X, Y)
#
#Part B notes
#Now we have two new conditionals! 
#If there is a "do()" command, execute the multiplication
#If there is a "don't" command, do not execute multiplication
#
#Well after fucking around for way too long.  i realized my input string was
#getting split on newlines that weren't supposed to be splits. Which would
#directly effect my ability to see which had do's or don'ts.  
#
#Lesson of today??
#CHECK YOUR INPUTS ANDY

