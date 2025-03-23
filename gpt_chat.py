from openai import OpenAI
def GPT(task, tests):
    client = OpenAI()
    completion = client.chat.completions.create(
        model="o1-mini",
        messages=[
            {"role": "user", "content": '''You are an expert Python programmer, and here is your task: {} Your code should pass these tests\n{}\n keep the function names the same, do not make any case changes. return only python code in this format:
     ```python
     
      [CODE]
      
    ```
'''.format(task, tests)},
        ]
    )
    
    return completion.choices[0].message.content