import socket
import time

def soc():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # サーバを指定
        s.connect(('192.168.10.222', 50000))
        # サーバにメッセージを送る
        s.send(b"hi i am nishiyama.")
        # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
        data = s.recv(1024)
        print("ok")
        #
        print(repr(data))
        soc()
        time.sleep(3)

soc()
print("end")
