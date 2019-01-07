#操作数据库
#封装操作数据库的方法
import  pymysql
import   random
from JLC_AutoTest.common.settings import MY_SQL_INFO,REDIS_INFO,BASE_PATH
import redis
import codecs,os
from datetime import date,timedelta

class OpMysql(object):
    def __init__(self,host, users, password, port, db):
        self.host=host
        self.users=users
        self.password = password
        self.port=port
        self.db=db
    def connect_mysql(self):
        try:
            conn = pymysql.connect(host=self.host, user=self.users, password=self.password, port=self.port,
                                               db=self.db, charset='utf8')
            conn._write_timeout = 10000
            # cursor = conn.cursor()
            print('数据库连接成功')
            return conn
        except Exception as e:
           print (e)

    def close_mysql(self):
        conn= self.connect_mysql()
        cursor = conn.cursor()
        cursor.close()
        conn.close()

    def op_db_delete(self,sql):
        conn = self.connect_mysql()
        cursor = conn.cursor()
        try:
            print ('delsql',sql)
            cursor.execute(sql)
        except Exception as e:
            print (e)
            return e
        else:
            conn.commit()
            res='数据库删除成功'
            print ('数据库删除成功')
        return res

    def op_db_select(self,sql):
        conn = self.connect_mysql()
        cursor = conn.cursor()
        try:
            print (sql)
            cursor.execute(sql)
        except Exception as e:
            print (e)
            return e
        else:
            res_list = []
            sql_res = cursor.fetchall()
            print ('数据库查询成功')
            # self.conn.cursor(0)         #移动游标
            for c in sql_res:
                res_list.append(c)

        return res_list

    def op_db_update(self,sql):
        # self.cursor = self.conn.cursor()
        conn = self.connect_mysql()
        cursor = conn.cursor()
        try:
            print ('update sql...',sql)
            cursor.execute(sql)
        except Exception as e:
            print (e)
            return e
        else:
            conn.commit()
            res = '数据库修改成功'
            print ('数据库修改成功')
            return res

    def op_db_insert(self, sql):
        conn = self.connect_mysql()
        cursor = conn.cursor()
        try:
            print('update sql...', sql)
            cursor.execute(sql)
        except Exception as e:
            print(e)
            return e
        else:
            conn.commit()
            res = '数据库添加成功'
            print('数据库添加成功')
            return res

# opmysql=OpMysql(**MY_SQL_INFO)

#删除redis里面的key值

def delete_redis():
    r=redis.Redis(**REDIS_INFO)
    r.delete('iosUpdateInfo')  # 删除key
    r.delete('iosPLusUpdateInfo')
    r.delete('iosVipUpdateInfo')
    r.delete('iosProUpdateInfo')

file_path=os.path.join(os.path.join(BASE_PATH,'model'),'districtcode.txt')

class JianlcTools(object):
    def createphones(self):  #随机产生手机号
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))


# 随机生成身份证号,男17位为奇数,女17位为偶数

def getdistrictcode():
    with open(file_path, "r") as file:
        data = file.read()
        # print(data)
        # data = data.replace(codecs.BOM_UTF8, "")
        districtlist = data.split('\n')
        file.closed
    for node in districtlist:
        if node[10:11] != ' ':
            state = node[10:].strip()
        if node[10:11] == ' ' and node[12:13] != ' ':
            city = node[12:].strip()
        if node[10:11] == ' ' and node[12:13] == ' ':
            district = node[14:].strip()
            code = node[0:6]
            codelist.append({"code": code})
def gennerator(sex, begainYear, endYear):

    # 男 sex 为1,  女 sex  为2
    jishu = (1, 3, 5, 7, 9)
    oushu = (0, 2, 4, 6, 8)

    global codelist
    codelist = []
    if not codelist:

        getdistrictcode()
    id = codelist[random.randint(0, len(codelist))]['code']  # 地区项
    id = id + str(random.randint(begainYear, endYear))  # 年份项
    da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
    id = id + da.strftime('%m%d')

    # 15,16位号码 随机处理
    id = id + str(random.randint(10, 99))  # ，顺序号简单处理

    # 17位号码判断男女性别
    if sex == 1:
        id = id + str(random.choice(jishu))
    elif sex == 2:
        id = id + str(random.choice(oushu))

    return id

# 得出第18位校验码
def jiaoyanma(shenfenzheng17):
    def haoma_validate(shenfenzheng17):
        if type(shenfenzheng17) in [str, list, tuple]:
            if len(shenfenzheng17) == 17:
                return True
        raise Exception('Wrong argument')

    if haoma_validate(shenfenzheng17):
        if type(shenfenzheng17) == str:
            seq = map(int, shenfenzheng17)
        elif type(shenfenzheng17) in [list, tuple]:
            seq = shenfenzheng17

        t = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        s = sum(map(lambda x: x[0] * x[1], zip(t, map(int, seq))))
        b = s % 11
        bd = {
            0: '1',
            1: '0',
            2: 'X',
            3: '9',
            4: '8',
            5: '7',
            6: '6',
            7: '5',
            8: '4',
            9: '3',
            10: '2'
        }
        return bd[b]
def get_sfz_num(time, sex, begainYear, endYear):
    sfzList = []
    times = int(time)
    sex = int(sex)
    begainYear = int(begainYear)
    endYear = int(endYear)
    for i in range(time):
        t = gennerator(sex, begainYear, endYear)
        z = jiaoyanma(t)
        m = t + z
        sfzList.append(m)
    return sfzList
def card_number():
    time = 1
    sex = 1
    startYear = 1989
    endYear = 1995
    data = get_sfz_num(time, sex, startYear, endYear)
    return data[0]
# print(card_number())

    #获取银行卡号
def create_bank(time):
    time = int(time)
    prelist = ["622848"]
    list = []
    for i in range(time):
        code = prelist[0] + "".join(random.choice("0123456789") for i in range(13))
        list.append(code)
    return list

def bank_number():
    time = 1
    data = create_bank(time)
    return data[0]

#随机生成姓名
def gener_name():

    xing='赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
    ming='讹误宿舍嘟嘟无悟空圣诞节说了我爱搜扫描阿斯阿里郎款斯柯达速度快肯定是'
    X=random.choice(xing)
    M="".join(random.choice(ming) for i in range(2))
    return X+M
