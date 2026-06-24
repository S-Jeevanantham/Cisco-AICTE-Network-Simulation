import time
from device import Router, Switch
def main():
    r0 = Router("Router0")
    r1 = Router("Router1")
    r2 = Router("Router2")
    s1 = Switch("Switch1")
    s2 = Switch("Switch2")
    devices = [r0, r1, r2, s1, s2]
    for d in devices:
        d.start()
    time.sleep(2)
    print("\n### PAUSE all devices")
    for d in devices:
        d.pause()
    time.sleep(2)
    print("\n### RESUME all devices")
    for d in devices:
        d.resume()
    time.sleep(2)
    print("\n=== Neighbor tables ===")
    for d in devices:
        if hasattr(d, "print_neighbors"):
            d.print_neighbors()
    time.sleep(2)
    print("\n### MTU TEST: send a too-big packet")
    r0.send_packet(2000)
    print("\n### FAULT: brought down link R0-R1")
    r0.neighbors.discard("Router1")
    r1.neighbors.discard("Router0")
    time.sleep(2)
    print("\n### STOPPING all devices")
    for d in devices:
        d.stop()
if __name__ == "__main__":
    main()

