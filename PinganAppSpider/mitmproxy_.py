import json

# from openpyxl import Workbook

from db.mongo_pool import MongoDB


# 实例化
mongo = MongoDB()

# 创建一个工作蒲对象
# wb = Workbook()

# sheet = wb.active

# 添加表头
# sheet.append(['医生姓名', '所属科室', '职位', '所在城市', '级别', '服务患者数', '好评率', '24小时回复率', '擅长', '简介', '医院名称', '医院地址'])


def response(flow):
    if 'api.jk.cn/m.api?' in flow.request.url:
        # 获取数据
        doctor_infos = json.loads(flow.response.text)["content"][0]["result"]

        # print(doctor_infos)
        # print('-'*200)

        for doctor_info in doctor_infos:
            # 创建储存信息列表
            infos_list = []
            # 医生姓名
            doctor_name = doctor_info["doctor_name"]
            # 所属科室
            org_dept_name = doctor_info["org_dept_name"]
            # 职位
            job_title_text = doctor_info["job_title_text"]
            # 所在城市
            prov_name = doctor_info["prov_name"]
            # 级别
            hospital_level_text = doctor_info["hospital_level_text"]
            # 服务患者数
            doctor_inquiry_service_num = doctor_info["doctor_inquiry_service_num"]
            # 好评率
            famous_good_rate = doctor_info["famous_good_rate"]
            # 24小时回复率
            doctor_24hour_reply_rate = doctor_info["doctor_24hour_reply_rate"]
            # 擅长
            expert_in = doctor_info["expert_in"]
            # 简介
            introduction = doctor_info["introduction"]
            # 医院名称
            hospital_name = doctor_info["hospital_name"]
            # 医院地址
            hospital_address = doctor_info["hospital_address"]

            # 去除非北京市的数据
            if prov_name == "北京市":

                infos_list.append([doctor_name, org_dept_name, job_title_text, prov_name, hospital_level_text, doctor_inquiry_service_num, famous_good_rate, doctor_24hour_reply_rate, expert_in, introduction, hospital_name, hospital_address])

                mongo.insert_one({'doctor': infos_list})



                # 加入表格
                # sheet.append([doctor_name, org_dept_name, job_title_text, prov_name, hospital_level_text, doctor_inquiry_service_num, famous_good_rate, doctor_24hour_reply_rate, expert_in, introduction, hospital_name, hospital_address])
                # infos_list.append([doctor_name, org_dept_name, job_title_text, prov_name, hospital_level_text, doctor_inquiry_service_num, famous_good_rate, doctor_24hour_reply_rate, expert_in, introduction, hospital_name, hospital_address])

        # 保存
        # wb.save("doctor_info.xlsx")


# for info in infos_list:
#     sheet.append(info)

# # 保存
# wb.save("doctor_info.xlsx")
