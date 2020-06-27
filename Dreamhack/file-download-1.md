# file-download-1

- 파일을 업로드하는 기능이 있다. 
- 업로드한 파일의 리스트를 보고, 내용을 보는 URL의 구조는 다음과 같다.
`/read?name=<파일명>`
- 그리고 app.py를 보면 `open(f'{UPLOAD_DIR}/{filename}', 'rb')` 이런식으로 파일명에 대한 검증없이 그냥 파일을 가져온다. 
- flag는 `/flag`에 있다. 따라서 `uploads/../flag`가 되도록, URL을 `/read?name=../flag` 로 만들어서 요청을 보낸다.

- 그럼. /flag의 내용을 읽어서 보여준다.