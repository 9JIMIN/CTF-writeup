import base64

user = 'admin'.encode('UTF-8')
password = 'nimda'.encode('UTF-8')

for _ in range(20):
    user = base64.b64encode(user)
    password = base64.b64encode(password)

def enc(s):
    s = s.replace('1', '!')
    s = s.replace('2', '@')
    s = s.replace('3', '$')
    s = s.replace('4', '^')
    s = s.replace('5', '&')
    s = s.replace('6', '*')
    s = s.replace('7', '(')
    s = s.replace('8', ')')
    return s

# replace는 원래값은 그대로임. 그래서 새로 넣어줘야함.
print(enc(user.decode()))
print(enc(password.decode()))
