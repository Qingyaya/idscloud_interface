# /user/bin/python3
# -*- coding : utf-8 -*-
# @Auther : Dong
# @Time : 2018/7/4 10:58
import pymysql
from common.ReadConfig import ReadConfig

rc=ReadConfig()
db = pymysql.connect(rc.get_db('ip'), rc.get_db('username'), rc.get_db('password'), rc.get_db('db'))
cursor = db.cursor()
sqls = """
delete from tb_role  where role_name in ('apitest','apitest1');
delete from tb_sps where sp_code in ('Oauth','apitest01');
delete from ids_service_company_middle where companytype= 1 or name='';
DELETE FROM ids_org_relation;
delete from ids_service_company where name='apitestopSS1';
delete from sorg where sorg_name='testGG';
"""

for sql in sqls.strip().split(";"):
    if sql:
        cursor.execute(sql)
        db.commit()
db.close()