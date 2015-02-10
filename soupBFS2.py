
# coding: utf-8

# In[3]:

"""
import urllib2
from bs4 import BeautifulSoup

page_object = urllib2.urlopen(r'file:\\C:\Users\atul_anand01\Desktop\test-html-imdb.html')
soup = BeautifulSoup(page_object)
links = soup.find_all('a')
for link in links:
    print  link.get('href') , '-=-=-=-=-=-=', link.get_text()
    

"""


import urllib2
from bs4 import BeautifulSoup
import requests
from urlparse import urlparse


def BFS(link_list1,check_redirection,append_to_file,file,level,response_object,level_var = 1):

    level = level - 1
    text = "level: "+str(level_var) + "\n" + "_________"
    append_to_file(file,text)
    len = len(linklist1)
    for link in link_list1:
        check_redirection(link.get('href'))
        
        text ='link:  '+link.get_text()+'/n'+'_______'+'/n'+'url:  '+link.get('href')+'/n' +'redirected url:  '+response_object.url+'/n'+'status code:  '+r.status_code+'/n'+'history'+r.history
        append_to_file(file,text)
        
        page = urllib2.ulropen(link)
        soup = BeautifulSoup(page)
        ##Adding parent link to the actual link so as to make complete link path
        links = soup.find_all('a')
        for every_link in links:
            complete_link = ''
            if every_link.get('href')[0:3] != 'http' and every_link.get('href')[0] == '/':
                #every_link.set('href') = link.get('href')+every_link.get('href')  ##check if there is a set function
                every_link['href'] = link.get('href')+every_link.get('href') ##can you change the value in the list like this?
                
                #Here can be included the function to check the navigation to the domain only if asked
                
                #complete_link_text_path =link.get_text() +'-->'+ every_link.get_text()
                #every_link['text'] = link.get_text() + '-->' + every_link.get_text() ## since there is no text attribute in the list, it can be create
                                                                    ## to serve the purpose like this?
            link_list2.append(every_link)
            #link_path_list2.append(complete_link_text_path)
        #link_list2.append(soup.find_all('a'))

        len = len - 1 
        if(len==0):
            BFS(link_list2) 
        if level == 0:
            # exit the loop
            break
    level_var = level_var + 1


def append_to_file(file,text):
    file.write(text) 

def prettify_link(link):
    new_link = ''
    if link[0:3] == 'http':
        new_link = link
    else:
        new_link = 'http://'+link
    return new_link




def check_domain_limit(link_string,domain_string):
    if domain_string in link_string:
        return 1
    else:
        return 2

def print_details(response_object, link): # Expects a response object and link
    print (response_object.url)
    print (response_object.status_code)
    print (response_ojbect.history)

def check_redirection(link_foo):
    r = requests.get(link_foo, timeout = 0.01) # A response object
    return r



##Always start with a smaller wireframe, most basic - a single functionality
##Execution for the script




#Ask for creation of the name of the report file

filename = raw_input("Enter the file name")

#Create the file with the file name and open it for editing

file = open(filename,'w')

#How deep you want to go? - define level

level = int(raw_input("how deep you want to go?"))
if level <= 0 :
    print "level needs to be bigger than 0"
    level = int(raw_input("please enter again"))

#default level 10

#Ask for the website link and create domain_string

given_url = raw_input("Provide the website link to be crawled")
parsed_url_object = urlparse(prettify_link(given_url))
domain_string = parsed_url_object.netloc  ## this will not be able to check for the urls like blog.example.com

#Also ask if they want to check for the domain or not
print """Check within domain only?
    1. yes
    2. no
    """
domain_check = int(raw_input("Choose an option"))

refined_link = [prettify_link(given_url)]
response_object = check_redirection(refined_link)

BFS(refined_link,check_redirection,append_to_file,file,level,response_object,level_var)

file.close()  #Close the file

#Display operation finishing message

print "Operation finished. Report is saved at given location"


# In[4]:

import matplotlib.pyplot as pyplot
pyplot.pie([1,2,3])
pyplot.show()

