import socket

BLUE = "\033[1;34m"
RESET = "\033[0m"
print(f"{BLUE}by : Mubarak | Ig : l.s4y {RESET}")
print("                                         ")
website = input(f"{BLUE}Enter the website URL : {RESET}")
print("                                         ")
ip = socket.gethostbyname(website)


print(f"{BLUE}The IP address of {website} is : {ip}{RESET}")

print(f"{BLUE}IG : https://www.instagram.com/l.s4y {RESET}")