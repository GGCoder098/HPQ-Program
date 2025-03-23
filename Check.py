import math
from math import *

def check_code(gen_code, test_case):
    namespace = {}
    try:
        exec(gen_code, namespace)
    except Exception as e:
        print("CodeError")
        return
    try:
        exec(test_case, namespace)
    except AssertionError:
        print("loss")
        return
        
    except Exception as e:
        # print(f"Error in test case execution: {e}")
        # print("\n", test_case)
        print("TestCaseError")
        print(e)
        return
               
    print("win")