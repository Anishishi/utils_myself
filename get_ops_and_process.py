import argparse
# to do this
# python3 get_ops_and_process.py hey --flag --d_value wow --a_req req ...

class Options:
    def __init__(self):
        self.initialized=False

    def initialize(self,parser):
        # set args(define the options)
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

        self.initialized=True
        return parser

    def gather_options(self):
        #create parser object, gather_options and return options
        if not self.initialized:  # check if it has been initialized
            parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
            parser = self.initialize(parser)

        self.parser=parser
        return parser.parse_args()

    def print_options(self, opt):
        """Print options
        It will print default options values.
        """
        message = ''
        message += '----------------- Options ---------------\n'
        for k, v in sorted(vars(opt).items()):
            comment = ''
            default = self.parser.get_default(k)
            if v != default:
                comment = '\t[default: %s]' % str(default)
            message += '{:>25}: {:<30}{}\n'.format(str(k), str(v), comment)
        message += '----------------- End -------------------'
        print(message)

    def parse(self):
        """parser our options"""
        opt = self.gather_options()
        self.print_options(opt)

        self.opt = opt
        return self.opt


if __name__ == "__main__":
    # create objects
    opt=Options().parse()