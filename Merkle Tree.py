import hashlib
import random
import math
def build(node_num):                     
    if node_num & (node_num - 1) == 0:  
        depth = int(math.log(node_num, 2)) + 1
    else:
        depth = int(math.log(node_num, 2)) + 2
    k = depth
    tree = [None] * k
    leaf = [None] * node_num
    data_block = [None] * node_num
    t = 'lixiping202000460017'
    tree[k - 1] = data_block
    k = k - 2
    for i in range(node_num): 
        for j in range(10):
            t += random.choice('qwertyuiopasdfghjklzxcvbnm')
        leaf[i] = t
        data_block[i] = hash('00' + t)
    return k,depth,tree,leaf,data_block
def hash(data):             
    obj = hashlib.sha256()
    obj.update(data.encode('utf-8'))
    return obj.hexdigest()
def create(node_list):
    l = len(node_list)
    if l == 1: 
        return node_list[0]        
    new_node_list = []
    for i in range(0, l-1, 2):  
        new_node_list.append(hash('01' + node_list[i] + node_list[i+1]))
    if l % 2 == 1:
        new_node_list.append(node_list[l-1])
    return create(new_node_list)


k,depth,tree,leaf,data_block = build(100000)
root = create(data_block)
hash_index = []
direction  = []


def path(m,node_num):
    global hash_index
    global data_block
    if node_num == 1:
        hash_index.append(data_block[0])
        return 0
    if node_num & (node_num - 1) == 0:
        p = 2 ** (int(math.log(node_num, 2))-1)
    else:
        p = 2 ** int(math.log(node_num, 2))
    if m < p:
        hash_index.append(create(data_block[p:node_num]))
        data_block = data_block[0:p]
        new_m = m
        new_node_num = p
        direction.append(1)
    else:
        hash_index.append(create(data_block[0:p]))
        data_block = data_block[p:node_num]
        new_m = m - p
        new_node_num = node_num - p
        direction.append(2)
    return path(new_m,new_node_num)
def cal():
    l = len(hash_index)
    if l == 1:
        return hash_index[0]
    if direction[l-2] == 1:
        hash_index[l-2] = hash('01' + hash_index[l-1] + hash_index[l-2])
    else:
        hash_index[l-2] = hash('01' + hash_index[l - 2] + hash_index[l - 1])
    hash_index.pop()
    direction.pop()
    return cal()
def existence(m,node_num):
    path(m, node_num)
    print('给定数据为：',leaf[m])
    a = cal()
    if root == a:
        print('该叶子结点存在')
        return
    else:
        print('该叶子结点不存在')
        return
existence(4,1000)