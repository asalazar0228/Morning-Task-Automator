from bs4 import BeautifulSoup
import webbrowser
import requests
import os

def grab_slickdeals_information():

##    PLEASE NOTE:
##        USING TWO ARRAYS/VECTORS TO HOLD THE TITLES AND HREFS IS PROBABLY
##        NOT THE BEST APPROACH. THE REASON WAS I DID IT WAS FOR EASE OF USE AND READABILITY.
##        TIME AND SPACE WISE IT SHOULD BE FINE DUE TO THE FACT THAT SPACE USED
##        IS AT LOWER BOUND AND LOOKUP TIME IS WORST CASE N WITH N BEING THE AMOUNT OF TITLES
##        PARSED OUT


    

    ##pull website content and format it
    page = requests.get('http://www.slickdeals.net')
    soup = BeautifulSoup(page.text, "html.parser")

    ##pull all the prices and descriptions 
    new_soup = soup.find_all("div", {"class":"priceLine"})
    href_soup = soup.find_all("a",{"class":"itemImageLink"})

    ##take user input
    os.system("say 'What are you looking for? Please type in search item to console' ")
    user_input = raw_input("What are you looking for?")


    ##declaring variables, count for arrays, 
    count = 0
    item_count = 1
    href_array = []

    
    for i in new_soup:
        
        ## grabbing title from html element and splitting into arrat for checking
        instance = i['title']
        results_array = instance.split()

        
        for x in results_array:

            ##if x = user input then it will print count, name, and href
            if(x == user_input):
                print item_count
                print instance
                print "http://www.slickdeals.net" + href_soup[count+1]['href'] + "\n"

                ## increase item_count number found
                item_count += 1

                ##append the href to the array of matching titles
                href_array.append(href_soup[count+1]['href'])
                break

        ##increase count in order to get 
        count +=1


    href_input = raw_input("Would you like to be directed to a webpage?")
    if(href_input == 'yes'):
        print 'Please provide me with a number :)'
        number_href = int(raw_input())
        num = number_href - 1


        webbrowser.open('http://www.slickdeals.net'+ href_array[num])
    else:
        print "Alright sounds god I hope you got what u needed"
