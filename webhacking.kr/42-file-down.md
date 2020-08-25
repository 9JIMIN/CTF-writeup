# 파일 다운받기

- `test.txt [download]`
- `flag.docx [download]`

이렇게 두 파일을 받을 수 있게 되어있다. 
하지만, `test.txt`만 받아지고, `flag.docx` 는 경고창이 뜨면서 받아지지 않는다.

처음에는 다운 권한을 얻는 거라서 쿠키를 조작해야되나.. 싶었지만, 그게 아니었다. 
다운을 받을려면 다운 링크를 알면된다. 
`test.txt` 를 받는 링크를 보면 마치 base64 인코딩값처럼 생겼다.

```
?down=dGVzdC50eHQ=
```

그래서 저걸 디코딩 해보니..

```
test.txt
```

즉, `flag.docx`를 인코딩해서 down에 넣어주면 된다.

```
?down=ZmxhZy5kb2N4
```

그럼 다운이 된다. 

word가 안깔려 있어서 docx파일이 xml로 보인다. 
document.xml에 내용이 있으니, 보면 flag를 알 수 있다.

```
FLAG{very_difficult_to_think_up_text_of_the_flag}
```



> base64값이라는 것을 바로 알았더라면, 더 빨리 풀 수 있었을 텐데..