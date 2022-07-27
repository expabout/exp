from Crypto.Hash import SHA256
import random
chain={}
def gcd(a,b):
    while a!=0:
        a,b=b%a,a
    return b
def findModReverse(a,m):
    if gcd(a,m)!=1:
        return None
    u1,u2,u3=1,0,a
    v1,v2,v3=0,1,m
    while v3!=0:
        q=u3//v3
        v1,v2,v3,u1,u2,u3=(u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
    return u1%m
def sig_RSA(p,q,d,m):
    n=p*q
    sig=pow(m,d,n)
    return sig
def hash(info):
    h = SHA256.new()
    h.update(info.encode('utf-8'))
    return h.hexdigest()
def Moe():
    p=76519
    q=56123
    e=5
    d=findModReverse(e,(p-1)*(q-1))
    dict={}
    dict['cn_id']='lxp'
    dict['grade']='425'
    dict['year']='2022'
    dict['sig']=sig_RSA(p,q,d,int(dict['grade'])) 
    r=random.randint(1,10)
    info=dict['cn_id']+dict['grade']+dict['year']+str(dict['sig'])+str(r)
    commit=hash(info)
    chain[dict['cn_id']]=commit
    return dict
def check(sig):
    p=76519
    q=56123
    e=5
    n=p*q
    if pow(sig,e,n)>=425:
        return True
    else:
        return False
def employer(id,sig):
    if id not in chain.keys():
        return False
    elif check(sig)==False:
        return False
    else:
        return True
dict=Moe()
if employer(dict['cn_id'],dict['sig']):
    print('pass')
else:
    print('fail')