import pandas as pd

df = pd.read_excel(r'C:\Users\NguyenVanKien\Desktop\Python VS Code\Auto\DanhSach_ThietBi.xlsx')
#print(df)

#chuyển đổi DataFrame thành danh sách các thiết bị
list_device_iso = []
for index, row in df.iterrows(): 
    device_iso = {
        'device_type': row['device_type'],
        'hostname': row['hostname'],
        'username': row['username'],
        'password': row['password'],
        'secret': row['secret'],
    }
    list_device_iso.append(device_iso)

#In danh sách các thiết bị
print(list_device_iso)