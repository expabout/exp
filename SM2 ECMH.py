from ECMH import MultiHash

set1 = (b'lixp',)
set3 = (b'lixp', b'0017')
set4 = (b'0017', b'lixp')
set2 = (b'lixp',b'lixp')
result1 = MultiHash(set1)
result2 = MultiHash(set2)
result3 = MultiHash(set3)
result4 = MultiHash(set4)
print("hash(set1) = ", result1)
print("hash(set2) = ", result2)
print("hash(set3) = ", result3)
print("hash(set4) = ", result4)