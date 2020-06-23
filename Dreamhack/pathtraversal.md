# pathtraversal

    유저의 이름을 넣고, 해당 유저경로의 내용을 출력하는 기능이 있다.
    input 값에 대한 필터링이 허술하여 path traversal공격에 취약.

    flag는 /api/flag 경로에 있다.

- /api/user, /api/flag 경로는 localhost로만 접근이 가능하다.
    - 따라서 input을 받아서 /api/user/{userid} 경로로 POST 요청을 보내는 주어진 기능을 이용해야한다. 

- 하지만 input값에 대해서 Client side의 필터링이 있다.
    - 받은 input값을 id값으로 바꿔서 요청바디로 넣는 방식이다. 
    - 이걸 우회하기 위해 프록시로 HTTP 요청을 만들어서 보내면 된다.
    - burpsuite도 되지만, postman으로도 가능.
    
- 바디의 formdata에 ../flag를 넣으면 필터링없이 그 바디 그대로 값이 서버로 가고, /api/user/../flag가 되어, /api/flag에 접근, 출력된 값을 받을 수 있다.

> - Path Traversal 취약점은 파일 경로를 조작하여, 서버에 있는 중요한 파일을 읽고, 조작할 수 있을 때 발생한다.
> - 이번 문제에서 /api/user/{userid} 에 input값이 들어간다는 것에서 Path Traversal 취역점이 생긴다. 
> - 그래서 input값에 ../flag를 넣어주기만 하면된다.
> - **Client side의 필터링을 우회하기 위해, 프록시로 직접 요청바디를 만들어서 보낸다.**  