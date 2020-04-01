from bs4 import BeautifulSoup
import requests

source=requests.get("http://coreyms.com").text

soup=BeautifulSoup(source,'lxml')

article=soup.find('article')

#print(article.prettify())

summary=article.find("div",class_='entry-content').p.text #383
print(summary)

#output:
'''
In this Python Programming Tutorial, we will be learning how to set up a 
Python development environment in VSCode on Windows. VSCode is a very nice 
free editor for writing Python applications and many developers are now 
switching over to this editor. In this video, we will learn how to install
 VSCode, get the Python extension installed, how to change Python 
 interpreters, create virtual environments, format/lint our code, how to use
  Git within VSCode, how to debug our programs, how unit testing works, and 
  more. We have a lot to cover, so let’s go ahead and get started…'''