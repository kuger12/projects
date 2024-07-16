from selenium import webdriver 
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.service import Service
import matplotlib.pyplot as plt
from matplotlib import style
from bs4 import BeautifulSoup
import time
from os import system as sys

sys("clear")

print("creating session(Morroco :casablaca_settat)...")

f_options = Options()
f_options.add_argument("--headless")

driver = webdriver.Firefox(options = f_options)
driver.get("https://www.accuweather.com/en/ma/casablanca/243353/weather-forecast/243353" )

driver.implicitly_wait(5)
content = driver.page_source
soup = BeautifulSoup(content , 'lxml')

def hourly(): 

    dates = soup.find_all("span" , {'class' : 'hourly-list__list__item-time'})
    temperatures = soup.find_all("span" , {'class' : 'hourly-list__list__item-temp'})
    humidites = soup.find_all("div" , {'class' : 'hourly-list__list__item-precip'})
    for x in range(12) :
        dates[x] = dates[x].text.strip()
        temperatures[x] = int(temperatures[x].text.strip().strip("°"))
        humidites[x] = int(humidites[x].text.strip().strip("%"))
    return dates , temperatures , humidites


def daily() :
    w_details = {} 
    driver.find_element(By.XPATH , "/html/body/div/div[7]/div[1]/div[1]/a[1]").click()
    content2 = driver.page_source
    soup2 = BeautifulSoup(content2 , "lxml")
    temperature = soup2.find("div" , {'class' : 'display-temp'}).text
    weath_desc = soup2.find("div" , {'class' : 'phrase'}).text
    details = soup2.find_all("div" , {'class' : 'detail-item spaced-content'})
    for x in range(len(details)) :
        details[x] = details[x].text
        key , value = details[x].strip().split("\n")
        w_details[key] = value
    return temperature , weath_desc , w_details



def weekly() :
    med_temp = []
    stamps = soup.find_all("div" , {'class' : 'date'})
    dates = soup.find_all("p" , {'class' : 'day'})
    big_temp = soup.find_all("span" , {'class' : 'temp-hi'})
    low_temp = soup.find_all("span" , {'class' : 'temp-lo'})
    humidites = soup.find_all("div" , {'class' : 'precip'})
    for x in range(10) :
        stamps[x] = stamps[x].text.strip().split("\n")[1]
        dates[x] = dates[x].text.strip()
        big_temp[x] = int(big_temp[x].text.strip().strip("°"))
        if low_temp[x].text.strip().strip("°") == "Lo" :
            low_temp[x] = big_temp[x]
        else :
            low_temp[x] = int(low_temp[x].text.strip().strip("°"))
        humidites[x] = int(humidites[x].text.strip().strip("%"))
    for big , low in zip(big_temp , low_temp) :
        medium = (big+low)//2
        med_temp.append(medium)
    return dates , stamps , big_temp , low_temp ,med_temp ,  humidites
 

def hourly_graph(dates , temperatures , humidities) : 
    sys("clear")
    degres = [x for x in range(min(temperatures)- (min(temperatures)%5) , max(temperatures)+5 , 5)]
    precipitations = [i  for i in range(min(humidities)- (min(humidities)%5) , max(humidities)+5 , 5) ]
    fig , axes  = plt.subplots(2 , 1)


    axes[0].plot(dates, temperatures ,   lw = 2 , color = "#ed190a" , label = "temperature")

    axes[0].set_xlabel("days")
    axes[0].set_ylabel("temperature(°C)")
    axes[0].set_yticks(degres , [f"{x}°C" for x in degres])
    axes[0].set_title("hourly temperature")
    
    axes[1].plot(dates , humidities,   lw = 2 , color = "#0f8eed" , label = "preecipitation")
    axes[1].set_xlabel("days")
    axes[1].set_ylabel("precipitation")
    axes[1].set_yticks(precipitations , [f"{x}%" for x in precipitations])
    axes[1].set_title("hourly precipitation")
    fig.suptitle("hourly temperature&precipitation")
    axes[0].legend()
    axes[1].legend()
    print("stretch the photo if u had any problems on reding it")
    print("close it to carry on")
    plt.show()
 






