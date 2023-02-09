import json
import requests

import config
from DTO import Record


class ApiCF:

    def __init__(self):
        result = requests.get(config.CF_ZONE, headers=config.CF_HEADER)
        if result.status_code == 200:
            dict_resp_result = json.loads(result.text)
            dict_zone_result = dict_resp_result["result"]

            result_zoneinfo = dict()
            for i in dict_zone_result:
                result_zoneinfo[i['name']] = i['id']
            self.zoneInfo = result_zoneinfo
        else:
            raise Exception('api를 가져올 수 없습니다.')

    def recordlist(self, zone):
        query = {'per_page': '5000'}
        cnt = 1
        dto_list = []

        while True:
            query['page'] = cnt
            zone_row_result = requests.get(config.CF_RECORD.format(self.zoneInfo[zone], ""), headers=config.CF_HEADER,
                                           params=query)
            zone_row_list = json.loads(zone_row_result.text)

            result = zone_row_list['result']

            if len(result) == 0:
                break

            for i in result:
                replace = i['name'].split(".")
                zone_cnt = len(config.CF_ZONE_NAME.split("."))  # nhn은 .하나 더 붙어서 -1 제거해준다.

                name = ".".join(replace[:-zone_cnt])
                if len(name) != 0:
                    dto_list.append(Record(type=i['type'],
                                           name=name,
                                           content=i['content'],
                                           ttl=i['ttl'],
                                           id=i['id']
                                           ))
            cnt = cnt + 1

        return dto_list

    def createrecord(self, zone, record):
        data = {
            'type': record.type,
            'name': record.name,
            'content': record.content,
            'ttl': record.ttl
        }
        res = requests.post(config.CF_RECORD.format(self.zoneInfo[zone], ""), headers=config.CF_HEADER,
                            data=json.dumps(data))

        res_dict = json.loads(res.text)

        if not res_dict['success'] and res_dict['errors'][0]['code'] == 81045:
            raise Exception("Full of record")

        print(res.text)


    def updaterecord(self, zone, record, id):
        data = {
            'type': record.type,
            'name': record.name,
            'content': record.content,
            'ttl': record.ttl
        }
        res = requests.put(config.CF_RECORD.format(self.zoneInfo[zone], id), headers=config.CF_HEADER,
                       data=json.dumps(data))
        print(res.text)


    def deleterecord(self, zone, id):
        res = requests.delete(config.CF_RECORD.format(self.zoneInfo[zone], id), headers=config.CF_HEADER)

        print(res.text)
