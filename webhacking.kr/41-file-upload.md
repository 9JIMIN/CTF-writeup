# 파일 업로드 & 에러 메세지

```php+HTML
<?php
  include "../../config.php";
  include "./inc.php";
  if($_GET['view_source']) view_source();
  error_reporting(E_ALL);
  ini_set("display_errors", 1);
?><html>
<head>
<title>Challenge 41</title>
</head>
<body>
<?php
  if(isset($_FILES['up']) && $_FILES['up']){
    $fn = $_FILES['up']['name'];
    $fn = str_replace(".","",$fn);
    $fn = str_replace("<","",$fn);
    $fn = str_replace(">","",$fn);
    $fn = str_replace("/","",$fn);

    $cp = $_FILES['up']['tmp_name'];
    copy($cp,"./{$upload_dir}/{$fn}");
    $f = @fopen("./{$upload_dir}/{$fn}","w");
    @fwrite($f,$flag);
    @fclose($f);
    echo("Done~");
  }
?>
<form method=post enctype="multipart/form-data">
<input type=file name=up><input type=submit value='upload'>
</form>
<a href=./?view_source=1>view-source</a>
</body>
</html>
```

파일을 올릴 수 있다. 

소스를 보면, `fn` 변수에 파일명을 저장해서 필터링을 한다.
../../ 이런 공격은 의미없다는 것을 보여준다.

필터링된 파일명을 `upload_dir` 경로에 파일을 저장한다. 

즉, `upload_dir` 이 뭔지 알아내야한다. 
이걸 알아내기 위해서는 에러를 내는 파일을 넣어서, 그 에러내용에 `'~~~ 경로에 업로드 중 에러'` 이걸 뜨게 만들어야 한다. 

그래서 필터링에 걸리는 '<' 파일을 올려봤지만, 에러는 뜨는데, 경로는 안뜨더라..
`copy($cp,"./{$upload_dir}/{$fn}");` 이 copy() 코드가 실행될때, 에러를 내기 위해서는 `fn` 파일명 자체가 시스템이 받아들일 수 없는 값이어야 한다.

찾아보니..

리눅스 시스템에서 파일이름 길이의 한계는 255라고 한다. 
그래서 256글자의 이름을 가진 파일을 올리면, 
에러가 나면서 upload 경로가 노출되고, 해당 경로로 들어가면 flag를 얻을 수 있다.

> 파일 업로드 공격은 파일명에 ../../ 이런거 넣고, 하는 줄 알았는데, 
> 에러 메시지를 이용한 공격이었다. 
>
> 에러 메세지에는 많은 정보가 포함될 수 있으니, 노출되지 않도록 조심.