def weekly_graph(dates , stamps , big_temp , low_temp ,med_temp ,  humidities) : 
    sys("clear")
    labels = [f"{date[:2]}({stamp})" for date , stamp in zip(dates , stamps)]
    degres = [x for x in range(min(low_temp)- (min(low_temp)%5) , max(big_temp)+5 , 5)]
    precipitations = [i  for i in range(min(humidities)- (min(humidities)%5) , max(humidities)+5 , 5) ]
    fig , axes  = plt.subplots(2 , 1)


    axes[0].plot(labels , big_temp ,   lw = 2 , color = "#ed190a" , label = "highest temperature")
    axes[0].plot(labels , low_temp   , lw = 2 , color = "#8fce00" , label = "lowest temperature")
    axes[0].plot( labels , med_temp  , lw = 2 , color = "#f1c232" , label = "average temperature")

    axes[0].set_xlabel("days")
    axes[0].set_ylabel("temperature(°C)")
    axes[0].set_yticks(degres , [f"{x}°C" for x in degres])
    axes[0].set_title("weekly temperature")
    
    axes[1].plot(labels , humidities,   lw = 2 , color = "#0f8eed" , label = "preecipitation")
    axes[1].set_xlabel("days")
    axes[1].set_ylabel("precipitation")
    axes[1].set_yticks(precipitations , [f"{x}%" for x in precipitations])
    axes[1].set_title("weekly precipitation")
    fig.suptitle("weekly temperature&precipitation")
    axes[0].legend()
    axes[1].legend()
    print("stretch the photo if u had any problems on reding it")
    print("close it to carry on")
    plt.show()
  

def daily_repr(temperature , weth_desc , details) :
    sys("clear")
    print("weather condition : ")
    print(f"   {weth_desc} : {temperature}")
    for index , key in enumerate(details) :
        if index%4 == 0 :
            input()
        if index > 1 :
           print(f"  {key} : {details[key]}")
        else : 
            print(f"  {key} : {details[key]}C")


def week_days_repr(sug_stamp ,dates , stamps , big_temp , low_temp ,med_temp ,  humidites) :
    sys("clear")
    for index , stamp in enumerate(stamps) : 
        if sug_stamp == stamp : 
            print(f"{stamp} ({dates[index]}) :")
            print(f"  lowest temperture : {low_temp[index]}°C")
            print(f"  highest temperature : {big_temp[index]}°C")
            print(f"  precipitation : {humidites[index]}%")
            break
    else : 
        print("that stamp does not belong to ower days range")



sys("clear")
print("creating session(Morroco :casablaca_settat)...")
print("  _scraping weekly_data")
weekly_data = weekly()
sys("clear")
print("creating session(Morroco :casablaca_settat)...")
print("  _scraping daily_data")
daily_data = daily()
sys("clear")
print("creating session(Morroco :casablaca_settat)...")
print("  _scraping hourly_data")
hourly_data = hourly()

message = """ what do you want to do ?
"dw" -> show the weather condition of the current day
"wk" -> show the weather condition of aspecific day (range : 10 days as maximum)
"hg" -> represent the variation of temperature and precipitation of the current day(12 hours) on a graph
"wg" -> represent the variation of temperature and precipitation of 10 days on a graph
"q" -> quit

"""

while True :
    print(message)
    choice = input("choice : ")
    if choice == "dw" :
        daily_repr(*daily_data)
    elif choice == "wk" :
        stamp = input("stamp(month/day) , ex : 7/14   : ")
        week_days_repr(stamp , *weekly_data)
    elif choice == "hg" :
        hourly_graph(*hourly_data)
    elif choice == "wg" :
        weekly_graph(*weekly_data)
    elif choice == "q" :
        print("the app is closed")
        quit()
    else :
        print("command doesn't exist")

    input("press enter to quit(E):")
    sys("clear")