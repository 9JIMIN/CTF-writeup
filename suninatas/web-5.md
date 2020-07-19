# web-5

    <script>
	eval(function(p,a,c,k,e,r){e=function(c){return c.toString(a)};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('g l=m o(\'0\',\'1\',\'2\',\'3\',\'4\',\'5\',\'6\',\'7\',\'8\',\'9\',\'a\',\'b\',\'c\',\'d\',\'e\',\'f\');p q(n){g h=\'\';g j=r;s(g i=t;i>0;){i-=4;g k=(n>>i)&u;v(!j||k!=0){j=w;h+=l[k]}}x(h==\'\'?\'0\':h)}',34,34,'||||||||||||||||var|result||start|digit|digitArray|new||Array|function|PASS|true|for|32|0xf|if|false|return'.split('|'),0,{}))		
    </script>

이런 난독화된 script가 삽입되어 있다.   
check key value라고, input을 받고 있고, 아무런 값도 안 준다.    힌트는 `<!--Hint : 12342046413275659 -->`  
저 스크립트를 해석하는게 핵심일 듯.

- 자바스크립트 난독화는 말 그대로 사람이 보기 힘들게 코드를 꼬는 것이다. 난 봐도 모르겠지만, 컴퓨터는 이해를 잘 할테니.. 자바스크립트를 잘 아는 콘솔에 저 함수를 넣어본다. 
- 잘보면 `eval()`로 함수를 감싸고 있다. 그래서 그걸 풀고, `a=function...` 이렇게 넣어본다. 
- 그럼 문장이 하나 튀어나온다. 
- 보면 `PASS` 라는 이름의 함수가 있다.
- 숫자를 받는 함수이고, 여기에 힌트를 넣어야한다는 것을 본능적으로 느낄 수 있다.
- `PASS(12342046413275659)`
- `9c43c20c`
- 이걸 인풋에 넣으면 키가 나온다. 

<p align="center">
<img src="../images/Suninatas/web-5.PNG" width="600" >
<p align="center">이렇게 할거 없이 eval(p,a,c,k,e,r)를 검색하면 언팩킹 사이트가 나온다.</p>
</p>

> 자바스크립트 난독화를 실제로 보는 건 처음이라 처음엔 감을 못 잡았다. 그래도 콘솔로 접근해서 함수를 해석하게 하는 것은 좋은 방법이있다.