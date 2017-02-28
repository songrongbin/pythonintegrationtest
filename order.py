# vim: fileencoding=utf-8 ts=4 sw=4 sts=4 et

import sys
import urllib

from main import Requester

reload(sys)
sys.setdefaultencoding('utf-8')

class OrderTester():
    USER_QUERY_PLUS = 'userId={userid}&clientOs=1&clientOsVersion=4.3&appType=1&appVersion=1.0&' \
                      'phoneType=GomeplusBSMonitor&ip=192.12.33.22&mac=ac+as+23+3d&netType=4G&devId=IPhone1234567890&' \
                      'otherDevInfo=someInfo&loginToken={token}&pageNum=1&numPerPage=10&lastRecordId=1000001'

    def u_get_shopcart_list(self):
        #requester = Requester(host='api.bs.dev.gomeplus.com', user='18629437310', pwd='123.gome')
        o = self.user_get('trade/shoppingCart?', self.getUserQueryPlus())
        return self.ret(o, lambda: True)

    def u_get_buyerorder_list(self):
        o = self.user_get('trade/buyerOrders?')
        return self.ret(o, lambda: True)

order_cases = [
    ('v2/trade/shoppingCart',    u'获取购物车列表'),
    ('v2/trade/buyerOrders', u'获取买家订单列表'),
]