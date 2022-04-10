# -*- coding: utf-8 -*-

from config import mysql_config
from flask import Flask,render_template, Response, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
import urllib.request
import urllib.parse
import json
import re
import hashlib
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')




# app.config.from_object(config)
# db = SQLAlchemy(app)
# 功能函数
def sql_result(dataset_name):
    conn = pymysql.connect(**mysql_config)
    conn.autocommit(1)
    conn.select_db('ecnugis_dataset')
    cursor = conn.cursor()

    cursor.execute('select a.dataset_name,a.data_name,(select count(*) from downrecord b where b.dataname=a.data_name) down_count, c.resolution,c.describe,c.date_b_e,c.projection from dataset a , data_description c  where a.dataset_name = c.dataset_name and a.dataset_name = "%s"' % dataset_name)
    #cursor.execute('SELECT * FROM dataset WHERE dataset_name= "%s"' % dataset_name)
    # print('total records:', cursor.rowcount)
    result = cursor.fetchall()
    conn.close()
    return result

def crossDomainResponse(data):
    response = Response(data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


# 获取所有数据
@app.route('/get_alldata/', methods=["POST", "GET"])
def get_alldata():
    # 默认返回内容
    return_dict = {'code': '200', 'msg': '处理成功', 'result': False}
    conn = pymysql.connect(**mysql_config)
    conn.autocommit(1)
    conn.select_db('ecnugis_dataset')
    cursor = conn.cursor()
    #sql = 'select a.dataset_name,a.data_name,(select count(*) from downrecord b where b.dataname=a.data_name) down_count from dataset a '
    sql = 'select a.dataset_name,a.data_name,(select count(*) from downrecord b where b.dataname=a.data_name) down_count, c.resolution,c.describe,c.date_b_e,c.projection from dataset a , data_description c where a.dataset_name = c.dataset_name ORDER BY dataset_name'
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    # 对参数进行操作
    return_dict['result'] = result

    return crossDomainResponse(json.dumps(return_dict, ensure_ascii=False))

# 获取数据集信息
@app.route('/get_describe/', methods=["POST", "GET"])
def get_describe():
    # 默认返回内容
    return_dict = {'code': '200', 'msg': '处理成功', 'result': False}
    # 获取传入的参数
    get_data = request.form.to_dict()
    dataset_name = get_data.get('dataset_name')
    conn = pymysql.connect(**mysql_config)
    conn.autocommit(1)
    conn.select_db('ecnugis_dataset')
    cursor = conn.cursor()
    sql = 'select * from data_description  where dataset_name = "%s"' % dataset_name
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    # 对参数进行操作
    return_dict['result'] = result

    return crossDomainResponse(json.dumps(return_dict, ensure_ascii=False))


# 获取数据
@app.route('/get_data/', methods=["POST", "GET"])
def get_data():
    # 默认返回内容
    return_dict = {'code': '200', 'msg': '处理成功', 'result': False}
    # 获取传入的参数
    get_data = request.form.to_dict()
    dataset_name = get_data.get('dataset_name')
    # 判断入参是否为空
    if dataset_name is None:
        return_dict['return_code'] = '504'
        return_dict['return_info'] = '请求参数为空'
        return crossDomainResponse(json.dumps(return_dict, ensure_ascii=False))
    # 对参数进行操作
    return_dict['result'] = sql_result(dataset_name)

    return crossDomainResponse(json.dumps(return_dict, ensure_ascii=False))


# 更新下载记录
@app.route('/down_record/', methods=["POST", "GET"])
def down_record():
    # 默认返回内容
    return_dict = {'code': '200', 'msg': '处理成功', 'result': False}

    # 获取传入的参数
    get_data = request.form.to_dict()
    dataset_name = get_data.get('dataset_name')
    data_name = get_data.get('data_name')
    user_name = get_data.get('user_name')
    user_email = get_data.get('user_email')
    user_company = get_data.get('user_company')
    user_used = get_data.get('user_used')

    # 判断入参是否为空
    if dataset_name is None:
        return_dict['return_code'] = '504'
        return_dict['return_info'] = '请求参数为空'
        return crossDomainResponse(json.dumps(return_dict, ensure_ascii=False))

    conn = pymysql.connect(**mysql_config)
    conn.select_db('ecnugis_dataset')
    cursor = conn.cursor()
    sql = 'insert into downrecord (username, useremail, usercompany, userused, datasetname, dataname) values ("%s", "%s", "%s", "%s", "%s", "%s") ' % (user_name, user_email, user_company, user_used, dataset_name, data_name)
    try:
        # 执行sql语句
        print(sql)
        cursor.execute(sql)
        conn.commit()
        return_dict['result'] = 'insert ok'
    except:
        # 发生错误时回滚
        conn.rollback()
        return_dict['result'] = 'error'
    # 关闭数据库连接
    conn.close()
    return crossDomainResponse(json.dumps(return_dict, ensure_ascii=False))
# 注册
@app.route('/register/', methods=["POST", "GET"])
def register():
    return_dict = {'code': '200', 'msg': '接收成功', 'result': False}
    conn = pymysql.connect(**mysql_config)
    conn.select_db('ecnugis_dataset')
    cursor = conn.cursor()
    # 获取传入的参数
    get_data = request.form.to_dict()
    telephone = get_data.get('telephone')
    username = get_data.get('name')
    title = get_data.get('title')
    duty = get_data.get('duty')
    password = get_data.get('password')
    major = get_data.get('major')
    email = get_data.get('email')
    organization = get_data.get('organization')
    direction = get_data.get('direction')
    # 1.用正则检验用户输入是否合法
    if not (re.match('1[3-8][0-9]{9}$', telephone) and re.match('\w{6,12}$', password)):

        return_dict['result'] = '请输入正确的手机号码或密码'
        return crossDomainResponse(json.dumps(return_dict, ensure_ascii=False))
    # 2.查询数据库中手机号是否已经被注册
    sql = 'select telephone from user_info where telephone = "{}"'.format(telephone)
    print(sql)
    cursor.execute(sql)
    if cursor.rowcount:
        print('该手机号已注册！')
        return_dict['result'] = '该手机号已注册'
        return crossDomainResponse(json.dumps(return_dict, ensure_ascii=False))
    # md5加密
    print(password)
    md5 = hashlib.md5()
    md5.update(password.encode('utf8'))
    password = md5.hexdigest()
    print(password)
    try:
        sql = 'insert into user_info(telephone,username,title,duty,password,major,email,organization,direction)' \
              ' values("{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(telephone, username, title, duty, password, major, email, organization, direction)
        print(sql)
        cursor.execute(sql)
        conn.commit()
        print("注册成功")
        return_dict['result'] = '注册成功'
    except:
        print('注册失败！')
        return_dict['result'] = '注册失败'
    finally:
        # 关闭游标
        conn.close()
    return crossDomainResponse(json.dumps(return_dict, ensure_ascii=False))

# 登录
@app.route('/login/', methods=["POST", "GET"])
def login():
    return_dict = {'code': '200', 'msg': '接收成功', 'result': False}
    conn = pymysql.connect(**mysql_config)
    conn.select_db('ecnugis_dataset')
    cursor = conn.cursor()
    # 获取用户名和密码
    get_data = request.form.to_dict()
    telephone = get_data.get('telephone')
    password = get_data.get('password')
    sql = 'select telephone,password,username from user_info where telephone = "{}"'.format(telephone)
    cursor.execute(sql)
    if not cursor.rowcount:
        print("用户不存在")
        return_dict['result'] = '用户不存在'
        return crossDomainResponse(json.dumps(return_dict, ensure_ascii=False))
    result = cursor.fetchone()
    md5 = hashlib.md5()
    md5.update(password.encode("utf-8"))
    password = md5.hexdigest()
    print(result)
    print(password)
    if result['password'] != password:
        print("请输入正确的密码")
        return_dict['result'] = '请输入正确的密码'
        return crossDomainResponse(json.dumps(return_dict, ensure_ascii=False))
    return_dict['result'] = '登录成功'
    return_dict['username'] = result['username']
    return crossDomainResponse(json.dumps(return_dict, ensure_ascii=False))

# 注册
@app.route('/cy_register/', methods=["POST", "GET"])
def cy_register():
    print("sdfhjsdfhjsadvfhv")
    return_dict = {'code': '200', 'msg': '接收成功', 'result': False}
    conn = pymysql.connect(**mysql_config)
    conn.select_db('laozi')
    cursor = conn.cursor()
    # 获取传入的参数
    get_data = request.form.to_dict()
    Username = get_data.get('Username')
    Organization = get_data.get('Organization')
    Career = get_data.get('Career')
    Email = get_data.get('Email')
    Password = get_data.get('Password')
    Information_type = get_data.get('Information_type')
    Information_description = get_data.get('Information_description')
    Address = get_data.get('Address')
    Time = get_data.get('Time')
    Upload = get_data.get('Upload')
    People= get_data.get('People')
    
    # 1.查询数据库中用户名是否已经被注册
    sql = 'select Username from user_info where Username = "{}"'.format(
        Username)
    print(sql)
    # cursor.execute(sql)
    # if cursor.rowcount:
    #     print('该用户名已注册！')
    #     return_dict['result'] = '该用户名已注册'
    #     return crossDomainResponse(json.dumps(return_dict, ensure_ascii=False))
    # # md5加密
    # print(password)
    # md5 = hashlib.md5()
    # md5.update(password.encode('utf8'))
    # password = md5.hexdigest()
    # print(password)
    # try:
    #     sql = 'insert into user_info(telephone,username,title,duty,password,major,email,organization,direction)' \
    #           ' values("{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(
    #               telephone, username, title, duty, password, major, email, organization, direction)
    #     print(sql)
    #     cursor.execute(sql)
    #     conn.commit()
    #     print("注册成功")
    #     return_dict['result'] = '注册成功'
    # except:
    #     print('注册失败！')
    #     return_dict['result'] = '注册失败'
    # finally:
    #     # 关闭游标
    #     conn.close()
    return crossDomainResponse(json.dumps(return_dict, ensure_ascii=False))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
    #app.run(host='0.0.0.0', port=8082, ssl_context=('D:/Download/scs1595384957755/Nginx/server.crt', 'D:/Download/scs1595384957755/Nginx/server.key'))

