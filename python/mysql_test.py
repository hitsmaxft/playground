#!/usr/bin/env python2

import _mysql
host_name='localhost'
user='root'
passwd='hits@data'
db_name='db_test11'

#sql ="""update `merchandises`,`promotion` set `merchandises`.`promotion_scale`=`promotion`.`discount_price` wherselecte `promotion`.`status`=1 and merchandises.id=promotion.goods_id """

sql=""" SELECT id,email FROM users """
con=_mysql.connect(
        host_name,user,passwd,db_name
        )
con.query(sql)

r=con.store_result()
if(r):
    print "effected rows :%d " %r.num_rows(),
    record=r.fetch_row()
    while(record):
        print record,"\n"
        record=r.fetch_row()
con.close()
