import threading
import time
class Device(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.running = False
        self.paused = False
        self.pause_cond = threading.Condition(threading.Lock())
        self.neighbors = set()
        self.mtu = 1000   
    def send_packet(self, size):
        if size > self.mtu:
            print(f"{self.name}: DROP BIGDATA ({size} bytes) > exceeds MTU {self.mtu}")
        else:
            print(f"{self.name}: Sent {size} bytes OK")
    def run(self):
        """Main loop for the device thread"""
        self.running = True
        print(f"{self.name}: START")
        while self.running:
            with self.pause_cond:
                while self.paused:
                    self.pause_cond.wait()
            time.sleep(1)  
            self.send_hello()
        print(f"{self.name}: STOP")
    def start(self):
        super().start()
    def stop(self):
        self.running = False
    def pause(self):
        with self.pause_cond:
            self.paused = True
            print(f"{self.name}: PAUSED")
    def resume(self):
        with self.pause_cond:
            self.paused = False
            self.pause_cond.notify()
            print(f"{self.name}: RESUMED")
    def send_hello(self):
        pass
    def recv_hello(self, sender):
        print(f"{self.name}: RECV HELLO from {sender.name}")
        self.neighbors.add(sender.name)
    def print_neighbors(self):
        print(f"{self.name} neighbors: {list(self.neighbors)}")
class Router(Device):
    def __init__(self, name):
        super().__init__(name)

    def send_hello(self):
        print(f"{self.name}: Sending HELLO")
class Switch(Device):
    def __init__(self, name):
        super().__init__(name)
    def send_hello(self):
        print(f"{self.name}: Listening for HELLO")
