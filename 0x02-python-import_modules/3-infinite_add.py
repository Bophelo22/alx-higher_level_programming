#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv)
    sum = 0
    for arguement in sys.argv[1:]:
        sum += int(arguement)

print("{}".format(sum))
