import pip._vendor.requests 
from bs4 import BeautifulSoup

word = "alan turing"
word = word.replace(" ", "-")
first_letter = word[0]

URL = "https://www.computer-dictionary-online.org/definitions-{}/{}.html".format(first_letter, word)
page = pip._vendor.requests.get(URL) # *handle page does not exist
soup = BeautifulSoup(page.content, 'html.parser').body
exists = True

for paragraph in soup.find_all('p'):
    paragraph = paragraph.get_text()
    if paragraph == "[Jargon File]":
        continue
    elif paragraph == "Sorry, but the page you're looking for isn't here.":
        exists = False
        break
    
    print(paragraph)

if not exists:
    print("oh noooo")

