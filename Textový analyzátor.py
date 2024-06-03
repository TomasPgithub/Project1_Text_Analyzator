"""
projekt_1.py: první projekt do Engeto Online Python Akademie

autor: Tomáš Plechatý
email: tomplechaty@seznam.cz
discord: Gulas_D_Kom#9800
"""

from task_template import TEXTS

registred = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
# print(registred)

userName = input("username:")
heslo = input("password:")
verified = False

for user in registred:
    if user == userName and heslo == registred[user]:
        verified = True
        break
    
if verified:
    print(40*"-")
    print("Welcome to the app,", userName)
    print("We have", len(TEXTS),"texts to be analyzed.")
    print(40*"-")
    choice = input("Enter a number btw. 1 and 3 to select: ")
    
    print(40*"-")
    
    if not choice.isnumeric():
        print(f"Choice must be only number from 1 to 3")
    else:
        choice = int(choice)
        if not int(choice) in range(1,4):
            print("Invalid choice, terminejtink D program..")

    
        else:
            source = TEXTS[choice-1].replace(",", "")
            source = source.replace(".", "")
            word_counts = len(TEXTS[choice-1].split())
            title_case = 0
            upper_case = 0
            lower_case = 0
            numeric_strings = 0
            sum_of_all_numbers = 0
            dict_of_lenghts = {}
            max_len = 0

            for word in source.split():
                if len(word) > max_len:
                    max_len = len(word)
    
            for lenght in range(1,max_len+1):
                dict_of_lenghts[lenght] = 0
    
            for word in source.split():
                
                if  not word.isnumeric() and word == word.title():
                    title_case += 1
                if word.isalpha() and word.islower():
                    lower_case += 1
                if word.isalpha() and word.isupper():
                    upper_case += 1
                if word.isnumeric():
                    numeric_strings +=1
                    word_value = word
                    word_value = int(word_value)
                    sum_of_all_numbers +=word_value
        
                word_lenght = len(word)
                dict_of_lenghts[word_lenght] +=1
            max_value = 0
            for value in dict_of_lenghts:
                if dict_of_lenghts[value]>max_value:
                    max_value = dict_of_lenghts[value]
        
            print("There are",word_counts,"words in the selected text.")
            print("There are",title_case,"titlecase words." ) 
            print("There are",upper_case,"uppercase words." ) 
            print("There are",lower_case,"lowercase words." ) 
            print("There are", numeric_strings,"numeric strings.")
            print("The sum of all the numbers", sum_of_all_numbers)
            print(40*"-")
            print("LEN|  OCCURENCES  |NR.")
            print(40*"-")
            for lenght in dict_of_lenghts:
                if lenght < 10:
                    print(3*" ",lenght,"|",dict_of_lenghts[lenght]*"*",(max_value+2-dict_of_lenghts[lenght])*" ","|",dict_of_lenghts[lenght],sep="")
                if lenght > 9 and lenght < 100 :
                    print(2*" ",lenght,"|",dict_of_lenghts[lenght]*"*",(max_value+2-dict_of_lenghts[lenght])*" ","|",dict_of_lenghts[lenght],sep="")    

else:
    print("unregistered user, terminating the program..")
