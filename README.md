# Morning-Task-Automator

The purpose of this script is to automate my morning routines. 
Note: Uses voice recognition for responses.

Before using make sure all dependencies are installed and you have set up login information for twilio and your email.
All requirements and instructions can be found [here](Dependencies.md)

The current version supports the following tasks:

1. Parse out slickdeals.com titles and href's and allow you to search through them with by specifying a keyword.

2. Open and edit a text file containing your notes.

3. Text you your notes

4. Scan your email and print out new emails with subject and sender information.

I will slowly add more functions when I have time :). 

---------Installations required---------

Install requests:
```bash
pip install requests
```

Install beautifulsoup4
```bash
pip install beautifulsoup4
```

Install twilio
```bash
pip install twilio
```

Install SpeechRecognition
```bash
pip install SpeechRecognition
```
---------Files Requiring modifications---------

The following lines in files require modification:

#### --- Lines 7, 8 in email_helpers.py --- 
Place in your gmail username and password

#### --- Lines 5, 6, 10 in text_twilio.py --- 
Place your twilio account info and phone number provided

#### --- Lines 57, 94 in Morning Task Automator.py ---
Place number you would like to send to

