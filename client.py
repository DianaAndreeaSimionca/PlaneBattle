import bluelet


def connecho():
    c = yield bluelet.connect("127.0.0.1", 8000)

    game_finish = False
    while ~game_finish:
        yield c.send("Ana are mere".encode())
        data = yield c.recv(1024)
        print("SERVER:", data.decode('utf-8'))


def main():
    yield bluelet.spawn(connecho())


bluelet.run(main())
