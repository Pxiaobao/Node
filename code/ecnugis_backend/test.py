from flask import Flask, request
import json
import pymysql
from conf import config

app = Flask(__name__)


# 只接受get方法访问
@app.route("/select/salary/", methods=["GET"])
def check():
    # 默认返回内容
    return_dict = {'code': '200', 'msg': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '504'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的参数
    get_data = request.args.to_dict()
    Account = get_data.get('Account')
    # age = get_data.get('age')
    # 对参数进行操作
    return_dict['result'] = sql_result(Account)

    return json.dumps(return_dict, ensure_ascii=False)


# 功能函数
def sql_result(Account):
    conn = pymysql.connect(**config)
    conn.autocommit(1)
    conn.select_db('test')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test.user WHERE Account= %s' % Account)
    # print('total records:', cursor.rowcount)
    result = cursor.fetchall()
    conn.close()
    return result[0]


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000)