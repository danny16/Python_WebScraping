from urllib import request
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # Index Page
    url = 'http://www.npr.org/sections/news/'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = request.Request(url, headers=head)
    response = request.urlopen(req)
    html = response.read()
    # Analyze Index Page
    soup = BeautifulSoup(html, 'html.parser')
    # find_next find next <div>
    soup_texts = soup.find_all('h2',class_='title')
    f = open('G:/Code/Python/NPR/NPR.txt', 'w')
    # Loop through all links, print chapter names and links
    for link in soup_texts:
        f.write(link.text)
        f.write(link.a.get('href'))
        f.write('\n\n')
