##################### CONFIG #####################
ssl = True   # True or False, True=https
address = "minecraft.azureedge.net"
path = "/bin-win/bedrock-server-1.18.11.01.zip"
dstFile = "./bds-temp.zip"
timeout = 10

###################### MAIN ######################
import http
import http.client
import os
import zipfile

print("Do you accept the Minecraft EULA(https://minecraft.net/terms)?")
print("您是否接受 Minecraft EULA(https://minecraft.net/terms)?")
ac = input("(y=Yes, n=No)")
if ac != "y":
	exit()

conn = None
s = ""
if ssl:
	conn = http.client.HTTPSConnection(address, timeout = timeout)
	s = "https://"
else:
	conn = http.client.HTTPConnection(address, timeout = timeout)
	s = "http://"

print("Downloading BDS from", s + address + path)
print("BDS核心来自", s + address + path)

conn.request("GET", path)
res = conn.getresponse()
print("HTTP: GET Response Status:", res.status, res.reason)
print("HTTP: 获得响应", res.status, res.reason)
if res.status != 200:
	print("HTTP: Error occured, exiting...")
	print("HTTP:出现错误, 退出...")
	exit()

data = res.read()
print("HTTP: Downloaded", len(data), "bytes")
print("HTTP: 下载", len(data), "字节")
print("Saving file...")
print("保存文件中...")
os.fdopen(os.open(dstFile, os.O_WRONLY | os.O_CREAT, 0o755), 'wb').write(data)
print("Saved")
print("保存")

zip = zipfile.ZipFile(dstFile)
print("Extracting...")
print("提取中...")
zip.extractall("./")
zip.close()
print("Extracted, deleting zip file...")
print("正在解压后删除zip文件...")
os.remove(dstFile)

print("Run SymDB2.exe")
print("运行SymDB2.exe中...")
os.system("SymDB2.exe")

print("Finished")
print("完成")
