from google import genai
from google.genai import types
from dotenv import load_dotenv
from time import sleep
import os
from agent_ai.prompts import SYSTEM_PROMPT

load_dotenv()

class AgentAI:
    def __init__(self, model: str ="gemini-2.5-flash"):
        self.model = model

    def generate_with_retry(self, prompt, max_retries=4):
        delay = 2
        for i in range(max_retries):
            try:
                client = genai.Client()


                response = client.models.generate_content(
                    model=self.model,
                    # system_instruction=SYSTEM_PROMPT,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT,
                    ),
                )
                answer = response.text
                if '### Пункт 3' in answer:
                    answer = answer[answer.find('### Пункт 3'):]
                    answer = answer[answer.find('\n') + 1:]
                return answer
                # for chunk in response:
                #     print(chunk.text, end="", flush=True)
            except genai.errors.ServerError as e:
                print("Server is full. retying!!")
                sleep(delay)
                delay *= 2
            except genai.errors.ClientError as e:
                if '429' in e:
                    print('Sorry, too many requests!')
                    break
        else:
            print("Server is very full, sorry!")

