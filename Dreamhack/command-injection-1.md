# command-injection-1

- `ping -c 3 "{host}"`로 host를 받아서, 
- `subprocess.check_output(['/bin/sh', '-c', cmd], timeout=5)` ping요청을 보냄.
- flag.py파일을 읽어야하는데.. 그럼, 커맨드 명령으로 파일을 보는 방법을 알아야할듯..
    - 먼저 앞에 있는 ping을 빠져나올 수 있어야함. ping으로는 내용을 알 수가 없어.
    - 어떻게 하는 걸까, 참고자료에 web basic만 있는 걸 보면 아주 기본적인 거 같은데.. 뭘까..