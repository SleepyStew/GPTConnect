import os

from gptconnect import GPTConnect, GPTFunction
import requests
import dotenv

dotenv.load_dotenv()

ai = GPTConnect(token=os.environ.get("TOKEN"), model="gpt-3.5-turbo-0613")


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
def ping_hostname(args: dict) -> str:
    print(f"Pinging hostname {args.get('hostname')}...")
    url = f"https://{args.get('hostname')}"
    response = requests.get(url)
    return f"Response code: {response.status_code}"


print(ai.call(prompt="Ping the hostname github.com", function_group="general_commands"))

# Output:
# Pinging hostname github.com...
# {
#     'content': 'The hostname "github.com" was successfully pinged with a response code of 200.',
#     'function_called': 'ping_hostname'
# }
