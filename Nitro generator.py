import random
import string
import time
import colorama 
from colorama import Fore
colorama.init()

print (Fore.RED)

print("""
████████╗███████╗███╗   ███╗██████╗ ███████╗██╗   ██╗
╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔════╝╚██╗ ██╔╝
   ██║   █████╗  ██╔████╔██║██████╔╝█████╗   ╚████╔╝
   ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██╔══╝    ╚██╔╝
   ██║   ███████╗██║ ╚═╝ ██║██║     ██║        ██║
   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝        ╚═╝""")

print("\n")

num = int(input("How Many nitro Codes to Generate: "))

with open("Nitro Codes.txt", "w", encoding="utf-8") as file:
    print("\nYour nitro codes are being generated, be patient if you entered a high number!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

time.sleep(4.20)
