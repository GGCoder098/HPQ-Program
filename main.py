from gpt_chat import GPT
from Ollama_chat import Ollama
from Gemini_chat import Gemini
from WriteToFile import Format
import subprocess
import sys
from datasets import load_dataset
from Check import check_code
import time

ds = load_dataset("mbpp", "sanitized", split="test")
tasks = []
tests = []
for problem in ds:
    tests.append(problem["test_list"])
    tasks.append(problem["prompt"])


final_results = []
len_largest_name = 0

def model_selector(selected_model):
    wins = 0
    temp_win = 0
    losses = 0
    temp_losses = 0
    code_errors = 0
    test_case_errors = 0
    final = ""

    print(f"Selected model: {selected_model}")
    try:
        if selected_model == "GPT":
            for i in range(len(tasks)):
                result = GPT(tasks[i], tests[i])
                result = Format(result)
                print(result,"\n")
                try:
                    for x in range(len(tests[i])):
                        final = subprocess.run([sys.executable, "-c", f"from Check import check_code; check_code({repr(result)}, {repr(tests[i][x])})"],capture_output=True, text=True, timeout=200).stdout
                        final = final.strip()
                        if final == "win":
                            temp_win += 1
                        elif final == "CodeError":
                            code_errors += 1
                            break
                        elif final == "TestCaseError":
                            test_case_errors += 1
                            break
                except:
                    pass
                if temp_win == len(tests[i]):
                    wins += 1
                    temp_win = 0
                else:
                    temp_win = 0
                    losses += 1
                print({"selected model": selected_model, "correct answers: ": wins, "incorrect answers": losses, "code errors": code_errors, "test case errors": test_case_errors})
            print({"selected model": selected_model, "correct answers: ": wins, "incorrect answers": losses, "code errors": code_errors, "test case errors": test_case_errors})
        elif selected_model == "Gemini":
            for i in range(len(tasks)):
                result = Gemini(tasks[i], tests[i])
                result = Format(result)
                print(result,"\n")
                try:
                    for x in range(len(tests[i])):
                        final = subprocess.run([sys.executable, "-c", f"from Check import check_code; check_code({repr(result)}, {repr(tests[i][x])})"],capture_output=True, text=True, timeout=200).stdout
                        final = final.strip()
                        if final == "win":
                            temp_win += 1
                        elif final == "CodeError":
                            code_errors += 1
                            break
                        elif final == "TestCaseError":
                            test_case_errors += 1
                            break
                except:
                    pass
                if temp_win == len(tests[i]):
                    wins += 1
                    temp_win = 0
                else:
                    temp_win = 0
                    losses += 1
                print({"selected model": selected_model, "correct answers: ": wins, "incorrect answers": losses, "code errors": code_errors, "test case errors": test_case_errors})
                time.sleep(10)
                print("slept for 10 seconds")
            print({"selected model": selected_model, "correct answers: ": wins, "incorrect answers": losses, "code errors": code_errors, "test case errors": test_case_errors})
        else:
            for i in range(len(tasks)):
                result = Ollama(selected_model, tasks[i], tests[i])
                # print(result, "\n", "\n")
                result = Format(result)
                print(result,"\n")
                try:
                    for x in range(len(tests[i])):
                        final = subprocess.run([sys.executable, "-c", f"from Check import check_code; check_code({repr(result)}, {repr(tests[i][x])})"],capture_output=True, text=True, timeout=200).stdout
                        final = final.strip()
                        if final == "win":
                            temp_win += 1
                        elif final == "CodeError":
                            code_errors += 1
                            break
                        elif final == "TestCaseError":
                            test_case_errors += 1
                            break
                except:
                    pass
                if temp_win == len(tests[i]):
                    wins += 1
                    temp_win = 0
                else:
                    temp_win = 0
                    losses += 1
                print({"selected model": selected_model, "correct answers: ": wins, "incorrect answers": losses, "code errors": code_errors, "test case errors": test_case_errors})
                #print("\n", tasks[i], "\n", tests[i])
            temp_win = 0
            with open('results.txt', 'a') as file:
                file.write(f"selected model: {selected_model},{" "*(len_largest_name-len(selected_model))} Dataset: MBPP, correct answers: {wins},{" " * (3-len(str(wins)))} incorrect answers: {losses},{" " * (3-len(str(losses)))} code errors: {code_errors},{" " * (3-len(str(code_errors)))} test case errors: {test_case_errors}\n")
                
            print({"selected model": selected_model, "correct answers: ": wins, "incorrect answers": losses, "code errors": code_errors, "test case errors": test_case_errors})
        print(f"Model {selected_model} completed successfully!")
    except Exception as e:
        print(f"Error while running model {selected_model}: {e}")
    with open('results.txt', 'a') as file:
        file.write(f"selected model: {selected_model},{" "*(len_largest_name-len(selected_model))} Dataset: MBPP, correct answers: {wins},{" " * (3-len(str(wins)))} incorrect answers: {losses},{" " * (3-len(str(losses)))} code errors: {code_errors},{" " * (3-len(str(code_errors)))} test case errors: {test_case_errors}\n")

private_models = ["GPT", "Gemini"]
open_models = ["codegeex4","codegemma","codellama:34b", "qwen2.5-coder:32b", "gemma2:27b","qwen2.5-coder:32b-instruct-q8_0"]
all_models = private_models + open_models


for model in all_models:
    if len(model) > len_largest_name:
        len_largest_name = len(model)
        
for model in all_models:
    model_selector(model)