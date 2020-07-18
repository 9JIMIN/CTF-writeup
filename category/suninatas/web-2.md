# web-2

- id, pw를 제출하는 form이 있다. 
- script가 form안에 있어서 client side에서 필터링을 한다.
- 이런 필터링은 프록시로 요청을 만들어서 보내면 우회가 가능하다. 

- burpsuite에서 id, pw POST요청을 가져와서, body를 만들어 보내면 script의 필터링없이 값이 서버에 전달된다. 

>비슷한 문제를 많이 풀었는데도 고민하다니.. 새로운 문제만 풀지말고! 복습도 좀 하자!!