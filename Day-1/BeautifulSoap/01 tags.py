from bs4 import BeautifulSoup

# Data Read garna suru ma (Start by reading data)
'''
Website bata data read garna ko lagi:

1. import requests garera URL bata data fetch garna sakincha.
2. requests.get(url) le URL ma request pathaune ani response pauxa.
3. Response lai BeautifulSoup bata parse garne.

Example:

import requests

url = 'https://example.com'
r = requests.get(url)  # URL bata data fetch garxa

soap = BeautifulSoup(r.text, 'html.parser')  # HTML data soap variable ma parse garxa
'''

# Local HTML file read garne
with open("sample.html", "r") as f:
    html_docs = f.read()
  
soap = BeautifulSoup(html_docs, "html.parser")
# print(soap.prettify())

#Title pauna
# print(soap.title)  #HTML Page ko title dincha
#Output : <title>Intense Diseases and Mortality Rates</title>


print(soap.title.string) #Esle title ko name dincha without <title></title> tag
