import argparse
import os
import glob
import shutil
import random

def die(string):
    print(string)
    exit(1)

class Options:
    def __init__(self):
        self.initialized=False

    def initialize(self,parser):
        parser.add_argument("--input_data_folder", type=str, required=True, help="ex)./data/original")
        parser.add_argument("--dir_type", type=str, required=True,
            help="[onlyfiles, inputDir_and_annoDir], if [inputDir_and_annoDir], the size of each dir must be same.")
        parser.add_argument("--output_data_folder", type=str, default="any", help="ex)./dataset :if any, output folder will be made below the input folder")
        parser.add_argument("--divide_ratio", type=str, default="0.6,0.2,0.2", help="[train,val,test] sum don't need 1")

        self.initialized=True
        return parser

    def gather_options(self):
        if not self.initialized:  # check if it has been initialized
            parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
            parser = self.initialize(parser)

        self.parser=parser
        return parser.parse_args()

    def print_options(self, opt):
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
        opt = self.gather_options()
        self.print_options(opt)

        self.opt = opt
        return self.opt

def split_data_to_trainvaltest(opt):
    in_path=opt.input_data_folder #get from this folder
    out_path=opt.output_data_folder #create this folder
    dirtype=opt.dir_type
    ratios_str=opt.divide_ratio.split(',')
    ratios=[float(n) for n in ratios_str]
    Sum=sum(ratios)
    train_ratio=float(ratios[0])/Sum
    val_ratio=float(ratios[1])/Sum
    test_ratio=float(ratios[2])/Sum

    if out_path=="any":
        out_path="./Mydataset"

    try:
        os.mkdir(out_path)
    except FileExistsError:
        die(out_path + " exists")
    
    if dirtype=="onlyfiles":
        files=glob.glob(os.path.join(in_path,'*'))
        num_files=len(files)

        try:
            train_dir = os.path.join(out_path, 'train')
            val_dir = os.path.join(out_path, 'val')
            test_dir = os.path.join(out_path, 'test')
            os.mkdir(train_dir)
            os.mkdir(val_dir)
            os.mkdir(test_dir)
        except FileExistsError:
            die("train, val or test folder exist")

        random.shuffle(files)
        for i, file_path in enumerate(files):
            filename=os.path.basename(file_path)
            if i<num_files*train_ratio:   
                dst_path=os.path.join(train_dir, filename) #connect train_dir_path and filename
            elif i<num_files*(train_ratio+val_ratio):
                dst_path=os.path.join(val_dir, filename)
            else:
                dst_path=os.path.join(test_dir, filename)
            shutil.copyfile(file_path, dst_path)
    elif dirtype=="inputDir_and_annoDir":
        dirlist = []
        for f in os.listdir(in_path):
            if os.path.isdir(os.path.join(in_path, f)):
                dirlist.append(f)
        
        if len(dirlist)!=2:
            die("this dataset must have two dirs for input and anno.")
        
        train_dir=list()
        val_dir=list()
        test_dir=list()
        for i in range(2):
            try:
                train_dir.append(os.path.join(out_path, dirlist[i], 'train'))
                val_dir.append(os.path.join(out_path, dirlist[i], 'val'))
                test_dir.append(os.path.join(out_path, dirlist[i], 'test'))
                os.mkdir(os.path.join(out_path, dirlist[i]))
                os.mkdir(train_dir[i])
                os.mkdir(val_dir[i])
                os.mkdir(test_dir[i])
            except FileExistsError:
                die("train, val or test input folder exist")
            
        files=glob.glob(os.path.join(in_path,dirlist[0],'*'))
        num_files=len(files)
        random.shuffle(files)
        for i, file_path in enumerate(files):
            filename=os.path.basename(file_path)

            if i<num_files*train_ratio:   
                dst_path0=os.path.join(train_dir[0], filename) #connect train_dir_path and filename
                dst_path1=os.path.join(train_dir[1], filename)
            elif i<num_files*(train_ratio+val_ratio):
                dst_path0=os.path.join(val_dir[0], filename)
                dst_path1=os.path.join(val_dir[1], filename)
            else:
                dst_path0=os.path.join(test_dir[0], filename)
                dst_path1=os.path.join(test_dir[1], filename)
            shutil.copyfile(os.path.join(in_path,dirlist[0],filename), dst_path0)
            shutil.copyfile(os.path.join(in_path,dirlist[1],filename), dst_path1)

if __name__ == "__main__":
    opt=Options().parse()
    split_data_to_trainvaltest(opt)
    print("end")