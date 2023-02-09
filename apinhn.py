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
        query = {'limit': '3000'}
        cnt = 1
        dto_list = []
        while True:
            query['page'] = cnt
            zone_row_result = requests.get(config.NHN_RECORD.format(config.NHN_APIKEY, self.zoneInfo[zone]),
                                           headers=config.HEADER,
                                           params=query)
            zone_row_dict = json.loads(zone_row_result.text)

            result = zone_row_dict['recordsetList']

            if len(result) == 0:
                break

            for i in result:
                replace = i['recordsetName'].split(".")
                zone_cnt = len(config.NHN_ZONE_NAME.split("."))

                name = ".".join(replace[:-zone_cnt])
                if len(name) != 0:
                    dto_list.append(Record(type=i['recordsetType'],
                                           name=name,
                                           content=i['recordList'][0]['recordContent'],
                                           ttl=i['recordsetTtl']
                                           ))
            cnt = cnt + 1

        return dto_list
