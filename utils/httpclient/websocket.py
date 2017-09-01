from ws4py.client.threadedclient import WebSocketClient


class DummyClient(WebSocketClient):
    def opened(self):
        self.send("123")

    def closed(self, code, reason=None):
        print
        "Closed down", code, reason

    def received_message(self, m):
        print
        m


if __name__ == '__main__':
    try:
        ws = DummyClient('ws://192.168.7.169:8082/logic/ws')
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()
