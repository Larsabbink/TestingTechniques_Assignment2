import os
import subprocess
import json
from dotenv import load_dotenv

def create_environment(url):
    command = f"npx newman run {url} --reporters json --reporter-json-export newman/report.json"
    result = subprocess.Popen(command.split(' '), shell=True, stdout=subprocess.PIPE)
    output, error = result.communicate()

    return error == None
    
def handle_json():
    users = []

    f = open('newman/report.json')

    data = json.load(f)

    requests = data['run']['executions']

    for request in requests:
        if request['item']['name'].split('_')[0] == "login":
            
            data = request['response']['stream']['data']
            json_object = json.loads(''.join(map(chr, data)))

            if "errcode" in json_object:
                print(json_object)
            else:
                users.append({'id': json_object['user_id'], 'access_token': json_object['access_token'] })

    f.close()

    return users

if __name__ == "__main__":
    load_dotenv()
    
    api_key = os.getenv("api_key")
    collection_id = "400db99a-9230-475e-b4d9-b6f46504d0bc"

    url = f"https://api.getpostman.com/collections/{collection_id}?apikey={api_key}"

    if(create_environment(url)):
        users = handle_json()
        print(users)
