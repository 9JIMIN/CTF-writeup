<!-- ---
layout: default
title: command-injection-1
nav_order: 1
parent: dreamhack
--- -->

# command-injection-1

- `ping -c 3 "{host}"`로 host를 받아서, ping요청을 보냄.
- flag.py파일을 읽어야하는데.. 그럼, 커맨드 명령으로 파일을 보는 방법을 알아야할듯..
    - 먼저 앞에 있는 ping을 빠져나올 수 있어야함. ping으로는 내용을 알 수가 없어.
    - 어떻게 하는 걸까, 참고자료에 web basic만 있는 걸 보면 아주 기본적인 거 같은데.. 뭘까..

- 리눅스cmd에는 `cat test.txt` 처럼 cat이라는 파일을 읽을 수 있는 명령어가 있다. (윈도우는 type) 
- 이 명령어를 실행하기 위해 일단 앞에 ping을 끝내고 `|`로 명령을 분리하고 넣어준다. (디바이더로는 `;`,  `&`도 가능, `&&`은 앞선 명령의 실행이 성공했을 때만)
    - `8.8.8.8"| cat "flag.py` 입력
    - 실행되는 명령 = `ping -c 3 "8.8.8.8"| cat "flag.py"`
    - ping 실행후, cat이 실행되어 flag를 읽을 수 있다. 