# web-4


    'plus'를 누르니 point가 증가한다. 
    25가 되니까 더이상 증가하지 않는다. 
    User-Agent를 보여준다.

    힌트는 'point를 50으로, SuNiNaTaS'
    
- user-agent를 보여준걸 보니, 이걸 조작하는 거고, SuNiNTaS가 그 조작할 값이라는 것을 추리할 수 있다. 

- burpsuite에서 `user-agent: SuNiNaTaS` 로 POST요청을 보냄.
- 그러고 나니, 25 이상으로 point가 증가함. 50까지 누르면 키 획득

>user-agent값을 조작하는 문제, 실제 상황에서는 user-agent 뿐만 아니라, 쿠키, 캐시, 호스트 등등 다른 여러가지 요청헤더를 조작이 가능하다.    
이전 문제와 마찬가지로 서버에 보내는 요청은 내 맘대로 만들 수 있기에 서버는 항상 요청을 비판적으로 받아들여야 함!