import json
import requests

import config
from DTO import Record


class ApiDF:

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
        query = {'per_page': '5000'}  # 버그의 원인이 될지도?
        zone_row_result = requests.get(config.CF_RECORD.format(self.zoneInfo[zone]), headers=config.CF_HEADER,
                                       params=query)
        zone_row_list = json.loads(zone_row_result.text)

        result = zone_row_list['result']

        dto_list = [Record(type=i['type'],
                           name=i['name'],
                           content=i['content'],
                           ttl=i['ttl'],
                           id=i['id']
                           ) for i in result]
        return dto_list

    def createrecord(self, zone, record):
        data = {
            'type': record.type,
            'name': record.name,
            'content': record.content,
            'ttl': record.ttl
        }

        print(data)
        res = requests.post(config.CF_RECORD.format(self.zoneInfo[zone]), headers=config.CF_HEADER,
                            data=json.dumps(data))

        print(res.text)
