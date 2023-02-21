from bs4 import BeautifulSoup
from urllib.request import urlopen

print(
  """
  Enter the max amount of characters you want to have in your password below.
  """
)

while True:
  max_length = input("What would you like the max length of the password to be? ")
  print("")
  url = f'https://password-generator.zameerlovesmath.repl.co/maxlength={max_length}'
  page = urlopen(url)
  html = page.read().decode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  print(soup.get_text())
  print("")