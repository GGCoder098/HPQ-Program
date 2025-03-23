from ollama import chat
from ollama import ChatResponse


def Ollama(model_name, task, tests):
    response: ChatResponse = chat(model=model_name, messages=[
    {"role": "system", "content": '''You are an expert Python programmer, and here is your task: {} Your code should pass these tests\n{}\n keep the function names the same, do not make any case changes. return only python code in this format:
     ```python
     
      [CODE]
      
    ```
'''.format(task, tests)}
    ])
    return response.message.content