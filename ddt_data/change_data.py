#公共域名及端口
host='http://192.168.1.88'
port=':8683'

#数据库mysql
mysql_host='192.168.1.171'
mysql_user='root'
mysql_passwd='123456'
mysql_db='zoo'

#question_delete插入语句
que_num="6"
question_delete_sql="insert into zoo_question(id,title,context,create_time,status) values ('6','问题6','context内容6','2019-04-23 17:06:40','11')"

#order_info接口插入的sql
order_info_num="147"
order_info_sql="insert  into `zoo_orders`(`id`,`order_item`,`pay_status`,`user_id`,`goods_id`,`goods_name`,`goods_url`,`buy_goods_num`,`goods_money`,`should_money`,`pay_money`,`freight`,`refund_money`,`refund_time`,`pay_type`,`pay_time`,`pay_call_back_time`,`pay_order_item`,`create_time`,`update_time`,`is_del`,`remark`) values (147,'4ebcadd9f75f427b9a2f09f474bf324e','21',7,3,'vip课程','http://pic31.nipic.com/20130804/7487939_090818211000_2.jpg',1,168.00,128.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2019-04-24 18:43:00','2019-04-24 18:43:00','11',NULL)"

#order_refund接口插入的sql
order_refund_num="146"
order_refund_sql="insert  into `zoo_orders`(`id`,`order_item`,`pay_status`,`user_id`,`goods_id`,`goods_name`,`goods_url`,`buy_goods_num`,`goods_money`,`should_money`,`pay_money`,`freight`,`refund_money`,`refund_time`,`pay_type`,`pay_time`,`pay_call_back_time`,`pay_order_item`,`create_time`,`update_time`,`is_del`,`remark`) values (146,'4ebcadd9f75f427b9a2f09f474bf324e','21',7,3,'vip课程','http://pic31.nipic.com/20130804/7487939_090818211000_2.jpg',1,168.00,128.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2019-04-24 18:43:00','2019-04-24 18:43:00','11',NULL)"
order_update_sql="UPDATE zoo_orders SET pay_status='21' WHERE id ='146'"
