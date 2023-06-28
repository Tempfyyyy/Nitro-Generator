import requests
import random
import string
import time
import sys

def animate_cover():
    sys.stdout.write("""
████████╗███████╗███╗   ███╗██████╗ ███████╗██╗   ██╗
╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔════╝╚██╗ ██╔╝
   ██║   █████╗  ██╔████╔██║██████╔╝█████╗   ╚████╔╝
   ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██╔══╝    ╚██╔╝
   ██║   ███████╗██║ ╚═╝ ██║██║     ██║        ██║
   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝        ╚═╝
    """)
    sys.stdout.write("\n")
    sys.stdout.write("NitroGenerator")
    sys.stdout.write("\n")
    sys.stdout.write("Loading")
    start_time = time.time()
    stop_time = start_time + random.uniform(5, 10)

    while time.time() < stop_time:
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.5)
        sys.stdout.write("\b \b" * 3)
        sys.stdout.flush()
        time.sleep(0.5)

    sys.stdout.write("\r")
    sys.stdout.write(" " * 13)
    sys.stdout.write("\r")
    sys.stdout.flush()
    time.sleep(1.5)  # 1.5 seconds pause

animate_cover()

num = int(input('How Many nitro Codes to Generate: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated, be patient if you entered a high number!")

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

input("Press Enter to close the menu")