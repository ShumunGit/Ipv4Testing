import sys, subprocess, pytest

# allure: generate report to the folder. 
# Example: PS C:\Users> pytest --alluredir C:\Report FolderFile_test\testCases
# load the allure report to html broswer: CMD > allure serve C:\Report

@pytest.mark.Smoke
def test_ipv4_address_valid():
    print('\n')
    # list of ipv4 address. 
    list = ["8.8.8.8\n","76.223.0.174","212.179.37.1","212.179.124.5","212.25.77.26","172.217.22.14"]
    # itartion to the list. 
    for ip in list:
        ip = ip.rstrip("\n")
       
        octet_list = ip.split('.')
        
        if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and (0 <= int(octet_list[1]) <= 255  and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
            continue
        else:
            print('\n* There was an invalid IP address in the file: {} :(\n)'.format(ip))
            sys.exit()

@pytest.mark.Regression
def test_ping_to_ipv4_address_list():
    print('\n')
    list = ["8.8.8.8","76.223.0.174","212.179.37.1","212.179.124.5","212.25.77.26","172.217.22.14"]
    for ip in list:
        ip = ip.rstrip("\n")

        ping_replay = subprocess.call('ping %s /n 2' % (ip), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        if ping_replay == 0:
            print("IPv4 address is respond: ", ip)
        else:
            print("{}, not Valid.".format(ip))
            sys.exit()
        
