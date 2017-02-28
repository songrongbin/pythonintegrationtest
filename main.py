# create by andybin
import json
import urllib
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

COMM_QUERY_PLUS = 'userId=0&clientOs=1&clientOsVersion=4.3&appType=1&appVersion=1.0&phoneType=GomeplusBSMonitor&' \
                  'ip=192.12.33.22&mac=ac+as+23+3d&netType=4G&devId=IPhone1234567890&' \
                  'otherDevInfo=someInfo&loginToken=&pageNum=1&numPerPage=10&lastRecordId=1000001'
USER_QUERY_PLUS = 'userId={userid}&clientOs=1&clientOsVersion=4.3&app=1&appVersion=1.0&' \
                  'phoneType=GomeplusBSMonitor&ip=192.12.33.22&mac=ac+as+23+3d&netType=4G&devId=IPhone1234567890&' \
                  'otherDevInfo=someInfo&loginToken={token}&pageNum=1&numPerPage=10&lastRecordId=1000001'

def dump(o, asc=False):
    print json.dumps(o, indent=4, sort_keys=True, ensure_ascii=asc, encoding='utf-8')

class Requester:

    def __init__(self, host=None, user=None, pwd=None):
        self.host = host or 'api-bs.gomeplus.com'
        self.user_query_plus = None
        self.verify = True
        self.userId = None
        self.token = None
        #self.login()

    def url(self, base):
        return 'http://api.bs.pre.gomeplus.com/v2/{base}'.format(base=base)

    def login(self):
        url = 'http://api.bs.pre.gomeplus.com/v2/user/login?app=001/2&device=1/1/1/009&pubPlat=001&ip=127.0.0.1'
        payload = {'loginName': '18629437310', 'password': '123.gome'}
        headers = {'content-type': 'application/json;charset=UTF-8', 'Accept': 'application/json'}
        o = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
        asc = False
        print o.json()
        result = o.json()

        print(result['data']['user']['id']);
        print(result['data']['loginToken']);
        self.userId = result['data']['user']['id']
        self.token = result['data']['loginToken']
        self.user_query_plus = USER_QUERY_PLUS.format(userid=result['data']['user']['id'], token=result['data']['loginToken'])
        print self.user_query_plus
        return result['data']['loginToken']

    def println(self, param):
        print(param)

    def getUserQueryPlus(self):
        print self.user_query_plus
        return self.user_query_plus

    def user_get(self, base, args):
        print self.url(base) + args
        r = requests.get(self.url(base) + args, verify=self.verify)
        return r.json()


    def u_get_shippingCart(self, orderTester):
        o = self.user_get('trade/shoppingCart?', self.getUserQueryPlus())
        return self.ret(o, lambda: True)

    def u_update_shippingCart(self, orderTester):
        url = 'https://api.bs.pre.gomeplus.com/v2/trade/shoppingCartItem?userId=1521'
        payload = {"mshopId": 509, "kid": "1", "skuId": 9627, "quantity": 1,"sourceCode": "{\"sourceCode\":\"1234567890123456\",\"activityNo\":\"12345678\"}"}
        headers = {'content-type': 'application/json;charset=UTF-8', 'Accept': 'application/json', 'x-gomeplus-login-token': self.token, 'x-gomeplus-app': self.userId}
        o = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
        asc = False
        print o.json()

    def u_get_order_info(self, orderTester):
        o = self.user_get('trade/shoppingCart?', self.getUserQueryPlus())
        return self.ret(o, lambda: True)

    def ret(self, o, expr):
        success = False
        try:
            success = o['success'] and expr()
        except Exception as e:
            pass

        if not success:
            dump(o)

        return success

