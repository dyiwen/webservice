# -*- coding:utf-8 -*-
import sys
import logging
import suds
from suds.xsd.doctor import Import,ImportDoctor
import Tkinter as tk

from Tkinter import StringVar
from Tkinter import Listbox
from Tkinter import END
from Tkinter import Scrollbar
from Tkinter import Text
from Tkinter import Entry


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
# add the Import Tag in wsdl
imp = Import('http://www.w3.org/2001/XMLSchema',
            location='http://www.w3.org/2001/XMLSchema.xsd')
imp.filter.add("http://WebXml.com.cn/")
d = ImportDoctor(imp)
#------------------------------------------------------------
#China weather predict in three days (webservice url)
try:
    web_url = 'http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl'
    client = suds.client.Client(web_url, doctor=d)

except:
    print 'url is error'
#----------------------------------------------------------------------------
#set FUNCTION
def get_all_methods(client): #查询本webservice所有的方法
    return [method for method in client.wsdl.services[0].ports[0].methods]

def get_method_args(client,method_name): #查询本webservice所有方法调用的参数
    method = client.wsdl.services[0].ports[0].methods[method_name]
    input_params = method.binding.input
    return input_params.param_defs(method)

interfaces = get_all_methods(client)
print 'There are interfaces what we got :\n',interfaces
print '-------------------------------------------------------------------------------------------'

def get_all_method_args(): #查询接口所有方法调用的参数
    for method_name in interfaces:
        print get_method_args(client, method_name)

cli_ser = client.service
#calling interface---------------------------------------------------------------------------------
def ProvinceAre():#查询天气预报支持的所有省份
    #print cli_ser.getSupportProvince()
    P_are = cli_ser.getSupportProvince()
    for province in P_are:
        #print province[1]
        #print type(province[1])
        return province[1]

def CityAre():#查询天气预报支持的国内外的城市
    p = get_City().
    #p = raw_input('Please input a ProvinceName in Cinese:\n')
    byProvinceName = p
    print cli_ser.getSupportCity(p)

def DataSetAre(): #查询本天气预报支持的所有数据信息
    #print cli_ser.getSupportDataSet()
    D_are = cli_ser.getSupportDataSet()
    for i in D_are:
        # print type(i)
        # print str(i)
        pass
    return str(i)


def WeatherInfo(): #查询未来3天内某城市的天气状况和生活指数
    c = raw_input('Please input a CityName in Chinese:\n')
    theCityName = c
    #print cli_ser.getWeatherbyCityName(c)
    output = tuple(cli_ser.getWeatherbyCityName(c))
    for i in output:
        for j,k in enumerate(i[1]):
            print j,k


