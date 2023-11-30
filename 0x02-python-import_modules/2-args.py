#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv)
    #print(arg_len)
    if arg_len == 1:
        args_len = 0
        print("{} arguments.".format(args_len))
    elif arg_len == 2:
        args_len = 1
        print("{} argument:".format(args_len))
        print("{}: {}".format(args_len,sys.argv[1]))
    else:
        args_len = arg_len -1
        print("{} arguments:".format(args_len))
        for arguement in range(1,arg_len):
            print("{}: {}".format(arguement, sys.argv[arguement]))
