import os
from groq import Groq
from dotenv import load_dotenv
from actions import get_response_time, get_seo_page_report

from prompts import system_prompt
from json_helpers import extract_json

# Load environment variables
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_text_with_conversation(messages, model = "llama3-8b-8192"):
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content



available_actions = {
    # "get_response_time": get_response_time
    "get_seo_page_report": get_seo_page_report
}

user_prompt = "Suggest some SEO optimization tips for google.com?"

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt},
]

turn_count = 1
max_turns = 5


while turn_count < max_turns:
    print (f"Loop: {turn_count}")
    print("----------------------")
    turn_count += 1

    response = generate_text_with_conversation(messages)

    print(response)

    json_function = extract_json(response)
    print(json_function, '<<<<<<<<<<')

    if json_function:
            function_name = json_function[0]['function_name']
            function_params = json_function[0]['function_params']
            if function_name not in available_actions:
                raise Exception(f"Unknown action: {function_name}: {function_params}")
                # action_function = available_actions[function_name]
                # result = action_function(**function_params)
                # function_result_message = f"Action_Response: {result}"
                # messages.append({"role": "user", "content": function_result_message})
                # print(function_result_message)
                # break
            print(f" -- running {function_name} {function_params}")
            action_function = available_actions[function_name]
            print(action_function, '+++++++++++', function_params)
            # call the function
            result = action_function(**function_params)
            function_result_message = f"Action_Response: {result}"
            messages.append({"role": "user", "content": function_result_message})
            print(function_result_message)
    else:
         break