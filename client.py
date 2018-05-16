import bluelet

def connecho():
    c = yield bluelet.connect("192.168.1.10", 8000)
    while True:
        yield c.send("Diana are pofte".encode())
        data = yield c.recv(1024)
        print("SERVER:", data)
        #raw_input("HEY")

def main():
    yield bluelet.spawn(connecho())

bluelet.run(main())