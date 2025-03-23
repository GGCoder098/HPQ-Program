

def Format(text):
    if text.find("```python") == -1 and text.find("```") == -1 and text.find("[PYTHON]") == -1 and text.find("[/PYTHON]") == -1 and text.find("### Solution Code") == -1 and text.find("### Explanation") == -1:
        return text
    if text.find("```python") != -1:
        text = text.replace("```python", "")
    if text.find("```") != -1:
        text = text.replace("```", "")
    if text.find("[PYTHON]") != -1:
        text = text.replace("[PYTHON]", "")
    if text.find("[/PYTHON]") != -1:
        text = text.replace("[/PYTHON]", "")
    if text.find("### Solution Code") != -1 and text.find("### Explanation") != -1:
        text = text[text.find("### Solution Code")+17:text.find("### Explanation")]
    lines = text.split('\n')
    filtered_lines = [line for line in lines if 'assert' not in line]
    result = '\n'.join(filtered_lines)
    return result