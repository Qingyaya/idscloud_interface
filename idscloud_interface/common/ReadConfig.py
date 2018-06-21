import os
import codecs
import configparser
from  common import get_csv

class ReadConfig:
    def __init__(self):
        proDir = get_csv.Propath()
        self.configPath = os.path.join(proDir, "config\\config.ini")
        fd = open(self.configPath)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(self.configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(self.configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_headers(self, name):
        value = self.cf.get("HEADERS", name)
        return value

    def set_headers(self, name, value):
        self.cf.set("HEADERS", name, value)
        with open(self.configPath, 'w+') as f:
            self.cf.write(f)

    def get_url(self, name):
        value = self.cf.get("URL", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

    def get_casepackage(self,name):
        value=self.cf.get('CASEPACKAGE',name)
        return value


if __name__ == '__main__':
    # sender=ReadConfig.get_email('sender')
    # email=ReadConfig.get_email('sender')
    re=ReadConfig()
    psw=re.get_email('psw')
