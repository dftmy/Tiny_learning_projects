import random
import time


lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(f"type in the following text: {lorem}")
start_time = time.time()
input_phrase = input()
end_time = time.time()
elapsed_time = end_time - start_time
count = 0
for i,c in enumerate(lorem): #создает итерируемый объект, где отдельно указывает индексы составных частей ==> далее по индексу идёт сравнение символов в образце и введеном тексте
    try:
        if input_phrase[i] == c:
            count += 1
    except:
         pass

accuracy = round(count/len(lorem)*100, 0)
print(f"Your accuracy is {accuracy}%")
print(f"You spent {round(elapsed_time, 0)} seconds")
