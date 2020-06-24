from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests

url = 'http://api.weatherstack.com/current?access_key={}&query={}'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


def get_weather(thanhpho):
    result = requests.get(url.format(api_key, thanhpho))
    if result:
        json = result.json()
        # (thanhpho, quocgia, doam, nhietdo_celsius, tocdogio, icon, thoitiet)
        thanhpho = json['location']['name']
        quocgia = json['location']['country']
        nhietdo_celsius = json['current']['temperature']
        icon = json['current']['weather_icons']
        doam = json['current']['humidity']
        thoitiet = json['current']['weather_descriptions']
        tocdogio = json['current']['wind_speed']
        final = (thanhpho, quocgia, nhietdo_celsius, icon, tocdogio, doam, thoitiet)
        return final
    else:
        return None



def search():
    thanhpho = thanhpho_text.get()
    thoitiet = get_weather(thanhpho)
    if thoitiet:
        diadiem_lbl['text'] = '{},{}'.format(thoitiet[0], thoitiet[1])
        nhietdo_lbl['text'] = '{}C'.format(thoitiet[2])
        thoitiet_lbl['text'] = thoitiet[6]
        tocdogio_lbl['text'] = '{}km/h'.format(thoitiet[4])
        doam_lbl['text'] = '{}%'.format(thoitiet[5])
    else:
        messagebox.showerror('Loi','khong tim thay thanh pho {}'.format(thanhpho))



app = Tk()
app.title("Phan mem thoi tiet")
app.geometry('700x350')


thanhpho_text = StringVar()
thanhpho_entry = Entry(app, textvariable=thanhpho_text)
thanhpho_entry.pack()

search_btn = Button(app, text='Tim kiem', width=18, command=search)
search_btn.pack()

diadiem_lbl = Label(app, text='',font=('bold',20))
diadiem_lbl.pack()

image_lbl = Label(app, bitmap='')
image_lbl.pack()

nhietdo_lbl = Label(app, text='',font=('bold',20))
nhietdo_lbl.pack()

thoitiet_lbl = Label(app, text='',font=('bold',20))
thoitiet_lbl.pack()

tocdogio_lbl = Label(app, text='',font=('bold',20))
tocdogio_lbl.pack()

doam_lbl = Label(app, text='',font=('bold',20))
doam_lbl.pack()

app.mainloop()
