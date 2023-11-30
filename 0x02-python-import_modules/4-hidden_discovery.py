#!/usr/bin/python3
if __name__ == "__main__":
    filename = 'hidden_4'
    # Print sorted name from directory
    for name in sorted(dir(filename)):
        # print only names that do not start with __
        if name[:2] != '__':
            print("{}".format(name))
