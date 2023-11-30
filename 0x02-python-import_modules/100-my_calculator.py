#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add,sub,mul,div
    arg_len = len(sys.argv[1:])
    operator = ['+', '-', '*', '/']
    results = " "
    print(arg_len)
    if arg_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if sys.argv[2] not in operator:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            op = sys.argv[2]
            if sys.argv[2] == '+':
                sum = add(a,b)
                results = "{} {} {} = {}".format(a,op,b,sum)
            elif sys.argv[2] == '-':
                difference = sub(a,b)
                results = "{} {} {} = {}".format(a,op,b,difference)
            elif sys.argv[2] == '*':
                product = mul(a,b)
                results = "{} {} {} = {}".format(a,op,b,product)
            else:
                division = div(a,b)
                results = "{} {} {} = {}".format(a,op,b,division)
            print(results)
