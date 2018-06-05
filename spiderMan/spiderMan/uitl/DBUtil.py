#!/usr/bin/python
# -*- coding: UTF-8 -*-
#desc：从数据库链接池操作数据库
#author：lijin

import MySQLdb
from DBUtils.PooledDB import PooledDB


class DBUtil:

	#数据库链接
	db_conn=null
	#数据库游标
	db_cur=null
	#数据库地址
	db_host=""
	#数据库端口
	db_port=""
	#数据库用名
	db_username=""
	#数据库密码
	db_pwd=""
	#数据库名称
	db_name=""
	#数据库连接池配置
	#mincached : 启动时开启的空连接数量(缺省值 0 意味着开始时不创建连接)
	mincached=2
	#maxcached: 连接池使用的最多连接数量(缺省值 0 代表不限制连接池大小)
	maxcached=10
	#maxshared: 最大允许的共享连接数量(缺省值 0 代表所有连接都是专用的)如果达到了最大数量，被请求为共享的连接将会被共享使用。
	maxshared=0
	#maxconnections: 最大允许连接数量(缺省值 0 代表不限制)
	maxconnections=0
	#blocking: 设置在达到最大数量时的行为(缺省值 0 或 False 代表返回一个错误；其他代表阻塞直到连接数减少)
	blocking=0
	#maxusage: 单个连接的最大允许复用次数(缺省值 0 或 False 代表不限制的复用)。当达到最大数值时，连接会自动重新连接(关闭和重新打开)
	maxusage=False
	#setsession: 一个可选的SQL命令列表用于准备每个会话，如 ["set datestyle to german", ...]
	
	
	def __init__(self,db_host,db_port,db_username,db_pwd,db_name):
		#访问mysql 数据库
		print db_host+"-"+db_port+"-"+db_username+"-"+db_username+"-"+db_username
		self.db_host=db_host
		self.db_port=db_port
		self.db_username=db_username
		self.db_pwd=db_pwd
		self.db_name=db_name
		
	#获取数据库链接池链接
	def _getConniction(self):
		if self.db_conn==null:
			try:
				self.db_conn = PooledDB(creator=pymysql,mincached=self.mincached, maxcached=self.maxcached,maxshared=self.maxshared, maxconnections=self.maxconnections, blocking=self.blocking,host=self.db_host,port=self.db_port,user=self.db_username,password=self.db_pwd,database =self.db_name,charset="utf8").connection()
				self.db_cur=self.db_conn.cursor()
			 except Exception, e:
				print "链接池获取链接失败"
		else:
			return self.db_cur
	
	
	
	#关闭数据库链接池链接
	def _closeConnection(self):
		if db_conn!=null:
			try：
				self.conn.close()
				self.db_cur.close()
				print "链接已经成功关闭"
			except Exception,e:
				print "链接关闭失败"
	
	
	
	#sql获取数据
	def _getDataList(self,sqlStr):
		cur=self._getConniction()
		cur.execute(sqlStr)
        relist=cur.fetchall()
        self._closeConnection()
        return relist
		
	#sql执行更新update或者delete
	def _update(self,sqlStr):
		cur=self._getConniction()
        cur.execute(sqlStr)
        self.conn.commit()
        self._closeConnection()
	
	def _updateBatch(self,sqlStrs):
		cur=self._getConniction()
		for sqlStr in range(len(sqlStrs))
		cur.execute(sqlStr)
		self.conn.commit()
        self._closeConnection()
	
	def _batchSQL(self,sqlStrs):
		cur=self._getConniction()
		for sqlStr in range(len(sqlStrs))
		cur.execute(sqlStr)
		self.conn.commit()
        self._closeConnection()
	
	def _delete(self,sqlStr):
		cur=self._getConniction()
        cur.execute(sqlStr)
        self.conn.commit()
        self._closeConnection()
	
	def _deleteBatch(self,sqlStrs):
		cur=self._getConniction()
		for sqlStr in range(len(sqlStrs))
		cur.execute(sqlStr)
		self.conn.commit()
        self._closeConnection()
	
	