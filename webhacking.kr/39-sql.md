# sql

```php
<?php
  include "../../config.php";
  if($_GET['view_source']) view_source();
?><html>
<head>
<title>Chellenge 39</title>
</head>
<body>
<?php
  $db = dbconnect();
  if($_POST['id']){
    $_POST['id'] = str_replace("\\","",$_POST['id']);
    $_POST['id'] = str_replace("'","''",$_POST['id']);
    $_POST['id'] = substr($_POST['id'],0,15);
    $result = mysqli_fetch_array(mysqli_query($db,"select 1 from member where length(id)<14 and id='{$_POST['id']}"));
    if($result[0] == 1){
      solve(39);
    }
  }
?>
<form method=post action=index.php>
<input type=text name=id maxlength=15 size=30>
<input type=submit>
</form>
<a href=?view_source=1>view-source</a>
</body>
</html>
```

쿼리는 아래와 같다. 
닫는 따옴표가 없음.

```sql
select 1 from member where length(id)<14 and id='<받은거>
```

그리고 값이 1이 되면 풀린다. 
id를 받는 부분을 보면, `\\`를 없애고, `'`를 `''`로 바꾸고, substr로 앞의 15개 문자만 받는다.

목표는 admin을 넣는건데, 
그냥 넣으면 따옴표 따옴표가 없어서 안되고, admin'이렇게 넣으면 admin''로 바꿔서 안됨.
그래서 `admin        '` 이렇게 넣으면, `admin         ''` 이렇게 바꿔도 앞에 15개만 가져가기 때문에 성공이 됨.

근데, 왜 `'admin'` 과 `'admin         '` 를 같다고 인식하는 것인가?
그건 SQL의 비교 방법이 이상해서 그럼.
길이가 다른 문자열을 비교할때는 짧은 쪽 끝에 공백을 추가해서 같은 길이로 만들어서 비교를 함.
왜 그러는 건지는 [여기](https://woowabros.github.io/study/2018/02/26/mysql-char-comparison.html)를 참고.

> 아무튼 admin을 넣어야 하는데, admin'나 admin             '나 똑같다는 SQL의 희한한 속성을 보여주는 문제임.