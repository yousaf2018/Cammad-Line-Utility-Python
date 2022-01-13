import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y 
    elif args.o == 'sub':
        return args.x - args.y 
    elif args.o == 'mul':
        return args.x * args.y 
    elif args.o == 'div':
        return args.x / args.y 
    else:
        return "Something went wrong"
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1, help="Enter first number or Please contact yousaf2018@namal.edu.pk")
    parser.add_argument('--y', type=float, default=1, help="Enter second number or Please contact yousaf2018@namal.edu.pk")
    parser.add_argument('--o', type=str, default=1, help="This utility for calculation or Please contact yousaf2018@namal.edu.pk")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
