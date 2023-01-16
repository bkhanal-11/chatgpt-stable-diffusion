import requests

with open("chatGPT-API.txt", "r") as file: # file containing openai api key
    api_key = file.read()
    authorization  = f"Bearer {api_key}"

def chatGPT(text):
  url = "https://api.openai.com/v1/completions"
  headers = {
  "Content-Type": "application/json",
  "Authorization": authorization,
  }
  data = { 
  "model": "text-davinci-003",
  "prompt": text,
  "max_tokens": 4000,
  "temperature": 1.0,
  }
  response = requests.post(url, headers=headers, json=data)
  output = response.json()['choices'][0]['text']
  
  return output

if __name__ == "__main__":
    # prints ChatGPT's response to "Tell a joke."
    query = "Tell a joke."
    response = chatGPT(query)

    print(f'Query: {query} \n')
    print(response)