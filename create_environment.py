import os
import subprocess
import json
from dotenv import load_dotenv

def create_environment(url):
    command = f"npx newman run {url}"
    result = subprocess.Popen(command.split(' '), shell=True, stdout=subprocess.PIPE)
    output, error = result.communicate()

    if output:
        print(output.decode('utf-8'))
    if error:
        print(error.decode('utf-8'))

if __name__ == "__main__":
    load_dotenv()
    
    api_key = os.getenv("api_key")
    collection_id = "400db99a-9230-475e-b4d9-b6f46504d0bc"

    url = f"https://api.getpostman.com/collections/{collection_id}?apikey={api_key}"

    create_environment(url)