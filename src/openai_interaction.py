import requests
import json
import logging
from config import API_KEY


def get_openai_response(prompt):
    try:
        api_url = 'https://pro.aiskt.com/v1/chat/completions'
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }
        payload = {
            'model': "gpt-4",
            'messages': [{"role": "user", "content": prompt}]
        }

        response = requests.post(api_url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            return f'Error: Received status code {response.status_code}'

    except Exception as e:
        logging.error(f"Error during API request: {e}")
        return 'An error occurred while processing the request'


# 测试调用
if __name__ == '__main__':
    prompt = "你好，红烧肉好不好吃？"
    response = get_openai_response(prompt)
    print(response)
