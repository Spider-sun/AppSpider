from openpyxl import Workbook

from db.mongo_pool import MongoDB

# 创建一个工作蒲对象
wb = Workbook()

sheet = wb.active

# 添加表头
sheet.append(['医生姓名', '所属科室', '职位', '所在城市', '级别', '服务患者数', '好评率', '24小时回复率', '擅长', '简介', '医院名称', '医院地址'])


# 实例化
mongo = MongoDB()

# 获取数据库数据
doctor_infos = mongo.find()

# 保存
for doctor_info in doctor_infos:

        sheet.append(doctor_info['doctor'][0])

wb.save("./data/doctor_info.xlsx")