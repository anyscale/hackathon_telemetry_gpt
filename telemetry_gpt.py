import os
import requests
import re
import time

s = requests.Session()

api_base = os.getenv("ANYSCALE_API_BASE")
token = os.getenv("ANYSCALE_API_KEY")
url = f"{api_base}/chat/completions"

file = open('system_prompt.txt', 'r')
system_prompt = file.read()
# Example: Write a query that count the number of records using ray version > 2.6.0
user_prompt = input("What is your prompt for ray telemetry data? (Example: Write a query that count the number of records using ray version > 2.6.0) ")

body = {
  "model": "meta-llama/Llama-2-70b-chat-hf",
  "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
  "temperature": 0.7
}

start_time = time.time()
with s.post(url, headers={"Authorization": f"Bearer {token}"}, json=body) as resp:
    data = resp.json()
    response = data['choices'][0]['message']['content']
    usage = data['usage']
    print("\nResponse:")
    try:
        sql_code = re.search(r'```(.*?)```', response, re.DOTALL).group(1).strip()
        print(sql_code)
    except:
        print(response)

end_time = time.time()
execution_time = end_time - start_time

print("\nMetrics:")
print(f"Execution time: {execution_time} seconds")
print(f"Prompt tokens: {usage['prompt_tokens']}")
print(f"Completion tokens: {usage['completion_tokens']}")
print(f"Total tokens: {usage['total_tokens']}")


