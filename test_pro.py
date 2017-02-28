import datetime
import sys
import traceback
import urllib


from order import OrderTester
from main import Requester

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    req = Requester(host='api.bs.dev.gomeplus.com', user='18629437310', pwd='123.gome')
    token = req.login()
    req.println(token)
    tester = OrderTester();
    req.u_get_shippingCart(tester)
    req.u_update_shippingCart(tester)
