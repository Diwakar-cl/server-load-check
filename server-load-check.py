name = input("Enter your name:")

server_name = input("Enter your server name:").upper()
print(server_name)




try:
    server_load = float(input("Enter server total number of people:"))
except ValueError:
    print("Try again with a number.")
    exit()




print(server_load)
def check_server(server_name, server_load):
    if server_load <= 200:
        return("Low")
    elif server_load >= 1000:
        return("High")
    else:
        return("Balanced")


print(f"Hi {name}, Checking {server_load}")
answer =check_server(server_name, server_load)


print(f"{server_name}:", answer)

servers= [("WEB", 100),("FORM", 1500),("WEB -01", 1000)]
names = [server_name for server_name, server_load in servers]

if server_name in names:
    print(f"{server_name} is in the list")
else:
    print(f"{server_name} is not in the list")


for server_name, server_load in servers:
    print(server_name,">", check_server(server_name, server_load))
