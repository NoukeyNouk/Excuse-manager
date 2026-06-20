from agent_ai.agent_ai import AgentAI

def main():
    print("Здравствуйте!")
    print("Опишите вашу ситуацию (вы опоздали, что-то сломали, и т. п)")
    print("Если хотите увидеть Запрос-пример, просто нажмите Enter.")

    situation = input()
    if situation == '':
        situation = 'Я всю ночь играл в доту и не смог подготовиться к экзамену, но хочу получить пятёрку'

    print(f'Ваша ситуация: "{situation}"')

    agent = AgentAI()

    print(agent.generate_with_retry(situation))



if __name__ == "__main__":
    main()




