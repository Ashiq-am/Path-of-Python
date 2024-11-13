#!/usr/bin/python

import psycopg2
from config import config


def insert_student(student_name):
	""" insert a new vendor into the vendors table """
	sql = """INSERT INTO students(student_name),VALUES(%s) RETURNING student_id"""
	conn = None
	student_id = None
	try:
		# read database configuration
		params = config()
		# connect to the PostgreSQL database
		conn = psycopg2.connect(**params)
		# create a new cursor
		cur = conn.cursor()
		# execute the INSERT statement
		cur.execute(sql, (student_name,))
		# get the generated id back
		student_id = cur.fetchone()[0]
		# commit the changes to the database
		conn.commit()
		# close communication with the database
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

	return student_id
