from datetime import datetime
import os
import subprocess
from dotenv import load_dotenv

TESTS = ['Registration', 'Login', 
         'Send_message', 'Change_Password', 
         'Deactivate_Account', 'Event_closest_to_timestamp',
         'Reporting_Content', 'Presence',
         'Creating_Rooms', 'Banning/Deleting_users'
         ]

COLLECTION_IDS = {
    'create_environment':   "400db99a-9230-475e-b4d9-b6f46504d0bc",
    'tests':                "459a0db9-e32e-4753-9ba8-081be7e324fc"
}

# Load Postman API key from .env file
load_dotenv()
API_KEY = os.getenv("api_key")

def reset_database():
    os.system('docker exec -it synapse rm /data/homeserver.db')
    os.system('docker restart synapse')

def run_collection(collection_id, folder_name = None):
    url = f"https://api.getpostman.com/collections/{collection_id}?apikey={API_KEY}"

    command = f"npx newman run {url} --disable-unicode"
    if folder_name:
        command += f" --folder {folder_name}"
    
    result = subprocess.Popen(command.split(' '), shell=True, stdout=subprocess.PIPE)
    output, error = result.communicate()

    if output:
        return output
    else:
        return error

def run_tests():
    current_time = datetime.now()
    folder_name = current_time.strftime("%d-%m-%Y-%H-%M-%S")
    os.mkdir(f'./logs/{folder_name}')

    for test in TESTS:
        reset_database()
        
        output = run_collection(COLLECTION_IDS['create_environment'])
        with open(f'./logs/{folder_name}/env_{test}.txt', 'w') as file:
            file.write(output.decode('cp1252'))

        output = run_collection(COLLECTION_IDS['tests'], test)
        with open(f'./logs/{folder_name}/{test}.txt', 'w') as file:
            file.write(output.decode('utf-8'))

if __name__ == "__main__":
    run_tests()