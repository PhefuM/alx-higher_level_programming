#!/usr/bin/python3
if __name == "__main__":
    import hidden_4
    for name in dir(hidden_4):
        if name[0] != '-' and name[1] != '_':
            print(name)