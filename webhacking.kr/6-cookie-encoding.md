# 6- cookie-encoding

```php
<?php
include "../../config.php";
if($_GET['view_source']) view_source();
if(!$_COOKIE['user']){
$val_id="guest";
$val_pw="123qwe";
for($i=0;$i<20;$i++){
    $val_id=base64_encode($val_id);
    $val_pw=base64_encode($val_pw);
}
$val_id=str_replace("1","!",$val_id);
$val_id=str_replace("2","@",$val_id);
$val_id=str_replace("3","$",$val_id);
$val_id=str_replace("4","^",$val_id);
$val_id=str_replace("5","&",$val_id);
$val_id=str_replace("6","*",$val_id);
$val_id=str_replace("7","(",$val_id);
$val_id=str_replace("8",")",$val_id);

$val_pw=str_replace("1","!",$val_pw);
$val_pw=str_replace("2","@",$val_pw);
$val_pw=str_replace("3","$",$val_pw);
$val_pw=str_replace("4","^",$val_pw);
$val_pw=str_replace("5","&",$val_pw);
$val_pw=str_replace("6","*",$val_pw);
$val_pw=str_replace("7","(",$val_pw);
$val_pw=str_replace("8",")",$val_pw);

Setcookie("user",$val_id,time()+86400,"/challenge/web-06/");
Setcookie("password",$val_pw,time()+86400,"/challenge/web-06/");
echo("<meta http-equiv=refresh content=0>");
exit;
}
?>
<html>
<head>
<title>Challenge 6</title>
<style type="text/css">
body { background:black; color:white; font-size:10pt; }
</style>
</head>
<body>
<?php
$decode_id=$_COOKIE['user'];
$decode_pw=$_COOKIE['password'];

$decode_id=str_replace("!","1",$decode_id);
$decode_id=str_replace("@","2",$decode_id);
$decode_id=str_replace("$","3",$decode_id);
$decode_id=str_replace("^","4",$decode_id);
$decode_id=str_replace("&","5",$decode_id);
$decode_id=str_replace("*","6",$decode_id);
$decode_id=str_replace("(","7",$decode_id);
$decode_id=str_replace(")","8",$decode_id);

$decode_pw=str_replace("!","1",$decode_pw);
$decode_pw=str_replace("@","2",$decode_pw);
$decode_pw=str_replace("$","3",$decode_pw);
$decode_pw=str_replace("^","4",$decode_pw);
$decode_pw=str_replace("&","5",$decode_pw);
$decode_pw=str_replace("*","6",$decode_pw);
$decode_pw=str_replace("(","7",$decode_pw);
$decode_pw=str_replace(")","8",$decode_pw);

for($i=0;$i<20;$i++){
$decode_id=base64_decode($decode_id);
$decode_pw=base64_decode($decode_pw);
}

echo("<hr><a href=./?view_source=1 style=color:yellow;>view-source</a><br><br>");
echo("ID : $decode_id<br>PW : $decode_pw<hr>");

if($decode_id=="admin" && $decode_pw=="nimda"){
solve(6);
}
?>
</body>
</html>
```


- user, password라는 쿠키가 있음
- 원래 user, password 값을 20번 base64인코딩 후에 숫자를 특수문자로 바꾼값이 쿠키이다.

- 그래서 admin, nimda를 20번 base64인코딩하고 숫자를 문자로 바꾸고 나서-
- 그걸 쿠키값으로 설정해주면 admin으로 로그인이 된다.

```python
import base64

user = 'admin'.encode('UTF-8')
password = 'nimda'.encode('UTF-8')

for _ in range(20):
    user = base64.b64encode(user)
    password = base64.b64encode(password)

def enc(s):
    s = s.replace('1', '!')
    s = s.replace('2', '@')
    s = s.replace('3', '$')
    s = s.replace('4', '^')
    s = s.replace('5', '&')
    s = s.replace('6', '*')
    s = s.replace('7', '(')
    s = s.replace('8', ')')
    return s

# replace는 원래값은 그대로임. 그래서 새로 넣어줘야함.

print(enc(user.decode()))
print(enc(password.decode()))
```


>쿠키값은 거의 암호화가 되어있다.    
그리고 그 암호화 알고리즘을 파악하면, 세션탈취가 가능하다는 것을 보여주는 문제이다. 