if __name__ == '__main__':
    root = tk.Tk()
    root.title('webservice_interface_tool')
    root.geometry('450x300')
    root.resizable(False, False)                      #FFFFFF白色 #003366蓝色
    canvas = tk.Canvas(root, height=300, width=450, bg='#FFFFFF')
    filename = r'/home/dyiwen/Documents/job/job_third(webservice)/picture/title.png'
    image_file = tk.PhotoImage(file=filename)
    canvas.pack()
    title_label=tk.Label(root,image=image_file,bg='#003366').place(x=0,y=0)
    JC_Lable = tk.Label(root,
                        text='天气预报Web服务，数据每2.5小时左右自动更新一次，准确可靠。'
                             '包括 340 多个中国主要城市和 60 多个国外主要城市三日内的天气预报数据。'
                             '此天气预报Web Services请不要用于任何商业目的',
                        bg='#FFFFFF',wraplength=450,justify='left',font='12').place(x=0,y=50)
    JC_Lable1 = tk.Label(root,text='本工具通过出入参测试webservice接口的调取功能',bg='#FFFFFF',justify='left',
                         font='12').place(x=0,y=160)



    def new_window():
        root.destroy()
        root1 = tk.Tk()
        root1.title('接口介紹')
        root1.geometry('600x450')
        root1.resizable(False, False)
        canvas = tk.Canvas(root1, height=450, width=600, bg='#FFFFFF').pack()
        # image
        file_City = r'/home/dyiwen/Documents/job/job_third(webservice)/picture/gSC.png'
        file_Prov = r'/home/dyiwen/Documents/job/job_third(webservice)/picture/gSP.png'
        file_Data = r'/home/dyiwen/Documents/job/job_third(webservice)/picture/gSDS.png'
        file_Weather = r'/home/dyiwen/Documents/job/job_third(webservice)/picture/gWbCN.png'

        image_City = tk.PhotoImage(file=file_City)
        image_Prov = tk.PhotoImage(file=file_Prov)
        image_Data = tk.PhotoImage(file=file_Data)
        image_Weather = tk.PhotoImage(file=file_Weather)
        # getsupportcity
        gSC_B = tk.Button(root1,bg='#FFFFFF',fg='#87CEEB',image=image_City,bd=0,command=get_City).place(x=0,y=0)
        gSC_L = tk.Label(root1,bg='#FFFFFF',text='查询本天气预报Web Services支持的国内外城市或地区信息'
                         ,justify='left',font='bold').place(x=0,y=30)
        gSC_L = tk.Label(root1,bg='#FFFFFF',text='输入参数：byProvinceName=指定的洲或国内的省份，'
                                                 '若为ALL或空则表示返回全部城市；返回数据：一个一维字符串数组String()，'
                                                 '结构为：城市名称(城市代码)。',
                         justify='left',wraplength=600,fg='#696969').place(x=0,y=50)
        #getsupportdataset
        gSDS_B = tk.Button(root1,bg='#FFFFFF',fg='#87CEEB',image=image_Data,bd=0,command=get_Data).place(x=0,y=80)
        gSDS_L = tk.Label(root1,bg='#FFFFFF',text='获得本天气预报Web Services支持的洲、国内外省份和城市信息'
                         ,justify='left',font='bold').place(x=0,y=110)
        gSDS_L = tk.Label(root1,bg='#FFFFFF',text='输入参数：无；返回：DataSet。DataSet.Tables(0)为支持的洲和国内省份数据，'
                                                  'DataSet.Tables(1)为支持的国内外城市或地区数据。'
                                                  'DataSet.Tables(0).Rows(i).Item("ID")'
                                                  '主键对应DataSet.Tables(1).Rows(i).Item("ZoneID")外键。'
                                                  'Tables(0)：ID=ID主键，Zone=支持的洲、省份；Tables(1)：ID'
                                                  '主键，ZoneID=对应Tables(0)ID的外键，'
                                                  'rea=城市或地区，AreaCode = 城市或地区代码。',
                         justify='left',wraplength=600,fg='#696969').place(x=0,y=130)
        #getsupportprovince
        gSP_B = tk.Button(root1,bg='#FFFFFF',fg='#87CEEB',image=image_Prov,bd=0,command=get_Pro).place(x=0,y=190)
        gSP_L = tk.Label(root1,bg='#FFFFFF',text='获得本天气预报Web Services支持的洲、国内外省份和城市信息'
                         ,justify='left',font='bold').place(x=0,y=220)
        gSP_L = tk.Label(root1,bg='#FFFFFF',text='输入参数：无； 返回数据：一个一维字符串数组 String()，内容为洲或国内省份的名称。',
                         justify='left',wraplength=600,fg='#696969').place(x=0,y=240)
        #getWeatherbyCityName
        gWeath_B = tk.Button(root1,bg='#FFFFFF',fg='#87CEEB',image=image_Weather,bd=0).place(x=0,y=260)
        gWeath_L = tk.Label(root1,bg='#FFFFFF',text='根据城市或地区名称查询获得未来三天内天气情况、现在的天气实况和生活指数'
                         ,justify='left',font='bold').place(x=0,y=290)
        gWeath_L = tk.Label(root1,bg='#FFFFFF',text='调用方法如下：输入参数：theCityName=城市中文名称(国外城市可用英文)'
                                                    '或城市代码(不输入默认为上海市)，如：上海或58367，'
                                                    '如有城市名称重复请使用城市代码查询(可通过getSupportCity或'
                                                    'getSupportDataSet获得)；返回数据：一个一维数组String(22)，共有23个元素。'
        'String(0)到String(4)：省份，城市，城市代码，城市图片名称，最后更新时间。String(5)到String(11)：当天的气温，概况，风向和风力，'
                                                    '天气趋势开始图片名称(以下称：图标一)，天气趋势结束图片名称(以下称：图标二)，'
                                                    '现在的天气实况，天气和生活指数。String(12)到String(16)：第二天的气温，'
                                                    '概况，风向和风力，图标一，图标二。String(17)到String(21)：第三天的气温，'
                                                    '概况，风向和风力，图标一，图标二。String(22)被查询的城市或地区的介绍',
                         justify='left',wraplength=600,fg='#696969').place(x=0,y=310)

        root1.mainloop()
    def get_Pro():
        Get_Pro_window = tk.Toplevel()
        Get_Pro_window.title('查询所有接口支持省份')
        Get_Pro_window.geometry('230x250')
        Get_Pro_window.resizable(False, False)
        #GP_Text = Message(Get_Pro_window,width=610,text=ProvinceAre()).place(x=0,y=0)
        #ProvinceAre()
        # v = StringVar()
        sl = Scrollbar(Get_Pro_window)
        sl.pack(side='right', fill='y')
        lb = Listbox(Get_Pro_window,height=300,width=230)
        lb['yscrollcommand'] = sl.set
        # v.set(ProvinceAre())
        for item in ProvinceAre():
            lb.insert(END,item)
        lb.pack(side='left')
        sl['command'] = lb.yview

        Get_Pro_window.mainloop()

    def get_Data():
        Get_data_window = tk.Toplevel()
        Get_data_window.title('查询接口支持的数据集')
        Get_data_window.geometry('300x600')
        Get_data_window.resizable(False, False)

        sl = Scrollbar(Get_data_window)
        sl.pack(side='right', fill='y')
        T = Text(Get_data_window,height=300,width=300)
        T['yscrollcommand'] = sl.set
        T.insert(END,DataSetAre())
        T.pack(side='left')
        sl['command'] = T.yview

        Get_data_window.mainloop()

    def get_City():
        Get_city_window = tk.Toplevel()
        Get_city_window.title('查询接口支持的国内外城市或地区信息')
        Get_city_window.geometry('300x600')
        Get_city_window.resizable(False, False)
        input_Lable = tk.Label(Get_city_window,text='请输入一个城市：').place(x=0,y=0)
        input_City = Entry(Get_city_window)
        input_City.place(x=100,y=0)
        a = input_City.get()
        City_B = tk.Button(Get_city_window,text='查询',command=CityAre).place(x=0,y=20)

        input_Text = Text(Get_city_window,height=60).place(x=0,y=45)


        Get_city_window.mainloop()


    Signin_B = tk.Button(root, bg='#003366', text='进入', height=1, width=12,command=new_window)
    Signin_B.place(x=100, y=250)
    Signup_B = tk.Button(root, bg='#003366', text='退出', height=1, width=12,command=root.quit)
    Signup_B.place(x=240, y=250)


    root.mainloop()
    #WeatherInfo()
    #DataSetAre()
    #CityAre()
    #ProvinceAre()
