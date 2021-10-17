import sys
import request
from requests.auth import HTTPBasicAuth


id='YOURHOTSPOTID'

api='YOUAPIHERE'
auth = HTTPBasicAuth(api, '')


def info():
    url="https://api.brandmeister.network/v1.0/repeater/?action=profile&q=%s" % id
    p=request.get(url)
    print(p)
    json=p.json()
    r=json['reflector']
    print(r)
    s=json['staticSubscriptions']
    print(s)
    for tg in s:
        print("=====   ",tg)

def delall():
    url="https://api.brandmeister.network/v1.0/repeater/?action=profile&q=%s" % id
    p=request.get(url)
    json=p.json()
    r=json['reflector']
    s=json['staticSubscriptions']
    for tg in s:
        print("=====   ",tg)
        deltg(tg['talkgroup'])

def deltg(tg):
    url="https://api.brandmeister.network/v1.0/repeater/talkgroup/?action=DEL&id=%s" % id
    data={"talkgroup":tg , "timeslot":"0"}
    r=request.post(url, auth=auth,data=data)
    print(r.text)

def addtg(tg):
    url="https://api.brandmeister.network/v1.0/repeater/talkgroup/?action=ADD&id=%s" % id
    data={"talkgroup":tg , "timeslot":"0"}
    r=request.post(url, auth=auth,data=data)
    print(r.text)

def drop():
    url="https://api.brandmeister.network/v1.0/repeater/setRepeaterTarantool.php?action=dropDynamicGroups&slot=0&q=%s" %id
    r=request.get(url, auth=auth)
    print(r.text)



print(len(sys.argv))
if len(sys.argv) >1:
    print("debug mode , run by input")
    print(sys.argv[1])
    cmd=sys.argv[1]
    argu=sys.argv[2]
    print(" %s %s " %(cmd,argu))
    if cmd=="add":
        addtg(argu)
    elif cmd=="del":
        deltg(argu)
    elif cmd=="delall":
        delall()
    elif cmd=="info":
        info()
    elif cmd=="drop":
        drop()
    else:
        info()
else:
    info()
    print("Please input your option")

