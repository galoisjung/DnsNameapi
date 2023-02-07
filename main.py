import hashlib

from apidf import ApiDF
from apinhn import ApiNHN

nhn = ApiNHN()
df = ApiDF()

nhn_list = nhn.recordlist('t3q.ai.')

df_list= df.recordlist('t3q.ai')

nhn_hash_dict = {}
df_hash_dict = {}

for i in nhn_list:
    hash = hashlib.sha1(i.__repr__().encode('utf-8')).hexdigest()
    nhn_hash_dict[i.name] = hash

for i in df_list:
    id = i.id
    i.id = ''
    hash = hashlib.sha1(i.__repr__().encode('utf-8')).hexdigest()
    df_hash_dict[i.name] = [hash, id]
    i.id = id

cnt = 0

while len(nhn_hash_dict.keys()) != 0:
    temp = nhn_hash_dict.popitem()

    if temp[0] not in df_hash_dict.keys():
        df.createrecord('t3q.ai', nhn_list[cnt])
    else:
        df_hash_list = [i[0] for i in df_hash_dict.values()]
        if temp[1] not in df_hash_list:
            id = df_hash_dict[temp[0]][1]
            df.updaterecord('t3q.ai', nhn_list[cnt], id)

    cnt += 1

#
# while len(nhn_hash_dict.keys()) != 0:
#     temp = nhn_hash_dict.popitem()
#
#     df_hash_list = [i[0] for i in df_hash_dict.values()]
#
#     if temp[1] not in df_hash_list:
#         if temp[0] not in df_hash_dict.keys():
#             df.createrecord('t3q.ai', nhn_list[cnt])
#         else:
#             df.updaterecord('t3q.ai', nhn_list[cnt])
#     else:
#         del df_hash_dict[temp[0]]
#     cnt += 1
#
