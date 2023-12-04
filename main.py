import requests
from bs4 import BeautifulSoup

#Get the Website using requests
url = "https://www.churchofjesuschrist.org/study/general-conference/2022/10/25soares?lang=eng"
response = requests.get(url)
if response.status_code == 200:
    print("Success")
    html_content    = response.content
else:
    print("Failure")
# print(response.text)

#Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

#Get article text
article_text = soup.find_all('article')

#get the text
# for article in article_text:
text_total = []
for i in article_text:
  text_total += i.get_text()

text_total = ''.join(text_total)
print(text_total)