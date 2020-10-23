from machine import Pin,ADC
import time
from keras_lite import Model  
import ulab as np
import network     
import urequests   

sta=network.WLAN(network.STA_IF)
sta.active(True)   
sta.connect('BBC-2.4G','29308118')   

while not sta.isconnected() :
    pass

print('Wifi Connected')

device_id = "24882018622"
headers={"CK":"DKHXWMR9HCE2C4MKBF"} 

url_CHT="http://iot.cht.com.tw/iot/v1/device/"+device_id+"/rawdata"


url_line="http://maker.ifttt.com/trigger/tem2/with/key/cpW5iV13wxj1QLV_LazLQs"

mean=170.98275862068965
std=90.31162360353873     
model = Model('temperature_model.json')

adc_pin = Pin(36)        
adc = ADC(adc_pin)       
adc.width(ADC.WIDTH_9BIT)
adc.atten(ADC.ATTN_11DB) 

data=0

while True:            

    for i in range(20):              
        thermal=adc.read()     
        data=data+thermal      
        time.sleep(0.01)
    
    data=data/20         
    
    data = np.array([int(data)])        
    data = data-mean                    
    data = data/std                     
    tem = model.predict(data)  
    tem = round(tem[0]*100,1)           
    print(tem,end='   ')                      
    
    CHT_data=[{"id":"thermistor","value":[str(tem)]}]
    
    urequests.post(url_CHT,json=CHT_data,headers=headers)  
    
    print("Uploaded")
    
    if(tem>=20):  
        urequests.get(url_line+"?value1="+str(tem)) 
        print("Warning!!!")
    
    data=0
    time.sleep(60)      