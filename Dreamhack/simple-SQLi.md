# simple-SQLi

    id, pw를 받는 인풋이 있다.
    admin으로 로그인을 해야한다. 

- id = `admin" or 1--` 해보니, guest로 로그인이 된다.
    - ?? 아마도, 참이 되는 것은 맞지만, 테이블의 최상단에 guest가 있어서, 그게 나오는 듯. 그래서 앞에 admin을 붙이는 게 의미없음. 

- `or 1 order by 1--` 로 정렬을 바꾸거나, 
- `admin--` 만 보내서 `or 1` 처럼 전부 참이 되지 않게 한다.