import bluelet

def connecho():
    c = yield bluelet.connect("127.0.0.1", 8000)
    while True:
        yield c.send("Ana are mere".encode())
        data = yield c.recv(1024)
        print("SERVER:", data)
        #raw_input("HEY")

def main():
    yield bluelet.spawn(connecho())

bluelet.run(main())