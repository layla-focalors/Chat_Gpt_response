# import os
# import openai
# from key import openai_api

# openai.api_key = ""
# question = "지금은 몇 시야?"

# completion = openai.ChatCompletion.create(
#     model = "gpt-3.5-turbo",
#     message = [
#         {"role" : "user", "content": question}
#     ]
# )
# print(completion.choices[0].message.content)

# import openai

# # Load your API key from an environment variable or secret management service
# openai.api_key = 'my_API'

import openai
openai.api_key = ""
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages = [{"role":"user", "content": "hello?"}],
    max_tokens = 20
)
print(response.choices[0].message.content)
# def get_response(prompts: list, model = "gpt-3.5-turbo"):
#   responses = []

  
#   restart_sequence = "\n"

#   for item in prompts:

#       response = openai.Completion.create(
#       model=model,
#       messages=[{"role": "user", "content": prompts}],
#       temperature=0,
#       max_tokens=20,
#       top_p=1,
#       frequency_penalty=0,
#       presence_penalty=0
#     )

#       responses.append(response['choices'][0]['message']['content'])

#   return responses

# get_response(['버추얼 유튜버 순위를 알려줘'])