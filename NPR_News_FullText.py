from urllib import request
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'http://www.npr.org/sections/news'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = request.Request(url, headers=head)
    response = request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')
    soup_texts = soup.find_all('h2', class_='title')

# Open the destination txt file
    f = open('G:/Code/Python/NPR/NPR.txt', 'w', encoding='utf-8')

# loop through chapter links
    for link in soup_texts:
        if link != '\n':
            download_url = link.a.get('href')
            #print(download_url)
            download_req = request.Request(download_url, headers=head)
            download_response = request.urlopen(download_req)
            download_html = download_response.read()
            download_soup = BeautifulSoup(download_html, 'lxml')
            download_soup_texts = download_soup.find('div',id='storytext')
# Get the texts
# Get the chapter names
            #f.write(link.text + '\n\n')
            # print(link.text)
            # print(download_chaptername.get_text())
# Print chanpter names and texts
            #f.write(download_soup_texts)
            #f.write('\n\n')
            #print(download_soup_texts)
            for text in download_soup_texts.find_all(['p']):
                f.write(text.get_text())
                f.write('\n\n')
    f.close()