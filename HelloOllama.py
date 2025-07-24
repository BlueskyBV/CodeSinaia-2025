import ollama

# Specify the model name
model_name = "gemma3:1b"

# Define the prompt
prompt = "What is the capital of France?"

# # Send the prompt to the model and get the response
# response = ollama.generate(model=model_name, prompt=prompt)

# # Print the response
# print(type(response))
# print(response.response)

answer = ollama.chat(model=model_name, messages=[{'role': 'user', 'content': prompt}])
answer_text = answer['message']['content']
print(answer_text)