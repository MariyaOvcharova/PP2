import json

file = open("jsonn.json")

file1 = file.read()

file2 = json.loads(file1)

print('Interface Status')
print('==================================================================================')
print('DN', '                                               ','Description', '         ', 'Speed',' ', 'MTU')
print('-------------------------------------------------- --------------------  ------ -----')

for i in file2['imdata']:
    attributes = i['l1PhysIf']['attributes']
    
    dn = attributes.get('dn', '')
    description = attributes.get('descr', '')
    speed = attributes.get('speed', '')
    
    mtu = int(attributes.get('mtu', 0))
    
    print(dn, '', description, '', speed, mtu, sep='\t')