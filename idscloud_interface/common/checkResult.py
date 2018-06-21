import unittest
from common.Log import Log
log=Log()
class checkResult(unittest.TestCase):
    def ck(self,caseId,caseName,assertKey,assertValue,params,url,re):
        if re.status_code == 200:
            try:
                return_json = re.json()
                code = return_json[assertKey]
            except Exception as e:
                log.error(e)
                self.assertEqual(1,2,msg=re.text)

            if re.json():
                if code == str(assertValue):
                    msg = "(%s):(%s)：成功！返回信息：[%s]" % (caseId, caseName, re.json())
                else:
                    msg = "(%s):(%s)：失败！返回信息：[%s]" % (caseId, caseName, re.json())

                log.build_case_line(url, str(params), str(re.json()))
                self.assertEqual(code, str(assertValue), msg=msg)

        else:
            log.error("地址%s的Status Code:%s" % (url, re.status_code))
            self.assertEqual(re.status_code, 200)
