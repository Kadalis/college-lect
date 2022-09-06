import bs4 as bs4
import sys

file = open(sys.argv[1], "r")
data = file.read()
soup = bs4.BeautifulSoup(data, features="lxml")

mya = soup.find_all("a", {"class": "b-phrase-link__link"})

for a in mya:
	print(a.contents[0])
