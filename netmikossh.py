from netmiko import ConnectHandler

net_connect=ConnectHandler(device_type= 'cisco_ios',ip='10.10.10.10',port='22',username='cisco',password='cisco')
net_connect.find_prompt()
output=net_connect.send_command("show ip int brief")
output2=net_connect.send_command("show run")
print(output)
print(output2)


