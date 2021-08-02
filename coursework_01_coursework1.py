from difflib import SequenceMatcher as sq
import time, os
import linecache as lc

global count
count=0

def spellChecker(sentence):

    start = time.time()

    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for ele in sentence:
        if ele in punc:
            sentence=sentence.replace(ele, " ")
    sentence = ''.join([i for i in sentence if not i.isdigit()])
    sentence = sentence.lower()
    words = sentence.split() #Remove numbers & punctuations from sentences and put in a list

    file=open("EnglishWords.txt")

    eng =[]
    for i in file:
        eng.append(i.strip()) #Push the words in the dictionary into a list

    correct_words=0
    incorrect_words=0
    dict_words=0
    changed_words=0

    new_sentence=[]


    for a in words: #Loop through the words in the sentence and compare them with the dictionary
        print(">> " + "Word: " + a)
        if a in eng:
            print(">> The word has been spelt correctly. Very nice!")
            new_sentence.append(a)
            correct_words+=1
            print("***********************************************************************")
            time.sleep(2)
        else:
            print(">> This word seems to be incorrect.")
            incorrect_menu = ["Ignore the word.", "Include question-mark in the beginning and end of the sentence.", "Add word to dictionary.", "Request suggestions."]
            b=0
            while (b<len(incorrect_menu)):
                print(">> " + str(b+1) + ". " + incorrect_menu[b])
                b+=1

            choice=int(input(">> Please click one of the options (1, 2, 3, 4): "))

            if (choice==1):
                print(">> This word has been marked incorrect.")
                new_sentence.append(a)
                incorrect_words+=1
                print("***********************************************************************")

            elif(choice==2):
                a=''.join(('?', a, '?'))
                print("The word now is: " + a)
                print(">> This word has been marked incorrect.")
                new_sentence.append(a)
                incorrect_words+=1
                print("***********************************************************************")

            elif(choice==3):
                eng.append(a)

                print(">> This word has been added to the dictionary. Great success!")
                print("***********************************************************************")
                new_sentence.append(a)
                dict_words+=1
                correct_words+=1

            elif(choice==4):
                suggest=[]
                for j in eng:
                    score = sq(None, a, j).ratio() #Loop through the dictionary and provide those words as suggestions whose ratio is >=0.6
                    if score>=0.6:
                        suggest.append(j)
                        print(">> Suggestions for you: " + str(suggest))

                        print(">> 1. Accept one of these suggestions.")
                        print(">> 2. Reject suggestions.")

                        anotherchoice=int(input("Choose the following options: "))
                        if (anotherchoice==1):
                            suggested_word=input(">> Type the word you'd like to choose: ")
                            print(">> The word has been changed! Great success.")
                            correct_words+=1
                            changed_words+=1
                            new_sentence.append(suggested_word)
                            print("***********************************************************************")
                            break

                        if (anotherchoice==2):
                            suggestion=input((">> Do you want to continue running through the dictionary?(y/Y or n/N): "))
                            if (suggestion=="n") or (suggestion=="N"):
                                print(">> This word has been marked incorrect.")
                                new_sentence.append(a)
                                incorrect_words+=1
                                break
                            print("***********************************************************************")


    stop = time.time()
    time.sleep(2)

    timetaken = stop-start
    timetaken = round(timetaken,1)



    print(">> Summary of this spell-check: ")
    time.sleep(1)
    print("***********************************************************************")
    print(">> Total number of words: " + str(len(words)), ">> Number of words spelt correctly: " + str(correct_words), ">> Number of words spelt incorrectly: " + str(incorrect_words), ">> Number of words added to dictionary: " + str(dict_words), ">> Number of words changed by the user accepting the suggested word: " + str(changed_words), sep="\n")
    print(">> Day, Date and Time of Spell-Check: " + time.asctime(), ">> Time taken to check spellings: " + str(timetaken) + " seconds", sep="\n")

    time.sleep(1)
    print("***********************************************************************")
    new_filename = input(">> Type the name of the file where you'd like to store this information: ")
    str1 = ""
    str1 = " ".join(new_sentence)


    f = open(new_filename,"a") #Opening a new file to store all the information

    f.write("Summary of this spell-check: ")

    f.write("\nTotal number of words: " + str(len(words)))

    f.write("\nNumber of words spelt correctly: " + str(correct_words))

    f.write("\nNumber of words spelt incorrectly: " + str(incorrect_words))

    f.write("\nNumber of words added to dictionary: " + str(dict_words))

    f.write("\nNumber of words changed by the user accepting the suggested word: " + str(changed_words))

    f.write("\nDay, Date and Time of Spell-Check: " + time.asctime())

    f.write("\nTime taken to check input: " + str(timetaken))

    f.write("\n"+ "Corrected sentence: " + str1)

    f.close()




print("Loading..")
time.sleep(2)
mainmenu=["Quit the program.", "Spell-check a sentence.", "Spell-check a file."]
print("***********************************************************************")
print(">> Welcome to the Spell-Checker!")
print("***********************************************************************")
time.sleep(1)



while (count == 0): #Loop through this menu as long as the user wants to use the program
    i=0
    while (i<len(mainmenu)):
        print(">> " + str(i) + ". " + mainmenu[i])
        i+=1

    option=int(input(">> Please click one of the following options (0, 1 or 2): "))
    print("***********************************************************************")



    if (option==1):
        sentence=input(">> Enter the sentence you'd like to check: ")
        print("***********************************************************************")
        spellChecker(sentence);
        continueprogram = input((">> Thanks for using the program! Would you like to continue?(y/Y or n/N): "))
        if (continueprogram=="n") or (continueprogram=="N"):
            count+=1


    elif (option==2):
        f=0
        while(f==0):
            name=input(">> Enter the name of the file you want to check with proper extension: ")
            try:
                file = open(name, 'r')
                print("File Opened!")
                f+=1
            except:
                print("The file doesn't exist in directory or has incorrect extension.")

        sentence=file.read()
        spellChecker(sentence);
        print("***********************************************************************")
        continueprogram = input((">> Thanks for using the program! Would you like to continue?(y/Y or n/N): "))
        if (continueprogram=="n") or (continueprogram=="N"):
            count+=1

    elif(option==0):
        print("***********************************************************************")
        print(">> Thanks for using the program!")
        exit()
        count+=1
    else:
        print(">> Invalid choice! You will now be taken back to the main menu.")
