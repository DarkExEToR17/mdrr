import string as s
import secrets
import time

def menu():
	global onstart
	print(f"""





				 
█████╗  █████╗ ██████╗ ██╗  ██╗████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║  ██║███████║██████╔╝█████╔╝    ██║   ██║   ██║██║   ██║██║     
██║  ██║██╔══██║██╔══██╗██╔═██╗    ██║   ██║   ██║██║   ██║██║     
██████╔╝██║  ██║██║  ██║██║  ██╗   ██║   ╚██████╔╝╚██████╔╝███████╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
 
Disclaimer FOR EDUCTIONAL PURPOSE ONLY""")
time.sleep(5)

def generate_password(length: int, symbols: bool, uppercase: bool):
    combination = s.ascii_lowercase + s.digits

    if symbols:
        combination += s.punctuation

    if uppercase:
        combination += s.ascii_uppercase

    combination_length = len(combination)

    new_password = ""

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password


for _, index in enumerate(range(900)):
    password = generate_password(length=20, symbols=True, uppercase=True)
    print(index + 1, ">>", password)
