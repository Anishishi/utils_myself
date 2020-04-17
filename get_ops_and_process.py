import argparse
# to do this
# python3 get_ops_and_process.py hey --flag --d_value wow ...


# create objects
parser = argparse.ArgumentParser()

# set args
# requirement argument
parser.add_argument("input", help="please set me", type=str)

# '--' mean optional argument
# 'python --flag' mean 'True'. Otherwise, 'False'
parser.add_argument("--flag", help="optional", action="store_true")
# 'help' show you the help strings when you python 'script' -h

parser.add_argument("--d_value", help="this parameter has default value", default='this is default.')

# you can only select these words.
parser.add_argument('--fruit', choices=['apple', 'banana', 'orange'])

# can get many values 'green yellow blue'...
parser.add_argument('--colors', nargs='*')

# this params is required.
parser.add_argument("--a_req", required=True)

args = parser.parse_args()

# get value
print(args.input)
print(args.flag)
print(args.d_value)
print(args.fruit)
print(args.colors)
print(args.a_req)