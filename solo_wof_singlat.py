"""
Author: Tanmay Singla, singlat@purdue.edu
Assignment: 12.1 - Solo wof
Date: 11/21/2021

Description:
    The program is a game of wheel of fortune combined with guessing the word and involves playing choosing options and guesssing. 

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

import random


def load_phrases(): #function for loafin phrase from text file

    list1x = open('phrases.txt','r') #opening file
    
    list1 = list1x.readlines()
    list2=[]
    
    for i in list1: #removing n
        list2.append(i.strip())   #appending list  
    
    random.shuffle(list2) #random
    list1x.close() #closing file
    return list2

def spin_the_wheel(): #funtion for getting a random number from amounts list
    listsp = [500,500,500,500,550,550,600,600,600,600,650,650,650,700,700,800,800,900,2500, "BANKRUPT", "BANKRUPT"] #making list
    return random.choice(listsp)

def vowel(total,listv): #function for vowel
    if total <275:
        print("You need at least $275 to buy a vowel.\n")
        return;
    else:
        vowel = input("Pick a vowel: ")
        while str(vowel).lower() not in listv: #converting list to str
                
            if len(vowel) != 1: #if construct
                print("Please enter exactly one character.")
            elif vowel.isdigit() == True: #if construct
                print(f"The character {vowel} is not a letter.")
            elif ((vowel.isalpha()) == False): #if construct
                print(f'The character {vowel} is not a letter.')
            elif ((vowel.isalpha()) == True and (vowel.lower() != "a" and vowel.lower() != "e" and vowel.lower() != "i" and vowel.lower() != "o" and vowel.lower() != "u" #if construct
)):
                 print("Consonants cannot be purchased.")

            else: #if construct
                print(f"The letter {vowel.upper()} has already been purchased.")
            vowel = input("Pick a vowel: ")
            
    return(vowel)

#def option3():
    
        
#def printing()

def main():
    listra1  = load_phrases()
    listc = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w', 'x','y','z'] #making list
    listv =['a','e','i','o','u'] #making list
    element = 0
    total = 0
    ctz = 0
    totalzz = 0
    listra2= [] #making list  
    listx2 = []   #making list
    right = 0
    print("Welcome to Solo Wheel of Fortune!\n")
    while element < 4:
          
        listra = listra1[element]
        x = 0
        
        if ctz == 0: #if construct
            listra2.clear()
            for i in listra: #removing n
                listra2.append(i.strip()) #appending list
                if listra2[x] == "": #if construct
                    listra2[x]= ' '
                x = x +1
       
        if ctz == 0: #if construct
            listx2.clear()
            for x in (listra2):        
                if x == ' ': #if construct
                    listx2.append(' ') #appending list
                elif x.isalpha() == True:#if construct
                    listx2.append('_') #appending list
                else: #if construct
                    listx2.append(x) #appending list
                
        str1 = ''    
       
       
        list2c = ''.join(str(i) for i in listc) #converting list to str
        list2v = ''.join(str(i) for i in listv) #converting list to str
        totalx1 = format(total, ',')     
        totalx2 = ("$"+str(totalx1))
        print(f":: Solo WoF :::::::::::::::::::::::::::::: Round {element+1} of 4 ::\n::{(str1.join(listx2)).center(54)}::\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n::   {list2v.upper()}   ::   {list2c.upper()}   ::{totalx2:>11} ::\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
        
        print("Menu:\n  1 - Spin the wheel.\n  2 - Buy a vowel.\n  3 - Solve the puzzle.\n  4 - Quit the game.\n")
        option = (input("Enter the number of your choice: ")) #user input
        while (option) != '1' and option != '2' and option != '3' and option != '4':
            print(f'"{option}" is an invalid choice.\n')
            print("Menu:\n  1 - Spin the wheel.\n  2 - Buy a vowel.\n  3 - Solve the puzzle.\n  4 - Quit the game.\n")
            option = (input("Enter the number of your choice: ")) #user input
            
        
        if int(option) == 1:            #if construct
                if not ((str1.join(listc)).strip()): #converting list to str
                    print("There are no more consonants to choose.\n")
            
                else: #if construct
                    ctz = 1
                    result = spin_the_wheel()
                    if result == "BANKRUPT": #if construct
                        print(f"The wheel landed on {result}.")
                        print(f'You lost ${total:,}!\n')
                        total = 0
                    else: #if construct
                        print(f"The wheel landed on ${result:,}.")
                        letter = input("Pick a consonant: ") #user input
                        
                       
                        while str(letter).lower() not in listc:
                            if letter.lower() == "a" or letter.lower() == "e" or letter.lower() == "i" or letter.lower() == "o" or letter.lower() == "u": #if construct
                                print("Vowels must be purchased.")
                            elif len(letter) != 1: #if construct
                                print("Please enter exactly one character.")
                            elif letter.isdigit() == True: #if construct
                                print(f"The character {letter} is not a letter.")
                            elif letter.isalpha() == False: #if construct
                                print(f"The character {letter} is not a letter.")
                                
                            else: #if construct
                                print(f"The letter {letter.upper()} has already been used.")
                            letter = input("Pick a consonant: ") #user input
                        if str(letter).lower() in listc: #if construct
                            listc[listc.index(letter.lower())] = " "
                            x = 0 
                            ct = 0
                            max1 = 0 
                           
                            for y in listra2:
                                if y.lower() == letter.lower():#if construct
                                    listx2[x] = letter.upper()
                                    ct = ct + 1 
                                x = x + 1
                            if ct == 0: #if construct
                                print(f"I'm sorry, there are no {letter.upper()}'s.\n")
                            elif ct ==1: #if construct
                                print(f"There is {ct} {letter.upper()}, which earns you ${result:,}.\n")
                                total = total + result

                                if result > max1: #if construct
                                    max1 = result
                            else: #if construct
                                print(f"There are {ct} {letter.upper()}'s, which earns you ${ct*result:,}.\n")
                                total = total + ct*result
                                if ct*result > max1: #if construct
                                    max1 = ct*result
                                    
                if not '_' in listx2:
                    print("Ladies and gentlmeen, we have a winner!")
                    print(f"You earned ${total} this round.\n")
                    element = element +1
                    listc = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w', 'x','y','z'] #making list
                    listv =['a','e','i','o','u'] #making list
                    right = right +1
                        
                
                    
                    
        elif int(option) ==2: #if construct
            if not ((str1.join(listv)).strip()): #converting list to str
                    print("There are no more vowels to buy.\n")
            else: #if construct
                ctz = 1
                
                letter1 = vowel(total,listv)
                if total >= 275: #if construct
                    total = total - 275
                
                if str(letter1).lower() in listv: #if construct
                    listv[listv.index(letter1.lower())] = " "
                if letter1 != None: #if construct
                    x = 0 
                    ct = 0
                    
                    for y in listra2:
                        if y.lower() == letter1.lower(): #if construct
                            listx2[x] = letter1.upper()
                            ct = ct + 1 
                        x = x + 1
                    if ct == 0: #if construct
                        print(f"I'm sorry, there are no {letter1.upper()}'s.\n")
                    elif ct ==1: #if construct
                        print(f"There is {ct} {letter1.upper()}.\n")
                        
                       
                    else: #if construct
                        print(f"There are {ct} {letter1.upper()}'s.\n")
                 
                if not '_' in listx2: #if construct
                    print("Ladies and gentlmeen, we have a winner!")
                    print(f"You earned ${total} this round.\n")
                    element = element +1
                    listc = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w', 'x','y','z'] #making list
                    listv =['a','e','i','o','u'] #making list
                    total = 0
                    right = right +1
                    
        
        elif int(option) ==3:
            
            listc = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w', 'x','y','z'] #making list
            listv =['a','e','i','o','u'] #making list
            print("Enter your solution.")
            print(f"  Clues: {str1.join(listx2)}") #converting list to str
            guess = input("  Guess: ")
            if guess.lower() == str(listra).lower(): #converting list to str
                ctz=0 #if construct
                print("Ladies and gentlemen, we have a winner!\n")
                element = element +1
                right = right +1
               
                
                if total > 1000: #if construct
                    print(f"You earned ${total:,} this round.\n")
                    
                        
                else: #if construct
                    print("You earned $1,000 this round.\n")
                    total = 1000
                totalzz = totalzz + total
                total = 0
                
                        
            else: #if construct
                print(f"I'm sorry. The correct solution was:\n{str(listra).upper()}")
                print("\nYou earned $0 this round.\n")
                element = element +1
                ctz=0
                total =0
                
               
           
        if int(option) ==4 or element == 4: #if construct
            if element != 4: #if construct
                print("\nYou earned $0 this round.\n")
                
            print("Thanks for playing!")
            if right == 0: #if construct
                print("You earned a total of $0.")
            elif right > 0: #if construct
                print(f"You earned a total of ${totalzz:,}.")
            element = 4
            return;
        
        
        
if __name__ == '__main__':
    main()
