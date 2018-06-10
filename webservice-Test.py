# -*- coding:utf-8 -*-
import sys
import logging
import suds
from suds.xsd.doctor import Import,ImportDoctor
import Tkinter as tk

#-------------set coding style----------------
reload(sys)
sys.setdefaultencoding('utf8')
#---------------------------------------------

#-------------set the output of '.log'
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./web.log',
                    filemode='w')
logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
#-----------------------------------------------------------
class webs:
    # add the Import Tag in wsdl
    imp = Import('http://www.w3.org/2001/XMLSchema',
                 location='http://www.w3.org/2001/XMLSchema.xsd')
    imp.filter.add("http://WebXml.com.cn/")
    d = ImportDoctor(imp)
    # ------------------------------------------------------------
    # China weather predict in three days (webservice url)
    try:
        web_url = 'http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl'
        client = suds.client.Client(web_url, doctor=d)

    except:
        print 'url is error'

    # ----------------------------------------------------------------------------
    # set FUNCTION
    def __init__(self):
        self.client = client
        self.method_name = method_name

    def get_all_methods(self,client):  # 查询本webservice所有的方法
        return [method for method in client.wsdl.services[0].ports[0].methods]

    def get_method_args(self,client, method_name):  # 查询本webservice所有方法调用的参数
        method = client.wsdl.services[0].ports[0].methods[method_name]
        input_params = method.binding.input
        return input_params.param_defs(method)

    interfaces = get_all_methods(self,client)
    print 'There are interfaces what we got :\n', interfaces
    print '-------------------------------------------------------------------------------------------'

    def get_all_method_args(self):  # 查询接口所有方法调用的参数
        for method_name in interfaces:
            print get_method_args(client, method_name)

    cli_ser = client.service

    # calling interface---------------------------------------------------------------------------------
    def ProvinceAre(self):  # 查询天气预报支持的所有省份
        print cli_ser.getSupportProvince()

    def CityAre(self):  # 查询天气预报支持的国内外的城市
        p = raw_input('Please input a ProvinceName in Cinese:\n')
        byProvinceName = p
        print cli_ser.getSupportCity(p)

    def DataSetAre(self):  # 查询本天气预报支持的所有数据信息
        print cli_ser.getSupportDataSet()

    def WeatherInfo(self):  # 查询未来3天内某城市的天气状况和生活指数
        c = raw_input('Please input a CityName in Chinese:\n')
        theCityName = c
        # print cli_ser.getWeatherbyCityName(c)
        output = tuple(cli_ser.getWeatherbyCityName(c))
        for i in output:
            for j, k in enumerate(i[1]):
                print j, k

class GUI:
    def window(self):
        root = tk.Tk()
        root.title('webservice接口测试')
        root.geometry('970x600')
        root.resizable(False, False)
        root.mainloop()


if __name__ == '__main__':
    #webs.WeatherInfo()
    #webs.DataSetAre()
    #webs.CityAre()
    webs.ProvinceAre()
