import json
from common import Case
from common.get_csv import *
path=Propath()
source=open(path+"/testFile/isv4.0.txt","r").readline()
csvfile = open(path+'/testFile/isv/isv.csv', 'w',newline ='')
writer = csv.writer(csvfile)
writer.writerow(["接口标识","接口名称","接口地址","接口请求方式", "接口参数"])
if source.startswith(u'\ufeff'):
    source = source.encode('utf8')[3:].decode('utf8')
jsonObject=json.loads(source)
paths=jsonObject["paths"]

for key in paths:
    # interfaceAddress ='http://'+ jsonObject['host']+jsonObject['basePath']+key
    interfaceAddress = 'https://' + 'service.bccastle.com' + jsonObject['basePath'] + key
    interfaceName = ""
    operationId = ""
    methond = ""
    param = []
    responseValue = ""
    methondItim=paths[key]
    for itimkey in methondItim:
        methond=itimkey
        interfaceName=methondItim[methond]["summary"]
        operationId=methondItim[methond]["operationId"]
        if("parameters" in methondItim[methond].keys()):
            parameterList=methondItim[methond]["parameters"]
            for pa in parameterList:
                if pa["in"] == "body":
                    try:
                        body = pa["schema"]["$ref"].split('/')
                        pas = jsonObject[body[1]][body[2]]["properties"].keys()
                        param.extend(pas)
                    except Exception as e:
                        param.append('error...')
                    # param.extend(pas)
                else:
                    param.append(pa["name"])
        writer.writerow([operationId,interfaceName , interfaceAddress, methond,param ])
        # Case.caseScript(path+'/testCase/eps/test_'+ operationId+'.py',operationId,interfaceName,methond,'eps')
        # Case.datacsv(path+'/testFile/user/'+interfaceName+'.csv',param)
csvfile.close()






