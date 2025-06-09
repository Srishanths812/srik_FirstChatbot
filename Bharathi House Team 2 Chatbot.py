from time import sleep as x
from datetime import datetime as ko
print("Bot: Namaste, I am Bharathi and I am your chatbot")
print("Bot: You can ask me anything about the school and i am here for you")
print("Bot: Enter 00 to stop our conversation")
while True:
    
    print("Bot: What would you want to know or do?")
    s=input("You : ")
    if s=="00":
        x(1)
        print("Bot : It was nice talking to you. Bye!!!")
        x(2)
        print('Exiting')
        x(0.2)
        print('.')
        x(0.2)
        print('.')
        x(0.2)
        print('.')
        x(0.4)
        break
    s=s.lower()
    s=s.split()      
    for i in s:
        print()
        if i=='namaste':
            print('Bot : Namaste to you too!!!')
        elif i=='good':
            if 'morning,' in s and 'morning' in s:
                print("Bot : Good morning to you too!!!")
            elif 'evening,' in s and 'evening' in s:
                print("Bot : Good evening to you too!!!")
            elif 'afternoon,' in s or 'afternoon' in s:
                print("Bot : Good Afternoon  to you too!!!")
        elif i=='christmas':
            print("Merry Christmas")
            break
        elif i=='new year':
            print("Happy New year")
        elif 'your' in s and 'age' in s:
            print("Just few minutes ago :)")
            break
        elif i=='fees' or i=='fee':
            print("Bot : Head to \'https://parent.neverskip.com/#/auth/login\' for fee payment")
            print("      click the link and login to student's Neverskip account to know more")
            break
        elif i=='admission' or i=='admissions' :
            print("Bot : admissions regarding LKG or higher classes")
            s1=input("You : ")
            s2=s1.lower()
            if 'higher' in s2:
                            print("Bot : Head to https://bgpm.davchennai.org/non-lkg-admissions/ to know more")
                            break
            elif 'lkg' in s2:
                    print("Bot : Head to https://bgpm.davchennai.org/LKG_admissions.html to know more")
                    break
        elif i=="history":
                    print("Bot : Our school has a very rich history. To talk about our school in a few lines is extremly oversimplified")
                    print("Bot : In short, our school was established in 1970 and has ever since been the most qualified school and competent school in our country")
                    break
        elif i=='time'or i=='date':          
            print("Bot : The time is",ko.now())
            break
        elif i=='publication' or i=='publications':
            print("Bot : We publish a lot of books. These include DEEPIKIA, Insight")
            print('Bot : Head to https://bgpm.davchennai.org/publications/ to know more')
            break
        elif i=='timings' or i=='timing':
            print("Bot : For primary classes it starts from 8:00 A.M to 2:00 P.M")
            print("Bot : For higher classes it is from 8:00 A.M to 2:40 P.M")
            break
        elif i=='ptm' or i=='parent teachers meeting' or i=='parent teacher meeting':
            print("Bot : For classes 1 to 8, it on 1st Satruday of every month")
            print("Bot : For classes 9 to 12, it on 3rd Satruday of every month")
            break
        elif i=='schol' or i=='shool' or i=='schoo' or i== 'scool' or i=='schooll':
            print("Bot : I think you meant 'school', please try again with correct spellings")
            break
        elif i=='admissin' or i=='admision' or i=='amission' or i=='admssion' or i=='admsion' or i=='admisions':
            print("Bot : I think you meant 'admission', please try again with correct spellings")
            break
        elif i=='timin' or i=='timngs' or i=='timngs' or i=='tmings':
            print("Bot : I think you meant 'timings', please try again with correct spellings")
            break
        elif i=='results' or i=='previous year score' or i=='previous year scores':
            print('Bot : Our results in class X and XII were excellent last year. Which class results do you want to know?')
            c=0
            while c<2:
                s1=input('You :')
                if 'x' in s1 or '10' in s1 or 'ten' in s1:
                    print('Bot : In the year 2021, our class X students had a 100% pass percentage')
                    print('         The highest score was 496')
                    print('         For more info head to \'https://bgpm.davchennai.org/results\'')
                    break
                elif 'xii' in s1 or '12' in s1 or 'twelve' in s1:
                    print('Bot : In the year 2021, our class XII students had a 100% pass percentage')
                    print('         The highest score in science stream was 497 ')
                    print('         The highest score in commerce stream was 492 ')
                    print('         For more info head to \'https://bgpm.davchennai.org/results\'')
                    break
                else :
                    print('Bot : Sorry I couldn\'t get you. Could you repeat that?')
                    c+=1
            break
        elif i=='coscholastic' or i=='extra curricular':
            print('Bot : Our students excelled in various coscholatic area. Do you want to know about sports or  other coscholatic areas?')
            c=0
            while c<2:
                s1=input('You :')
                if 'sport' in s1 or 'sports' in s1:
                    print('Bot : Head to \'https://bgpm.davchennai.org/achievements/sports/state/\'')
                    break
                elif 'other' in s1 or 'others' in s1:
                    print('Bot : Head to \'https://bgpm.davchennai.org/achievements/coscholastic/state/\'')
                    break
                else:
                    print('Bot : Sorry I couldn\' get you. Could you repeat that?')
                    c+=1
            break
        elif ('school' in s or 'institution' in s) and 'about' in s and 'admissions' not in s and 'admission' not in s and 'fees' not in s and 'fee' not in s and 'history' not in s and 'ptm' not in s and 'parent teachers meeting' not in s and 'parent teacher meeting' not in s:
            print('Bot : D.A.V Boys Senior Secondary School was started in 1970')
            print('         It is the oldest DAV school in Chennai')
            print('         It has created its own space in the education sector')
            print('         To know more head to \'https://bgpm.davchennai.org/about-us/\'')
            break
        elif i=='principal' or i=='pri':
            print('Bot : Mrs. Chitra Raghavan is the current principal')
            break
        elif i=='spl' :
            print('Bot : Rohith of XII-C is our current SPL in the year 2022-23')
            break
        elif i=='aspl' :
            print('Bot : Sriram of XI-A is our current ASPL in the year 2022-23')
            break
        elif i=='teaching' or i=='staff':
            print('Bot : Head to \'https://bgpm.davchennai.org/static/pdf/staff_list_2022-23.pdf\'')
            break
        elif i=='branches' or i=='branch':
            print('Bot : Owned schools : 8')
            print('Bot : Managed schools : 4')
            print('Bot : Academic associations : 11')
            print('Bot : Government aided schools : 2')
            break
        elif i=='integrated':
            print('Bot : Our school offers integrated programs for JEE and NEET coaching')
            print('         For more info contact the office : 044-28352866')
            break
        elif i=='office':
            print('Bot : email : boys.gpm@davchennai.org')
            print('         phone : 044-28352866')
            print('         phone : 044-28351370')
            break
        elif i=='hm' or i=='head master' or i=='head mistress':
            print("Bot : Mrs. Swarna Karpagavalli is our current head mistress")
            break
        elif i=='publction' or i=='publiations' or i=='publiation' or i=='publiaions' or i=='publition':
            print("Bot : I think you meant 'publications'")
            print("Bot : please try again with correct spellings")
        elif i=='thank' or i=='thank you':
            print("Bot : It was really nice talking to you")
            break
    
        
    else:
        print("Bot : The information you has asked is either not updated in my server or is unavailable")
        print("Bot : Please ask any other query")

            
            
                
                
        

