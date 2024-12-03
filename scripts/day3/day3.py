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
def get_indexes(mainstr:str, searchterm:str):
    res = []
    idx  = mainstr.find(searchterm)
    while idx != -1:
        res.append(idx)
        idx = mainstr.find(searchterm, idx + 1)
    return res

def execute_command(inst:str):
    s1, s2 = inst[4:-1].split(",")
    return (int(s1)*int(s2))

def problemsolver(arr:list, part:int):
    instructions = []
    for command in arr:
        indexes = deque(get_indexes(command, "mul("))
        if part == 2:
            # do = get_indexes(command, "do()")
            dont = get_indexes(command, "don't()")

        while len(indexes) > 0:
            start = indexes.popleft()
            end = 4
            while start+end <= len(command):
                #If the next char is a comma or isnumeric()
                if (command[start+end] == ",") | (command[start+end].isnumeric()):
                    end += 1
                #If the next char is an end parenthesis AND it has a comma in it)
                elif (command[start+end] == ")") & ("," in command[start:start+end]):
                    end += 1
                    if part == 2:
                        #If any don't is less than the start. Kick off eval to see if a do is located farther forward
                        if any(x < start for x in dont):
                            #Filter the list of don'ts
                            dontfilt = list(filter(lambda x:x < start, dont))
                            # If there is a "do()" inside the latest don't to current position.
                            # Execute multiplication, if not, break to next start index
                            if "do()" in command[dontfilt[-1]:start+end]:
                                # logger.info(f"{command[dontfilt[-1]:start+4+end]}")
                                res = execute_command(command[start:start+end])
                                instructions.append(res)
                                #If not break and continue to next start index
                        #? I think my any condition here is whats hosing me. 
                        #if there's any don'ts less than the start, Check 
                        #for a do in between
                        #else
                        #Add it anyway??? 
                        #somethings f'd up
                        else:
                            #Initial start condition.  If no don't beforehand, execute mul
                            res = execute_command(command[start:start+end])
                            instructions.append(res)
                    else:
                        res = execute_command(command[start:start+end])
                        instructions.append(res)
                    break
                    
                else:
                    # if the next char is not numeric or close parenthesis. break and continue to next index
                    break
    
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
#Too Low : 68964573
#Too high : 99812796