from netmiko import ConnectHandler

Network_Device = { "host": "ios-xe-mgmt.cisco.com",
                    "username": "developer",
                    "password": "C1sco12345",
                     "device_type": "cisco_ios",
                     "secret": "C1sco12345",
}               

Connect = ConnectHandler(**Network_Device)
Connect.enable()