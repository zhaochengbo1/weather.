from tkinter import *
from tkinter import messagebox
import urllib.request
import requests
import json
def weather():
    city=entry.get()
    if city=='':
        messagebox.showinfo('Alarm','Please input city name')
    else:
        headers = {
            'Authorization': 'APPCODE b3d51258b02747a9a086603fda9e6b3a',
        }

        params = (
            ('city', city),
            ('citycode', 'citycode'),
            ('cityid', 'cityid'),
            ('ip', 'ip'),
            ('location', 'location'),
            )

        response = requests.get('https://jisutqybmf.market.alicloudapi.com/weather/query', headers=headers, params=params, verify=False)

        info=response.content.decode('utf-8')
        info = json.loads(info)
        lis.delete(0,END)
        weeker=info['result']['week']
        wea=info['result']['weather']
        lis.insert(0, "Week:%s"  %weeker.replace('星期一','Monday').replace('星期二','Tuesday').replace('星期三','Wednesday').replace('星期四','Thursday').replace('星期五','Friday').replace('星期六','Saturday').replace('星期日','Sunday') )
        lis.insert(1, "Weather:%s" %wea.replace('晴','Sunny').replace('阴','Cloudy').replace('多云','Cloudy').replace('阵雨','Rainy'))
        lis.insert(2, "Temp:%s℃" % info['result']['temp'])
         


root =Tk()
root.title("search weather")
root.geometry('500x400+55+300')
lable = Label(root,text='Input city name:')
lable.grid(row=0,column=0)
entry=Entry(root,font=('Microsoft Yahoo',22))
entry.grid(row=0,column=1)
lis=Listbox(root,font=('Microsoft Yahoo',15),width=40,height=10)
lis.grid(row=1,columnspan=2)
button=Button(root,text='Search',width=10,command=weather)
button.grid(row=2,column=0,sticky=W)
button1=Button(root,text='Exit',width=10,command=root.quit)
button1.grid(row=2,column=1,sticky=E)
root.mainloop()
