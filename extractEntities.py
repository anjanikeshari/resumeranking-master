# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 20:57:57 2018

@author: saurabh.keshari
"""
#python -m spacy download en_core_web_sm
#mport spacy
import re
#from collections import Counter
#import en_core_web_sm


#Function to extract names from the string using spacy
def extract_name(resume):
   
   # Load English tokenizer, tagger, parser, NER and word vectors
    nlp = en_core_web_sm.load()
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(resume)
    for ent in doc.ents:
        if(ent.label_ == 'PER'):
            print(ent.text)
            break 
    return ent.text                  

#Function to extract Phone Numbers from string using regular expressions
def extract_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    value = r.findall(string)
    values = [re.sub(r'\D', '', number) for number in value if len(number) >9]
    phoneNumbers = list(set(values))
    return phoneNumbers

#Function to extract Email address from a string using regular expressions
def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    print('printing the email values from function')
    values = list(r.findall(string))
    value = map(lambda x:x.lower(), values) 
    email_list = list(set(value))
    return email_list

def extract_names(tttt, resumeTitle):
    #noun_list = [w for (w, pos) in TextBlob(tttt).pos_tags if pos[0] == 'N']
    #noun_Sentence = " ".join(noun_list)
    TITLE = r"(?:[A-Z][a-z]*\.\s*)?"
    NAME1 = r"[A-Z][a-z]+,?\s+"
    MIDDLE_I = r"(?:[A-Z][a-z]*\.?\s*)?"
    NAME2 = r"[A-Z][a-z]+"
    name = []
    name = re.findall(TITLE + NAME1 + MIDDLE_I + NAME2, tttt)
    if len(name) > 0:
        rep1 = {"Career": "", "career": "", "Objective":"", "objective": "", "Email": "", "email": "", "Experience Summary": "", "ph": "", "Ph": "", "Professional": "", "Curriculum Vitae": "", "Resume": "", "Profile": "", "Professional": "", "Recruiter": "", "Lead": "", "Summary": "", "HR": "", "new":"", "New": ""}  # define desired replacements here
        rep = dict((re.escape(k), v) for k, v in rep1.items()) 
        #Python 3 renamed dict.iteritems to dict.items so use rep.items() for latest versions
        pattern = re.compile("|".join(rep.keys()))
        personName = pattern.sub(lambda m: rep[re.escape(m.group(0))], name[0])
        #sentence=name[0].replace('Email',"")
        if len(personName)==0:
                #a = 'saurabh+keshari_1234'
                titleSplit = re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]', resumeTitle)
                strr = " ".join(titleSplit)
                titleSplit = re.findall(r"[\w']+", strr)
                titleSplit_lower = to_lowercase(titleSplit)
                titleSplit_cleaned = remove_stopwords(titleSplit_lower)
                firstName = titleSplit_cleaned[0]
                secondName = titleSplit_cleaned[1]
                thirdName = titleSplit_cleaned[2]
                if not secondName.isdigit() and not firstName.isdigit():
                    personName = firstName +" " + secondName
                elif not firstName.isdigit() and (secondName.isdigit()):
                    personName = firstName
                elif (firstName.isdigit()) and not secondName.isdigit():
                    personName = secondName 
                else:
                    personName = thirdName
        
    else:
        #a = 'saurabh+keshari_1234'
        titleSplit = re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]', resumeTitle)
        strr = " ".join(titleSplit)
        titleSplit = re.findall(r"[\w']+", strr)
        titleSplit_lower = to_lowercase(titleSplit)
        titleSplit_cleaned = remove_stopwords(titleSplit_lower)
        firstName = titleSplit_cleaned[0]
        secondName = titleSplit_cleaned[1]
        thirdName = titleSplit_cleaned[2]
        if not secondName.isdigit() and not firstName.isdigit():
            personName = firstName +" " + secondName
        elif not firstName.isdigit() and (secondName.isdigit()):
            personName = firstName
        elif (firstName.isdigit()) and not secondName.isdigit():
            personName = secondName 
        else:
            personName = thirdName
    return re.sub(' +',' ',personName) # removes multiple spaces

"""

resume = open("resumeSample.txt", "r")
resume_txt = resume.read()
#print(resume_txt)
#print(programmingScore(pdftotextmaybe.convert("Sample resumes/sample1.pdf"), jd_txt) )
#print(extract_name(resume_txt) )
print("Phone numbers are ",extract_phone_numbers(resume_txt) )
print("Email id is ",extract_email_addresses(resume_txt) )


 Code to Read skills from any file 
skills = open("skillDB.txt", "r")
skills = skills.read()
print(skills)
listOfSkills = skills.split(",")
print(listOfSkills)

"""
