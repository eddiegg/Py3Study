import hashlib

parm_dict={"start":2,"eid":"123456","hit":5}

SALT = 'eddie'

def get_md5(parms,salt):
    sorted_parm = sorted(parms.items())
    temp=''
    for (k,v) in sorted_parm:
        temp+=str(v)
    temp+=salt
    print(temp)
    m5 = hashlib.md5()
    m5.update(temp.encode(encoding='utf-8'))
    return m5.hexdigest()

print(get_md5(parm_dict,SALT))