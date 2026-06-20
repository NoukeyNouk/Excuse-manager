from google import genai
from google.genai import types
from dotenv import load_dotenv
from time import sleep
import os
from prompts import SYSTEM_PROMPT

load_dotenv()

def generate_with_retry(prompt, max_retries=4):
    delay = 2
    for i in range(max_retries):
        try:
            client = genai.Client()


            response = client.models.generate_content(
                model="gemini-2.5-flash",
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
            print(answer)
            # for chunk in response:
            #     print(chunk.text, end="", flush=True)
            break
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


def main():
    print("Здравствуйте!")
    print("Опишите вашу ситуацию (вы опоздали, что-то сломали, и т. п)")
    print("Если хотите увидеть Запрос-пример, просто нажмите Enter.")

    situation = input()
    if situation == '':
        situation = 'Я всю ночь играл в доту и не смог подготовиться к экзамену, но хочу получить пятёрку'

    print(f'Ваша ситуация: "{situation}"')


    generate_with_retry(situation)



if __name__ == "__main__":
    main()




