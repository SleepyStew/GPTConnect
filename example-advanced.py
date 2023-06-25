# More will be added to this example soon

import os

from gptconnect import GPTConnect, GPTFunction, GPTFunctionHandler
import requests
import dotenv


dotenv.load_dotenv()

ai = GPTConnect(token=os.environ.get("TOKEN"), model="gpt-3.5-turbo-0613")


@GPTFunctionHandler()
def custom_function_handler(function, args):
    # Please make sure to update or remove this code when adding new functions
    if function.__name__ == "ping_hostname":
        return function(args)
    else:
        return "The function called is invalid. Please let the user know this operation failed."


@GPTFunction(
    group="general_commands",
    description="Ping a hostname",
    params={
        "type": "object",
        "properties": {
            "hostname": {
                "type": "string",
                "description": "The hostname to ping",
            },
        },
        "required": ["hostname"],
    },
)
def ping_hostname(args):
    print(f"Pinging hostname {args.get('hostname')}...")
    url = f"https://{args.get('hostname')}"
    try:
        response = requests.get(url)
        return f"Ping was successful. Response code was {response.status_code}."
    except requests.exceptions.ConnectionError:
        return f"The hostname {args.get('hostname')} could not be pinged."


print(ai.call(prompt="Ping the hostname github", function_group="general_commands"))

# Output:
# Pinging hostname github.com...
# {
#     'content': 'The hostname "github.com" was successfully pinged with a response code of 200.',
#     'function_called': 'ping_hostname'
# }