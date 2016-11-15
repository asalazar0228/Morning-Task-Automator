import slickdealsparse
import voicerec_helper
import file_helpers
import text_twilio
import voicerec_helper
import email_helpers
import requests
import datetime
import os


##  PROVIDE TIME AND GREETING


##begin by telling user good morning and provide time
print "Hello Good Morning!\n"
os.system("say 'Hello Good Morning!' ")
os.system("say 'Would you like a to search through the current slickdeals?' ")

##get the date and time, format it, and print it to console
date = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
print "The current date and time is " + date +"\n"



## SLICKDEALS PORTION


##take audio from google search recognition
audio_slickdeals = voicerec_helper.rec_audio_response('Would you like a to search through the current slickdeals?')

##if audio finds that the answer is yes then it will proceed to slickdeals parsing
if(audio_slickdeals == "yes"):
    slickdealsparse.grab_slickdeals_information()

elif(audio_slickdeals == "no"):
    print "Alright no problem sounds good :)"

else:
    os.system("say 'Sorry I didn't quite catch that if you would like this task pls restart program' ")





## FILE OPERATIONS: TEXT TO PHONE OT OPEN IN CONSOLE


os.system("say 'Would you like me to open your open notes file, text notes file, or none? ' ")

##text_question = raw_input("Would you like me to open your open notes file, text notes file, or none? Type in")

audio_notes_question = voicerec_helper.rec_audio_response('Would you like me to open your open notes file, text notes file, or none? Please enter answer')

if(audio_notes_question == "text"):
    file_contents = file_helpers.file_read()
    text_twilio.text(file_contents, "NUMBER TO SEND TO HERE")

if(audio_notes_question == "none"):
    print "Alright sounds good :)"

if(audio_notes_question == "open"):
    file_contents = file_helpers.file_read()
    print file_contents



## FILE OPERATIONS: APPENDING 


user_input = voicerec_helper.rec_audio_response('Would you like to make any additions to your notes file?')
os.system("say 'Would you like to make any additions to your notes file?' ")


if(user_input == "yes"):
    edit_input = raw_input("Please type in your inputs")
    file_helpers.file_edit(edit_input)
    

elif(user_input == "no"):
    print "Alright no problem sounds good :)"



## FILE OPERATIONS: SEND UPDATED FILE
    
    
os.system("say 'Would you like me to text you an updated version of your notes file?' ")
user_input = voicerec_helper.rec_audio_response('Would you like me to text you an updated version of your notes file? (Yes/ No)')


if(user_input == "yes"):
    file_contents = file_helpers.file_read()
    text_twilio.text(file_contents, "NUMBER TO SEND TO HERE")
else:
    print "Alright sounds good :)"
    
    
## SCAN EMAIL OPERATIONS

    
os.system("say 'Would you like me to scan through email and see if you received important email?' ")
user_input = voicerec_helper.rec_audio_response('Would you like me to scan through email and see if you received important email?')    


if(user_input == "yes"):
    email_helpers.email_get()
    
elif(user_input == "no"):
    print "Alright no problem sounds good :)"





##     DONE


print "Okay it seems like morning task is done Good Luck with your day ^-^"        
