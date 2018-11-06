import time
import requests
import math
import random
import Adafruit_DHT
import RPi.GPIO as GPIO, time, sys
import time
import smbus
from time import sleep

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

ENDPOINT = "things.ubidots.com"
TOKEN = "A1E-a5kZXG3B2szRpDU6ktgmstpWnxm3B7"  # Put your TOKEN here
DEVICE_LABEL = "IoT-Proj"  # Put your device label here 
VARIABLE_LABEL_1 = "buzzer"  # Put your first variable label here
VARIABLE_LABEL_2 = "temperatura"  # Put your second variable label here
VARIABLE_LABEL_3 = "eixoX"  # Put your second variable label here
VARIABLE_LABEL_4 = "eixoY"  # Put your second variable label here
VARIABLE_LABEL_5 = "eixoZ"  # Put your second variable label here
DELAY = 1
# Define o tipo de sensor
sensor = Adafruit_DHT.DHT11

# Define a GPIO conectada ao pino de dados do sensor
pino_sensor = 25
buzzer_pin = 11

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
 
GPIO.setup(buzzer_pin, GPIO.OUT)

def MPU_Init():
    # Write to sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
	
    # Write to power management register
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
	
    # Write to Configuration register
    bus.write_byte_data(Device_Address, CONFIG, 0)
	
    # Write to Gyro configuration register
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
	
    # Write to interrupt enable register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
    # Accelero and Gyro value are 16-bit
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr+1)
    
    # Concatenate higher and lower value
    value = ((high << 8) | low)
        
    # To get signed value from mpu6050
    if(value > 32768):
        value = value - 65536
    return value

bus = smbus.SMBus(1) 	# Or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

# print (" Reading Data of Gyroscope and Accelerometer")
print ("Reading Data of Gyroscope")

MPU_Init()

def build_payload(variable_2, variable_3, variable_4, variable_5):
    
    umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);

    # Read Accelerometer raw value
    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_YOUT_H)
    acc_z = read_raw_data(ACCEL_ZOUT_H)
	
    # Read Gyroscope raw value
    gyro_x = read_raw_data(GYRO_XOUT_H)
    gyro_y = read_raw_data(GYRO_YOUT_H)
    gyro_z = read_raw_data(GYRO_ZOUT_H)
	
    # Full scale range +/- 250 degree/C as per sensitivity scale factor
    Ax = acc_x/16384.0
    Ay = acc_y/16384.0
    Az = acc_z/16384.0
	
    Gx = gyro_x/131.0
    Gy = gyro_y/131.0
    Gz = gyro_z/131.0
	
    # Print giroscopio + acelerometro
    # print ("Gx = %.2f" %Gx, u'\u00b0'+ "/s", "\tGy = %.2f" %Gy, u'\u00b0'+ "/s", "\tGz = %.2f" %Gz, u'\u00b0'+ "/s", "\tAx = %.2f g" %Ax, "\tAy = %.2f g" %Ay, "\tAz = %.2f g" %Az)
    # Print giroscopio

    print ("Gx = %.2f" %Gx, u'\u00b0'+ "/s", "\tGy = %.2f" %Gy, u'\u00b0'+ "/s", "\tGz = %.2f" %Gz) 
    print ("Temperature = %.2f" %temp + " graus Celsius", "\tHumidity = %.2f" %umid + "%")
    
    # Buzzer
    #value_1 = 10

    # Temperature
    value_2 = temp

    # EixoX
    value_3 = round(Gx, 2)

    # EixoY
    value_4 = round(Gy, 2)

    # EixoZ
    value_5 = round(Gz, 2)

    payload = {variable_2: value_2,
               variable_3: value_3,
               variable_4: value_4,
               variable_5: value_5}

    return payload

def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://things.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True

def get_var(url=ENDPOINT, device=DEVICE_LABEL, variable=VARIABLE_LABEL_1,
            token=TOKEN):
    
    # Read Gyroscope raw value
    gyro_x = read_raw_data(GYRO_XOUT_H)
    gyro_y = read_raw_data(GYRO_YOUT_H)
    gyro_z = read_raw_data(GYRO_ZOUT_H)

    Gx = gyro_x/131.0
    Gy = gyro_y/131.0
    Gz = gyro_z/131.0
    
    try:
        url = "http://{}/api/v1.6/devices/{}/{}/lv".format(url,
                                                        device,
                                                        variable)

        headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

        attempts = 0
        status_code = 400

        while status_code >= 400 and attempts < 5:
            print("[INFO] Retrieving data, attempt number: {}".format(attempts))
            req = requests.get(url=url, headers=headers)
            status_code = req.status_code
            attempts += 1
            time.sleep(1)

        print("[INFO] Results:")
        print(req.text)
        print ("Gx = %.2f" %Gx, u'\u00b0'+ "/s", "\tGy = %.2f" %Gy, u'\u00b0'+ "/s", "\tGz = %.2f" %Gz)
        if (float(req.text) > 0.0):
            if (Gx > 5.0 or Gy > 5.0 or Gz > 5.0):
                myPWM=GPIO.PWM(buzzer_pin, 100)
                myPWM.start(100)
                sleep(5)
                myPWM.stop()
            
    except Exception as e:
        print("[ERROR] Error posting, details: {}".format(e))

        
def main():
    payload = build_payload(VARIABLE_LABEL_2, VARIABLE_LABEL_3, VARIABLE_LABEL_4, VARIABLE_LABEL_5)

    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")

if __name__ == '__main__':
    while (True):
        main()
        get_var()
        time.sleep(DELAY)

