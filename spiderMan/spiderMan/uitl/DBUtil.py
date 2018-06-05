#!/usr/bin/python
# -*- coding: UTF-8 -*-
#desc�������ݿ����ӳز������ݿ�
#author��lijin

import MySQLdb
from DBUtils.PooledDB import PooledDB


class DBUtil:

	#���ݿ�����
	db_conn=null
	#���ݿ��α�
	db_cur=null
	#���ݿ��ַ
	db_host=""
	#���ݿ�˿�
	db_port=""
	#���ݿ�����
	db_username=""
	#���ݿ�����
	db_pwd=""
	#���ݿ�����
	db_name=""
	#���ݿ����ӳ�����
	#mincached : ����ʱ�����Ŀ���������(ȱʡֵ 0 ��ζ�ſ�ʼʱ����������)
	mincached=2
	#maxcached: ���ӳ�ʹ�õ������������(ȱʡֵ 0 �����������ӳش�С)
	maxcached=10
	#maxshared: �������Ĺ�����������(ȱʡֵ 0 �����������Ӷ���ר�õ�)����ﵽ�����������������Ϊ��������ӽ��ᱻ����ʹ�á�
	maxshared=0
	#maxconnections: ���������������(ȱʡֵ 0 ��������)
	maxconnections=0
	#blocking: �����ڴﵽ�������ʱ����Ϊ(ȱʡֵ 0 �� False ������һ������������������ֱ������������)
	blocking=0
	#maxusage: �������ӵ���������ô���(ȱʡֵ 0 �� False �������Ƶĸ���)�����ﵽ�����ֵʱ�����ӻ��Զ���������(�رպ����´�)
	maxusage=False
	#setsession: һ����ѡ��SQL�����б�����׼��ÿ���Ự���� ["set datestyle to german", ...]
	
	
	def __init__(self,db_host,db_port,db_username,db_pwd,db_name):
		#����mysql ���ݿ�
		print db_host+"-"+db_port+"-"+db_username+"-"+db_username+"-"+db_username
		self.db_host=db_host
		self.db_port=db_port
		self.db_username=db_username
		self.db_pwd=db_pwd
		self.db_name=db_name
		
	#��ȡ���ݿ����ӳ�����
	def _getConniction(self):
		if self.db_conn==null:
			try:
				self.db_conn = PooledDB(creator=pymysql,mincached=self.mincached, maxcached=self.maxcached,maxshared=self.maxshared, maxconnections=self.maxconnections, blocking=self.blocking,host=self.db_host,port=self.db_port,user=self.db_username,password=self.db_pwd,database =self.db_name,charset="utf8").connection()
				self.db_cur=self.db_conn.cursor()
			 except Exception, e:
				print "���ӳػ�ȡ����ʧ��"
		else:
			return self.db_cur
	
	
	
	#�ر����ݿ����ӳ�����
	def _closeConnection(self):
		if db_conn!=null:
			try��
				self.conn.close()
				self.db_cur.close()
				print "�����Ѿ��ɹ��ر�"
			except Exception,e:
				print "���ӹر�ʧ��"
	
	
	
	#sql��ȡ����
	def _getDataList(self,sqlStr):
		cur=self._getConniction()
		cur.execute(sqlStr)
        relist=cur.fetchall()
        self._closeConnection()
        return relist
		
	#sqlִ�и���update����delete
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
	
	