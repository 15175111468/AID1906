"""
ftp 文件服务器 ,服务端
env: python 3.6
多进程多线程并发 socket
"""

from socket import *
from threading import Thread
import os,sys

# 全局变量
HOST = '0.0.0.0'
PORT = 8080
ADDR = (HOST,PORT)
FTP = "/home/tarena/FTP/" # 文件库路径

# 功能类 (线程类)
# 查文档, 下载,上传
class FTPServer(Thread):
    def __init__(self,connfd):
        super().__init__()
        self.connfd = connfd

    def 查看(self):

    # 循环接受来自客户端的请求
    def run(self):
        while True:
            request=self.connfd.recv(1024).decode()
            if request == '查看列表':
                self.查看()
                 

# 启动函数
def main():
    # 创建监听套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    print("Listen the port 8080....")

    while True:
        # 循环等待客户端连接
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            os._exit(0)
        except Exception as e:
            print(e)
            continue

        # 创建新的线程处理请求
        client = FTPServer(c)
        client.setDaemon(True)
        client.start()




