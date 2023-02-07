import requests
import json
import config
from DTO import Record


class ApiNHN:

    def __init__(self):
        self.apikey = config.NHN_APIKEY
        result = requests.get(config.NHN_ZONE, headers=config.HEADER)
        if result.status_code == 200:
            dict_resp_result = json.loads(result.text)
            dict_zone_result = dict_resp_result["zoneList"]

            result_zoneinfo = dict()
            for i in dict_zone_result:
                result_zoneinfo[i['zoneName']] = i['zoneId']
            self.zoneInfo = result_zoneinfo
        else:
            raise Exception('api를 가져올 수 없습니다.')

    def recordlist(self, zone):
        query = {'limit': '3000'}  # 버그의 원인이 될지도?
        zone_row_result = requests.get(config.NHN_RECORD.format(self.zoneInfo[zone]), headers=config.HEADER,
                                       params=query)
        zone_row_dict = json.loads(zone_row_result.text)

        result = zone_row_dict['recordsetList']

        dto_list = [Record(type=i['recordsetType'],
                           name=i['recordsetName'][:-1],
                           content=i['recordList'][0]['recordContent'],
                           ttl=i['recordsetTtl']) for i in result]

        return dto_list
