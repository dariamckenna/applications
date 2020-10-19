#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:37:21 2020

@author: EDSE-dariamck-workspace
"""

#Import the necessary libraries 	
import os
from email.parser import Parser

rootdir = "/home/EDSE-dariamck-workspace/Enron_dataset/maildir/lay-k/family"

def email_analyse(inputfile, to_email_list, from_email_list, email_body, email_date_list, email_subject_list):
    with open(inputfile, "r") as f:
        data = f.read()
        
    email = Parser().parsestr(data)
    if email['to'] not in to_email_list:
        to_email_list.append(email['to'])
    if email['from'] not in from_email_list: 
        from_email_list.append(email['from'])
    email_date_list.append(email['date'])
    email_subject_list.append(email['subject'])
    email_body.append(email.get_payload())
    
    
#empty lists to structure the data!!!
to_email_list = []
from_email_list = []
email_body = []
email_date_list = []
email_subject_list = []

'''
PART 1: Use Helper Function to move data from unstructured email form to 
structured form
'''

print ("moving data to new structures")
for directory, subdirectory, filenames in  os.walk(rootdir):
    for filename in filenames:
        #uses the root directory
        #see files
        email_analyse(os.path.join(directory, filename), to_email_list, from_email_list, email_body, email_date_list, email_subject_list)
  
print(email_date_list)        
'''
PART 2: Move newly structured data into files, in this case .txt
there are other types like pickle files, binaries, csvs etc
'''
'''
#Move "to_email_list
print ("saving to email list as text \n")
with open("to_email_list.txt", "w") as f:
    for to_email in to_email_list:
        if to_email: #if there is to email then write (avoids adding empty lines)
            f.write(to_email)
            f.write("\n")

#Moves from_email list
print ("saving from email list as text \n")
with open("from_email_list.txt", "w") as f:
    for from_email in from_email_list:
        if from_email: #if there is an from email then write (avoids adding empty lines)
            f.write(from_email)
            f.write("\n")        

#Moves email body
print ("saving email body as text \n")
with open("email_body.txt", "w") as f:
    for email_bod in email_body:
        if email_bod: #if there is an email body then write (avoids adding empty lines)
            f.write(email_bod)
            f.write("\n")  
    

#Let's look at the text files and see what we got
            
# Issues are in the lay-k/family folder, open up the file 4
    '''
    
    