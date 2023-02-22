import json

obj = open('tsis4\json\package.json')
dict = json.loads(obj.read())

print('Interface Status')
print('Dn', 'Description', 'Speed', "MTU", sep='    ')
for x in dict[ 'imdata' ]:
    dn = x['l1PhysIf']['attributes'].get('dn')
    desk = x['l1PhysIf']['attributes'].get('descr')
    speed = x['l1PhysIf']['attributes'].get('fecMode')
    mtu = x['l1PhysIf']['attributes'].get('mtu')
    print(dn, desk, speed, mtu, sep='    ')