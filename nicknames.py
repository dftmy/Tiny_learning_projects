import random
import os
syllables = ["ar", "gar", "har", "dor", "var", "si", "ki", "la", "bla", "ae", "pi", "kok", "va", "sa", "re", "ri", "ra", "ka", "fo", "as", "sas"]

clear = lambda : os.system('cls')
new_cycle = 'y'

while new_cycle == "y":
    clear()
    number = random.randint(2,5)
    syl_list = random.choices(syllables, k= number)
    nickname = "".join(syl_list)
    print(f"Your new nickname is: {nickname}")
    new_cycle = input("Wanna go again y/n?: ")




