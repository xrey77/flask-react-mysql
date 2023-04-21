import math
# import jwt
from flask import jsonify
from flask_restful import request, Resource
from db import db_connection
# from config import SECRET_KEY

class GetproductsHandler(Resource):  
  
  def count_Pages():

    conn = db_connection()
    cursor = conn.cursor()
    sql = """SELECT count(*) as 'page' FROM products"""
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

  def get(self):
    conn = db_connection()
    cursor = conn.cursor()
    totalpage=None
    page = request.args.get('page', type=int)

    # TOTAL RECORDS
    totalrecs = GetproductsHandler.count_Pages()
    perpage = 10

    # CALCULATE TOTAL PAGES
    totalpage = math.ceil(float(totalrecs['page']) / perpage)
    
    offset = (page - 1) * perpage

    sql = """SELECT * FROM products LIMIT %s OFFSET %s"""
    if(page == 1):
        page = 0

    prods=cursor.execute(sql, (int(perpage), int(offset)))
    if page == 0:
       page = 1

    results = cursor.fetchall()
    if (prods):
        return jsonify({'totpages': totalpage,'page': page, 'products': results})

       