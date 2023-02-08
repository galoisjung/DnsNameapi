import hashlib

import config
from apidf import ApiDF
from apinhn import ApiNHN

nhn_zone_name = config.NHN_ZONE_NAME
cf_zone_name = config.CF_ZONE_NAME

nhn = ApiNHN()
cf = ApiDF()

nhn_list = nhn.recordlist(nhn_zone_name)

cf_list = cf.recordlist(cf_zone_name)

nhn_hash_dict = {}
df_hash_dict = {}

for j, i in enumerate(nhn_list):
    hash = hashlib.sha1(i.__repr__().encode('utf-8')).hexdigest()
    nhn_hash_dict[i.name] = [hash, j]

for i in cf_list:
    id = i.id
    i.id = ''
    hash = hashlib.sha1(i.__repr__().encode('utf-8')).hexdigest()
    df_hash_dict[i.name] = [hash, id]


while len(nhn_hash_dict.keys()) != 0:
    temp = nhn_hash_dict.popitem()

    if temp[0] not in df_hash_dict.keys():
        cf.createrecord(cf_zone_name, nhn_list[temp[1][1]])
    else:
        df_hash_list = [i[0] for i in df_hash_dict.values()]
        if temp[1][0] not in df_hash_list:
            id = df_hash_dict[temp[0]][1]
            print("test")
            print(nhn_list)
            cf.updaterecord(cf_zone_name, nhn_list[temp[1][1]], id)

        df_hash_dict.pop(temp[0], None)

while len(df_hash_dict.keys()) != 0:
    temp = df_hash_dict.popitem()
    cf.deleterecord(cf_zone_name, temp[1][1])
