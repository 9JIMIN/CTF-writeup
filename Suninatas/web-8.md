# web-8

    admin의 비번이 0~9999까지라고 한다. 
    
    너무나 쉬운 brute force문제

- burp suite로 POST요청을 intruder로 보내고, 
- password에 페이로드 추가
- 0 ~ 9999 설정, 이거 헷갈리더라. 위에는 자릿수고, 밑에는 소수자릿수
<p align="left">
<img src="../images/Suninatas/web-8.PNG" width="200" >
</p>

- attack!
- length로 정렬하면, 7707만 다름.
