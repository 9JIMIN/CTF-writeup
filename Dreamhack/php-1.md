# php-1

`<?php include $_GET['page']?$_GET['page'].'.php':'main.php'; ?>`
이런 코드가 있다. 
- 그리고 URL에서
/?page=list, /?page=main 이렇게 받으면, list.php, main.php파일을 보여준다. 
    - 이걸 이용해서 /?page=/var/www/uploads/flag를 하면 파일 내용을 볼 수 있음. 
    - 내용은 `"can you see $flag?"` 이것이 전부..
    - 이상한게 flag.php파일안에 flag가 없음.. 저 이상한 문장이 전부임.
    - 아마도 view, list를 활용해야하는 문제같음. 

- ?/page=view, view.php파일로 파일의 내용을 볼 수 있다. 하지만, 'flag'라는 단어를 필터링한다. 
    - 그래서 알파벳 하나를 2번 인코딩해서 우회하려 했으나, 안됨.
    - 그럼 file의 파라미터로 flag를 넣을 수가 없는 건데.. view의 활용방법을 모르겠음.