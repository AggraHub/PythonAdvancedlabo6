from enum import Enum
import sys 
from time import sleep
import json
from ping3 import ping

OPTIE1 = "server toevoegen"
OPTIE2 = "server verwijderen"
OPTIE3 = "server lijst"

def server_toevoegen():
    # Load the existing JSON data from a file
    with open('serverlijst.json', 'r') as file:
        data = json.load(file)

    # Prompt the user for server name and IP address
    server_name = input("Enter the server name: ")
    ip_address = input("Enter the IP address: ")

    # Create a new server information object
    new_server_info = {
        "server": server_name,
        "ip": ip_address
    }

    # Add the new server information to the existing data
    data.append(new_server_info)

    # Save the updated data back to the file
    with open('serverlijst.json', 'w') as file:
        json.dump(data, file, indent=4)

    i = input("type 'stop' om te stoppen of druk op enter om door te gaan: ")

def server_verwijderen():
    naam_server = input("geef de naam van de server die je wilt verwijderen: ")
    i = True
    while i != "stop":
        with open('serverlijst.json', 'r') as file:
            data = json.load(file)
        for server in data:
            if server["server"] == naam_server:
                data.remove(server)
            else:
                print("server niet gevonden")
        with open('serverlijst.json', 'w') as file:
            json.dump(data, file, indent=4)
        i = input("type 'stop' om te stoppen of druk op enter om door te gaan: ")

def server_lijst():
    with open('serverlijst.json', 'r') as file:
        data = json.load(file)
    for server in data:
        print(server["server"] + " " + server["ip"])

def ping(server) -> str:
    response = None
    with open('serverlijst.json', 'r') as file:
        data = json.load(file)
    for server in data:
        server_name = server["server"]
        if response == None:
           response = server_name + " is offline"
        else:
            response = server_name + " is online"

    return response

def update_json_with_ping_status():
    with open('serverlijst.json', 'r') as file:
        data = json.load(file)

    for server in data:
        server_name = server["server"]
        status = ping(server_name)
        server["status"] = status  # Add the 'status' key to each object

    # Save the updated data back to the file
    with open('serverlijst.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    




    
#Keuze = input("kies uit de volgende opties: \n 'server toevoegen','server verwijderen','server lijst' \n")
def main():

    configKeuze = input("kies uit 'modi' of 'checks': ")
    if configKeuze == "modi":
        if len(sys.argv) > 1:
            sys.argv[1] == OPTIE1 or sys.argv[1] == OPTIE2 or sys.argv[1] == OPTIE3
            Keuze = sys.argv[1]
            print(Keuze + " is een geldige optie")
            sleep(1)
        else:
            Keuze = input("kies uit de volgende opties: \n 'server toevoegen','server verwijderen','server lijst' \n")
        
        if Keuze == OPTIE1:
            server_toevoegen()
        elif Keuze == OPTIE2:
            server_verwijderen()
            print(Keuze)
        elif Keuze == OPTIE3:
            server_lijst()
        else:
            print("geen geldige optie")

    elif configKeuze == "checks":
        update_json_with_ping_status()
        print("ping status is geupdate")
if __name__ == "__main__":
    main()
