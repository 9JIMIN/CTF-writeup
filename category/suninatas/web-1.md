# web-1

    <%
        str = Request("str")

        If not str = "" Then
            result = Replace(str,"a","aad")
            result = Replace(result,"i","in")
            result1 = Mid(result,2,2)
            result2 = Mid(result,4,6)
            result = result1 & result2
            Response.write result
            If result = "admin" Then
                pw = "????????"
            End if
        End if
    %>
- `a`를 입력하면, `aad`로 replace, `i`는 `in`으로..
- 결과에서 2번째부터 2개의 값, 4번째부터 2개의 값을 가져옴. 
- `ami`를 넣으면 `aadmin` 2,2가 `ad`, 4,6이 `min`그래서 `admin`이 되고, pw가 나옴. 
