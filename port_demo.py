"""D2 实验：进程、文件、端口

跑法（两个终端）：
  终端 1：python port_demo.py    ← 启动后先别关
  终端 2：python port_demo.py    ← 第二次启动，观察端口冲突报错

浏览器打开 http://127.0.0.1:8765 能看到本进程回的一句话。
"""

import os
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

# 选 8765 而不是 8000：本机 8000 已经被"芯火助手"占用，正好可以说明端口是"先到先得"的座位
PORT = 8765

# ① 进程：正在运行的这份程序，操作系统给它一个身份证号，叫 PID
print(f"我的 PID（进程身份证号）：{os.getpid()}")

# ② 文件：程序在磁盘上的位置，路径就是它的地址
print(f"我的文件位置：{os.path.abspath(__file__)}")

# ③ 端口：进程对外服务时占的一个"门牌号"。
#    同一台机器上，同一个端口同时只能被一个进程占；第二个来的会被拒。
#    先试探一次端口能不能用，被占了就把真实报错打出来再退出。
probe = socket.socket()
try:
    probe.bind(("127.0.0.1", PORT))
    probe.close()
except OSError as e:
    print(f"端口 {PORT} 已被别的进程占用：{e}")
    raise SystemExit(1)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"你好，我是 port_demo，PID={os.getpid()}，端口={PORT}".encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print(f"[收到请求] {fmt % args}")


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", PORT), Handler)
    print(f"服务已启动：http://127.0.0.1:{PORT}  （按 Ctrl+C 停止）")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n已停止。")
