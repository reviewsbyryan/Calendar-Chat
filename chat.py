import json
import openai
import database

messages = database.messages
functions = database.functions
available_functions = database.available_functions


def chat(inp):
    if inp:
        messages.append(
            {"role": "user", "content": inp},
        )
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            functions=functions,
        )

    response_message = completion["choices"][0]["message"]
    messages.append(response_message)

    while response_message.get("function_call"):

        function_name = response_message["function_call"]["name"]

        try:
            fuction_to_call = available_functions[function_name]
        except KeyError:
            raise Exception(f"Function {function_name} not found")
        
        function_args = json.loads(response_message["function_call"]["arguments"])
        run_function = fuction_to_call(**function_args)

        print(f"Function call: {function_name}({function_args})")

        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": run_function,
            }
        )

        second_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            functions=functions,
            function_call="auto",  # auto is default, but we'll be explicit
        )
        
        second_reply = second_completion["choices"][0]["message"]
        messages.append(second_reply)
        
        if second_reply.get("function_call"):
            response_message = second_reply
            continue
        else:
            second_reply = second_completion["choices"][0]["message"]["content"]

        print(f"ChatGPT: {second_reply}")
        return str(second_reply)
    else:
        return completion.choices[0].message.content