# web-3

    공지게시판에 글을 쓰라고 함. 
    당연히 공지게시판에 글쓸 수 있는 기능이 없음. 

    하지만! 자유게시판에는 글을 쓸 수 있음. 
    그래서 burpsuite로 자유게시판에 글쓰는 POST 요청을 reqeater로 보냄. 

`POST /board/free/write HTTP/1.1`   
`POST /board/notice/write HTTP/1.1`

free를 notice로 바꿈. 그리고 요청을 보내면, 키가 나옴.

>웹 표면 상에는 특정 요청을 보낼 방법을 안 만들어놔도, 어떤 요청을 만들어낼지 모름.    
> 따라서, 서버로 오는 모든 요청은 검열이 필수!