from bs4 import BeautifulSoup
import lxml
import urllib.request
from collections import Counter
from string import punctuation

# Store the website input as a variable and excecute BS4 on it
website = input("What is the URL you want to read faster? ")
web_page = urllib.request.urlopen(website)
soup = BeautifulSoup(web_page,"lxml")

# We get the words within all paragraphs
text_p = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
c_p = Counter((x.rstrip(punctuation).lower() for y in text_p for x in y.split()))

# We get the words within divs
text_div = (''.join(s.findAll(text=True))for s in soup.findAll('div'))
c_div = Counter((x.rstrip(punctuation).lower() for y in text_div for x in y.split()))

# We sum the two countesr and get a list with words count from most to less common
total = c_div + c_p
tot_len = len(total)

print("There are", tot_len, "words on this page.")

word_spd_avg = tot_len/250

print("At the average reading speed, it would take you", word_spd_avg, "minutes to read this article.")
