# login-1

    유저화면을 보니, user/17임. 뒤에 오는게 idx값임. 그래서 user/1를 해보니, 여러 계정이 앞에 있었다. 
    관리자 계정의 idx를 확인.
    비번을 재설정하기위해서는 backup코드를 알아야 함. 
    
- 비번 재설정 기능을 이용해야함. backup코드 필터링을 우회하는 것이 최종목표.

- backup코드를 알아내거나, 없어도 요청이 가게 하거나. 

- backup코드는 받은 값을 int로 인코딩을 함. => 코드를 넣을 수가 없음..

- 계정화면에는 userid, userName, userLevel이 표시됨. 
- 이걸 user backupCode로 바꿔서 출력을 하게 하면 되는데...
    - 이 방법은 불가능한 듯. 
***

- 쿠키가 `{"idx":17,"level":"guest","name":"one","userid":"one"}`를 base64로 인코딩한 형태이다. 
- 그래서 내용을 바꿔서 `{"idx":1,"level":"admin","name":"Apple","userid":"Apple"}` 이걸 인코딩해서 넣어주니.. 안된다. 왜지?? 맞는 거 같은데..