# web-6

    게시판이 있다. 내용을 확인해본다. 
    md5 해싱사이트 주소가 있다. 힌트인가보다. 
    그리고, password를 입력할 수 있는 input필드가 있다. 

- input 필드의 아래에는 SQL 쿼리가 있다. 여기에 넣은 인풋값이 `pwd`에 들어가는 것 같다. 
- `"select szPwd from T_Web13 where nIdx = '3' and szPwd = '"&pwd&"'"`
- `' or 1--`를 넣어서 참이 되도록 하는데, `NO hacking!` 이라고, 해킹을 감지하고, 에러를 띄운다.
    - client쪽에서 필터링을 하는지 확인해보니, 그런건 없다. 
    - 그럼, 서버쪽에서 필터링을 한다는 건데.. 
    - 항상 참이 되는 다른 여러 쿼리를 보내본다. 
    - `'or '2'>'1'--`이게 통한다.

- 그렇게 auth key를 획득할 수고 이걸로 게시물을 읽을 수 있다고 한다. 
- **결국 이 문제는 권한에 대한 내용, 쿠키를 조작해야 한다.**
- 받은 내용을 md5로 해싱하고, 쿠키값으로 넣어준다. 
- 그럼 내용이 보인다. 표면상에는 별 내용이 없길래.. 개발자 도구로 요소를 본다. 보니 이런게 있다.
- `<form method="post" name="KEY_HINT" action="Rome's First Emperor"></form>` 
- 아니 근데 이렇게만 주면 보고도 걍 지나갈 듯.. 핵심은 SQL인젝션에 쿠키값 조작이 전부인데, 막판에 이렇게 애매하게 답을 줄 필요가 있었나 싶다. 왜냐하면 내가 보고도 몰랐거든. 
- 암튼, 답은 로마의 첫번째 황제이름은 `Augustus`였다.
***
> SQL인젝션으로 기본적인 필터링을 우회하는 방법을 알 수 있는 문제이다.    
그리고, 쿠키값을 조작하여 권한을 얻는 것도 해볼 수 있는 문제이다. 