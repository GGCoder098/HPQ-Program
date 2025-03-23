import vertexai

from vertexai.generative_models import GenerativeModel

def Gemini(task, tests):
    PROJECT_ID = "hpq-api"
    vertexai.init(project=PROJECT_ID, location="us-central1")

    model = GenerativeModel("gemini-2.0-flash-001")

    response = model.generate_content(['''You are an expert Python programmer, and here is your task: {} Your code should pass these tests\n{}\n keep the function names the same, do not make any case changes, do not add explanations or your own tests. return only python code in this format:
     ```python
     
      [CODE]
      
    ```
'''.format(task, tests)])
    # print(response.text)
    return (response.text)

