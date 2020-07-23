# for-18

    알 수 없는 숫자들이 쫙 나열되어 있다. 
    이걸 해석하는 것이 문제.

- 아스키 코드다. (이걸 파악하면 다 푼거다.)
- 파이썬으로 아스키를 문자로 변환한다. 
- `VG9kYXkgaXMgYSBnb29kIGRheS4gVGhlIEF1dGhLZXkgaXMgVmVyeVZlcnlUb25nVG9uZ0d1cmkh`
- base64 인코딩되어있다. (이걸 바로 좀 파악하자..)
- 디코딩하면 답이 나옴.


        import base64


        n = '
        86 71 57 107 89 88 107 103 97 88 77 103 89 83 66 110 98 50 57 107 73 71 82 104 101 83 52 103 86 71 104 108 73 69 70 49 100 71 104 76 90 88 107 103 97 88 77 103 86 109 86 121 101 86 90 108 99 110 108 85 98 50 53 110 86 71 57 117 90 48 100 49 99 109 107 104 
        '

        n = list(map(int, n.split()))
        ans = []
        for i in range(len(n)):
            ans.append(chr(n.pop(0)))

        ans = ''.join(ans)
        e = base64.b64decode(ans)
        print(e) // 
        
- Today is a good day. The AuthKey is VeryVeryTongTongGuri!

> 해킹에는 감이 중요하다. 경험이 필요한거지.   
처음에 숫자들을 보고, ascii를 파악하는 것.   
바꾼 문자열을보고, base64 인코딩된 것을 파악하는 것.   