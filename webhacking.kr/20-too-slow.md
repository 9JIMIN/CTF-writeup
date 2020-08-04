# 빠르게 폼을 보내야하는 문제.

써니나타스에서 같은 문제를 풀어본 적이 있었다. 
그래서 이번에도 requests, soup로 푸는 건 줄 알았지..

근데, 아니였다. 

\<script> 태그를 클라이언트 측에서 변조하는 문제였다. 

```html
<script>
    function ck(){
      if(lv5frm.id.value=="") { lv5frm.id.focus(); return; }
      if(lv5frm.cmt.value=="") { lv5frm.cmt.focus(); return; }
      if(lv5frm.captcha.value=="") { lv5frm.captcha.focus(); return; }
      if(lv5frm.captcha.value!=lv5frm.captcha_.value) { lv5frm.captcha.focus(); return; }
      lv5frm.submit();
    }
</script>
```

이런 스크립트가 있다. 값이 없으면 해당 영역으로 이동하는.. 그런 함수다. 

그러니까 **저기서 if에 빠지지 않도록 하면 된다.**

id값을 뭐든 넣어주고, 
cmt값도 뭐든 넣어주고, 
captcha는 if문에 있는 것 처럼, `lv5frm.captcha_.value`값을 넣어준다.
그리고 submit() 을 실행하면 된다.

```javascript
// 콘솔에 입력한다. 
lv5frm.id.value='d'
lv5frm.cmt.value='d'
lv5frm.captcha.value=lv5frm.captcha_.value
lv5frm.submit()
```

> 이전에도 같은 유형의 문제를 풀었었다. 이번 문제도 클라이언트 측에서 스크립트를 변조하는 간단한 문제였다. 
> 스크립트를 해석하는 능력, 중요한 부분만 캐치해내는 힘이 필요하다.