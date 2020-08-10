# admin으로 로그인하기

시작화면에 

- login
- join

이렇게 두개가 있다. 그리고 join을 하려 하면, Access deny가 뜬다. 
소스를 살펴보니, join버튼에 onclick으로 alert 함수가 부여되어있다. 

```html
<input 
       type="button" value="Login" 
       style="border:0;width:100;background=black;color=green" 
       onmouseover="this.focus();" 
       onclick="move('login');">

<input type="button" value="Join" 
       style="border:0;width:100;background=black;color=blue" 
       onmouseover="this.focus();" 
       onclick="no();">

<script>
	function no(){
	alert('Access_Denied');
	}
	function move(page){
	if(page=='login') { location.href='mem/login.php'; }
	}
</script>
```

page값에는 'login', 'join' 이 있는것 같은데 join은 제대로 함수가 안만들어져있다. 
콘솔에 아래와 같이 함수를 재정의해도 되지만, 그냥 join을 url에 쳐서 이동해보자.

```javascript
function no(){
location.href='mem/join.php'
}
```

challenge/web-05/mem/join.php 에 오면 아무것도 없다. 
다시 소스를 보면 아래와 같은 스크립트가 있다. 

```javascript
l = 'a';
ll = 'b';
lll = 'c';
llll = 'd';
lllll = 'e';
llllll = 'f';
lllllll = 'g';
llllllll = 'h';
lllllllll = 'i';
llllllllll = 'j';
lllllllllll = 'k';
llllllllllll = 'l';
lllllllllllll = 'm';
llllllllllllll = 'n';
lllllllllllllll = 'o';
llllllllllllllll = 'p';
lllllllllllllllll = 'q';
llllllllllllllllll = 'r';
lllllllllllllllllll = 's';
llllllllllllllllllll = 't';
lllllllllllllllllllll = 'u';
llllllllllllllllllllll = 'v';
lllllllllllllllllllllll = 'w';
llllllllllllllllllllllll = 'x';
lllllllllllllllllllllllll = 'y';
llllllllllllllllllllllllll = 'z';
I = '1';
II = '2';
III = '3';
IIII = '4';
IIIII = '5';
IIIIII = '6';
IIIIIII = '7';
IIIIIIII = '8';
IIIIIIIII = '9';
IIIIIIIIII = '0';
li = '.';
ii = '<';
iii = '>';
lIllIllIllIllIllIllIllIllIllIl = lllllllllllllll + llllllllllll + llll + llllllllllllllllllllllllll + lllllllllllllll + lllllllllllll + ll + lllllllll + lllll;
lIIIIIIIIIIIIIIIIIIl = llll + lllllllllllllll + lll + lllllllllllllllllllll + lllllllllllll + lllll + llllllllllllll + llllllllllllllllllll + li + lll + lllllllllllllll + lllllllllllllll + lllllllllll + lllllllll + lllll;
if (eval(lIIIIIIIIIIIIIIIIIIl).indexOf(lIllIllIllIllIllIllIllIllIllIl) == -1) {
    alert('bye');
    throw "stop";
}
if (eval(llll + lllllllllllllll + lll + lllllllllllllllllllll + lllllllllllll + lllll + llllllllllllll + llllllllllllllllllll + li + 'U' + 'R' + 'L').indexOf(lllllllllllll + lllllllllllllll + llll + lllll + '=' + I) == -1) {
    alert('access_denied');
    throw "stop";
} else {
    document.write('<font size=2 color=white>Join</font><p>');
    document.write('.<p>.<p>.<p>.<p>.<p>');
    document.write('<form method=post action=' + llllllllll + lllllllllllllll + lllllllll + llllllllllllll + li + llllllllllllllll + llllllll + llllllllllllllll +
        '>');
    document.write('<table border=1><tr><td><font color=gray>id</font></td><td><input type=text name=' + lllllllll + llll + ' maxlength=20></td></tr>');
    document.write('<tr><td><font color=gray>pass</font></td><td><input type=text name=' + llllllllllllllll + lllllllllllllllllllllll + '></td></tr>');
    document.write('<tr align=center><td colspan=2><input type=submit></td></tr></form></table>');
}
```

내용은 콘솔에서 확인이 가능하다. 
근데 대충봐도 끝에 if 로 접근못하게 막고, else에서 뭔가 join 폼이 나타나는 듯하다. 

그래서 저 else부분만 따로 실행을 시켜본다. 

```html
document.write('<font size=2 color=white>Join</font><p>');
document.write('.<p>.<p>.<p>.<p>.<p>');
document.write('<form method=post action=' + llllllllll + lllllllllllllll + lllllllll + llllllllllllll + li + llllllllllllllll + llllllll + llllllllllllllll + '>');
document.write('<table border=1><tr><td><font color=gray>id</font></td><td><input type=text name=' + lllllllll + llll + ' maxlength=20></td></tr>');
document.write('<tr><td><font color=gray>pass</font></td><td><input type=text name=' + llllllllllllllll + lllllllllllllllllllllll + '></td></tr>');
document.write('<tr align=center><td colspan=2><input type=submit></td></tr></form></table>');
```

그럼 드디어 join 폼이 나타난다. 
하지만, 목표한 admin으로 가입하면 이미 admin이 등록되어있다고 나온다. 

처음 알았는데 `admin           ' `  이런식으로 문자 뒤에 공백을 넣으면 가입이 된다. 
이건 php의 insert버그를 이용하는 것이다. 
데이터베이스에 길이가 5자로 제한되어있으면, 
그 이상의 문자가 와도 앞에 5개만 저장을 하기에 이게 가능하다고 한다. 

그렇게 admin으로 가입하고, 로그인하면 해결된다. 

> 스크립트 해석은 별거 없었지만, 마지막에 admin 뒤에 공백을 붙이는 php insert버그는 처음 알았다.