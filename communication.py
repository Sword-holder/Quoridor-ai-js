import socket
from decision import make_decision

class Communicator(object):

    def __init__(self, port=12345):
        self.host = socket.gethostname()
        self.port = port

    def startServer(self):
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        print('服务器程序创建完成')

        self.server.listen(4)
        while True:
            try:
                conn, addr = self.server.accept()
                print('检查到链接，地址为：', addr)
                print(conn)
                message = conn.recv(256)
                print('接受到消息：', message)

                board_info = bytes.decode(message)
                print(board_info)
                board_info = board_info.split(',')
                
                if len(board_info) != 42:
                    print('Warning: length of board information not equals to 42!')
                board_info = list(map(lambda x: int(x), board_info))
                board_info_array = np.asarray(board_info)
                decision = make_decision(board_info_array)
                conn.send(str.encode(decision))

                conn.close()
            except BaseException as e:
                print(e)
                print('服务器关闭')
                break

        self.server.close()

if __name__ == '__main__':
    comm = Communicator()
    comm.startServer()