
import requests
import random
import string
import time

print("""
___.                             __                                         .___                
\_ |__  _______  __ __   ____  _/  |_     ____    ____  _______ _____     __| _/  ____  _______ 
 | __ \ \_  __ \|  |  \ /    \ \   __\   / ___\ _/ __ \ \_  __ \\__  \   / __ |  /  _ \ \_  __ \
 | \_\ \ |  | \/|  |  /|   |  \ |  |    / /_/  >\  ___/  |  | \/ / __ \_/ /_/ | (  <_> ) |  | \/
 |___  / |__|   |____/ |___|  / |__|    \___  /  \___  > |__|   (____  /\____ |  \____/  |__|   
     \/                     \/         /_____/       \/              \/      \/                 """)
time.sleep(2)
print("Gerando links Nitro")
time.sleep(0.3)
print("Join https://discord.gg/dbwDBJBt6d")
time.sleep(0.2)

num = int(input('Insira quantos códigos gerar e verificar: '))

with open("Códigos Nitro", "w", encoding='utf-8') as file:
    print("Seus códigos nitro estão sendo gerados, seja paciente se você inseriu o número alto!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Gerado {num} códigos | Tempo gasto: {time.time() - start}\n")

with open("Códigos Nitro.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valid | {nitro} ")
            break
        else:
            print(f" Invalid | {nitro} ")

input("\nVocê gerou, agora pressione Enter para fechar, você obterá códigos válidos em Valid Codes.txt se vir que está vazio, então você não teve sorte, gere 20 milhões de códigos para a sorte ou então.")
