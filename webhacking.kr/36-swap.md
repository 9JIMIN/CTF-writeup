# 스왑파일

**While editing index.php file using vi editor in the current directory, a power outage caused the source code to disappear.**
**Please help me recover.**

위와 같은 문구가 있다. 이게 끝-

***

vi에디터로 편집을 하는 중에 저장을 하기 전까지의 내용은 메모리에 일시적으로 저장이 된다. 그래서 저장을 못하고 터미널을 끄게 되면 변경된 내용을 유지하기 위한 스왑파일이 생성된다. 

가령, 

```
jimin.txt 라는 파일을 편집중에 터미널을 끄면, 
.jimin.txt.swp 라는 스왑파일이 생성된다. 
```

 따라서, 스왑파일을 통한 파일복구가 가능하다. 

***

문제에서 index.php를 수정중에 문제가 생겼다고 했기에 

```
.index.php.swp
```

이름의 스왑파일이 생성되었을 것이다. 

```
https://webhacking.kr/challenge/bonus-8/.index.php.swp
```

url에 넣고 요청을 보내면 해당 파일을 받을 수 있다. 

바이너리파일이기에 헥스에디터로 열어봐도 확인이 가능하지만, 
좀더 정석적인 풀이는 직접 vim을 통해 복구하는 것.

터미널을 열어서 아래와 같이 vim으로 열면, 알아서 스왑파일 내용을 기반으로 복구를 한다. 

```
vim -r index.php.swp
```

```
<?php
  $flag = "FLAG{what_about_the_nano_editor?}";
?>
~
~
~
```

짠-

> 가끔, ppt파일을 편집하다보면 이상한 파일이 생기는 것은 알고 있었는데, 
> 이걸로 직접 복구를 해본적은 처음이었다. 
>
> 저장을 제대로 못했을 경우에는 스왑파일같은 임시저장파일을 이용할 수 있다는 것을 확실하게 알게 되었다. 
> vi에디터는 .파일명.swp 라는 이름의 스왑파일을 만든다!!