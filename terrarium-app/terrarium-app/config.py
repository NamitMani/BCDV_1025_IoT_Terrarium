import pandas as pd


BASE_URL = "http://4.204.190.172:3000"


dummy_data = pd.DataFrame([
    {'device_id': '69', 'Temperature': '30 C', 'Humidity': '22%', 'Time': 'June 23, 2023 4:27 PM', 'Status': 'OK'}
])

configuration = {
    'createDevice': {'Device ID', 'Owner'},
    'queryDevice': {'Device ID'},
    'recordSensorData': {'Device ID', 'Temperature', 'Humidity'},
    'queryAllDevices': {}
}

if __name__ == '__main__':
    print(dummy_data)