# vim: fileencoding=utf-8 ts=4 sw=4 sts=4 et

import json
import urllib
import requests
import sys



reload(sys)
sys.setdefaultencoding('utf-8')

if sys.version_info[1] < 7:
    sys.stderr = open('/dev/null', 'w')
else:
    requests.packages.urllib3.disable_warnings()

COMM_QUERY_PLUS = 'userId=0&clientOs=1&clientOsVersion=4.3&appType=1&appVersion=1.0&phoneType=GomeplusBSMonitor&' \
                  'ip=192.12.33.22&mac=ac+as+23+3d&netType=4G&devId=IPhone1234567890&' \
                  'otherDevInfo=someInfo&loginToken=&pageNum=1&numPerPage=10&lastRecordId=1000001'
USER_QUERY_PLUS = 'userId={userid}&clientOs=1&clientOsVersion=4.3&appType=1&appVersion=1.0&' \
                  'phoneType=GomeplusBSMonitor&ip=192.12.33.22&mac=ac+as+23+3d&netType=4G&devId=IPhone1234567890&' \
                  'otherDevInfo=someInfo&loginToken={token}&pageNum=1&numPerPage=10&lastRecordId=1000001'


def dump(o, asc=False):
    print json.dumps(o, indent=4, sort_keys=True, ensure_ascii=asc, encoding='utf-8')


class Requester:
    def __init__(self, host=None, user=None, pwd=None):
        self.verify = (host is None)
        self.host = host or 'api-bs.gomeplus.com'
        self.user = user
        self.pwd = pwd
        self.user_query_plus = None

    def url(self, base, **kwargs):
        return 'https://{host}/api/{base}'.format(host=self.host, base=base).format(**kwargs)

    def get(self, base, **kwargs):
        return requests.get(self.url(base, **kwargs), verify=self.verify)

    def comm_get(self, base, **kwargs):
        r = requests.get(self.url(base, **kwargs) + COMM_QUERY_PLUS, verify=self.verify)
        return r.json()

    def user_get(self, base, **kwargs):
        r = requests.get(self.url(base, **kwargs) + self.user_query_plus, verify=self.verify)
        return r.json()

    def login(self):
        ep = self.get('dsp/get_encrypt_password.json?password={pwd}', pwd=self.pwd).text

        o = self.comm_get('user/login.json?loginName={user}&password={ep}&verifyCode=1&', user=self.user,
                          ep=urllib.quote(ep))
        dump(o)
        self.user_query_plus = USER_QUERY_PLUS.format(userid=o['data']['userId'], token=o['data']['token'])
        return o


class TesterBase:
    def __init__(self, test_cfg, req):
        self.cfg = test_cfg
        self.req = req
        self.env = test_cfg['name']
        self.sms_send = test_cfg['sms_send']
        self.comm_get = req.comm_get
        self.user_get = req.user_get

    def login(self):
        o = self.req.login()
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