#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#RUN THIS CODE TO CREATE THE INDIVIDUAL TEXT_FILES FOR COMPENDIUM DOC.  IE MAKING JUDGEMENTS FOLDER

#NOTE : THE CODE ONLY WORKS IF THE COMPENDIUM STARTS WITH EQUIVALENT CITATION

import linecache
#import difflib
from thefuzz import fuzz
import pandas as pd
import re
regex = re.compile('[^a-zA-Z]')

def str_sim(str1, str2):
    
    a,b = regex.sub('',str1.lower()), regex.sub('',str2.lower())
    
    score = fuzz.ratio(a,b)
    return score

#Here paste the path of Compendiums
with open(r"C:\Users\Siddharth\Downloads\COMPENDIUM- Karnataka HC Judgements.doc.txt","r",encoding="utf8") as f:
    
    text = f.read()
    
    f_text=text.replace("Equivalent", "=-Equivalent")

    split_text=f_text.split("=-")

    del split_text[0]
    x=1
    j=0
    Comp=[]
    #strr=""
    for i in split_text:
        name=i.split("\n\n\n,E"  or "\n\n,E" or "\n,E" or "\n\n\n\n,E")
        with open(F"./a/{x}.txt","a+") as f:
            f.write(i)
            

        with open(F"./a/{x}.txt", 'r') as f:
            stre=" "
            for l_no, line in enumerate(f):
                if 'Appellants' in line:
                    stre = line+"VS "
                if 'Respondent' in line:
                    stre+= line
                    break

            s=stre
            new_string = stre.replace("\n", " " )
            stre = new_string.replace("Appellants: ", "" )
            new_string = stre.replace("Respondent: ", "" )
            stre = new_string.replace("@", "" )
            new_string=stre.lower()
            stre = new_string.replace(".", "" )

            new_string = stre.replace("/", "" )

            stre = new_string.replace("  ", " " )
            new_string = stre.replace(",", "" )
            
            print(new_string)
            Comp.append(new_string)
            
            x=x+1
            
    print("\n\n\n\n")
    
    #here paste the path of case table with the column name as [CASE NAME] and in that include only the names that that present in the case table of that particular file.
    ndf= pd.read_csv(r"C:\Users\Siddharth\OneDrive\Desktop\DATA STRUCTURES PROGRAMS\Judgements\one.csv")
    c=0
    li=[]
    n=0
    avail=[]
    name=[]
    for val,s1 in enumerate(Comp):
        name.append(s1)

        temp=""
        maxi=0
        mid=0
        
        for ver, st in enumerate(ndf["CASE NAME"]):

            st=str(st)
            s1=str(s1)
           
            ll=str_sim(st,s1)
            
            if ll>70:
                
                if(ll>maxi):
                    temp=st
                    maxi=ll
                    mid=ver
        if(temp==""):
            avail.append("NA")
        else:
            avail.append("A")
            c+=1

        t1=temp.replace("@","")
        temp=t1
        t2=temp.replace("/","")
        temp=t2
        t3=temp.replace(":","")
        temp=t3
        
        print(temp)
        print(maxi)
        print(s1)
        print("\n\n")
        li.append(temp)

        
    #print(avail)
    #print(name)

    data={"CASE NAME": name,"AVAILABLE":avail}

    df=pd.DataFrame(data)

    print(df)

    cssvv=df.to_csv('Availability Table.csv',index=True)
    print("No of available is :",c)

y=0
for j in split_text:
    name=j.split("\n\n\n,E"  or "\n\n,E" or "\n,E" or "\n\n\n\n,E")
    with open(F"./Judgements/{li[y]}.txt","a+") as f:
        f.write(j)
        y+=1

#intially adjust the path with Compendium and case table kas mentioned above 
#So basically we are supposed to do judgements list and availability table

# 1.  For the Judgements list run the above code  
#  - Where your Python path is there pls create a folder name (a) and (judgements) after each time you run the code pls delete the (a) folder contents and judgements contents.
#  - In the judgements you have the actual splitted text or Individual Text files with appellent name in .txt format 

###############################################################################################################################

# 2.  For the avialability table run this Code
#    - Run below code after running the code for Individual text files (judgements)
#    - Dont forgot to delete the folder contents of (a) and (judgements)
#    - Here in the below I reversed the Comp and ndf["CASE NAME"] in the two for loops part.
import linecache
#import difflib
from thefuzz import fuzz
import pandas as pd
import re
regex = re.compile('[^a-zA-Z]')

def str_sim(str1, str2):
    
    a,b = regex.sub('',str1.lower()), regex.sub('',str2.lower())
    
    score = fuzz.ratio(a,b)
    return score

#Here paste the path of Compendiums
with open(r"C:\Users\Siddharth\Downloads\COMPENDIUM- Karnataka HC Judgements.doc.txt","r",encoding="utf8") as f:
    
    text = f.read()
    
    f_text=text.replace("Equivalent", "=-Equivalent")

    split_text=f_text.split("=-")

    del split_text[0]
    x=1
    j=0
    Comp=[]
    #strr=""
    for i in split_text:
        name=i.split("\n\n\n,E"  or "\n\n,E" or "\n,E" or "\n\n\n\n,E")
        with open(F"./a/{x}.txt","a+") as f:
            f.write(i)
            

        with open(F"./a/{x}.txt", 'r') as f:
            stre=" "
            for l_no, line in enumerate(f):
                if 'Appellants' in line:
                    stre = line+"VS "
                if 'Respondent' in line:
                    stre+= line
                    break

            s=stre
            new_string = stre.replace("\n", " " )
            stre = new_string.replace("Appellants: ", "" )
            new_string = stre.replace("Respondent: ", "" )
            stre = new_string.replace("@", "" )
            new_string=stre.lower()
            stre = new_string.replace(".", "" )

            new_string = stre.replace("/", "" )

            stre = new_string.replace("  ", " " )
            new_string = stre.replace(",", "" )
            
            print(new_string)
            Comp.append(new_string)
            
            x=x+1
            
    print("\n\n\n\n")
    
    #here paste the path of case table with the column name as [CASE NAME] and in that include only the names that that present in the case table of that particular file.
    ndf= pd.read_csv(r"C:\Users\Siddharth\OneDrive\Desktop\DATA STRUCTURES PROGRAMS\Judgements\one.csv")
    c=0
    li=[]
    n=0
    avail=[]
    name=[]
    for val,s1 in enumerate(ndf["CASE NAME"]):
        name.append(s1)

        temp=""
        maxi=0
        mid=0
        
        for ver, st in enumerate(Comp):

            st=str(st)
            s1=str(s1)
           
            ll=str_sim(st,s1)
            
            if ll>70:
                
                if(ll>maxi):
                    temp=st
                    maxi=ll
                    mid=ver
        if(temp==""):
            avail.append("NA")
        else:
            avail.append("A")
            c+=1

        t1=temp.replace("@","")
        temp=t1
        t2=temp.replace("/","")
        temp=t2
        t3=temp.replace(":","")
        temp=t3
        
        print(temp)
        print(maxi)
        print(s1)
        print("\n\n")
        li.append(temp)

        
    #print(avail)
    #print(name)

    data={"CASE NAME": name,"AVAILABLE":avail}

    df=pd.DataFrame(data)

    print(df)

    cssvv=df.to_csv('Availability Table.csv',index=True)
    print("No of available is :",c)

y=0
for j in split_text:
    name=j.split("\n\n\n,E"  or "\n\n,E" or "\n,E" or "\n\n\n\n,E")
    with open(F"./Judgements/{li[y]}.txt","a+") as f:
        f.write(j)
        y+=1



