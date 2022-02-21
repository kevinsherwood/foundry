import os
import shutil
import stat
import json
import csv

def make_dir(r):
    if not os.path.exists(r):
        print(f"  Creating {r}")
        os.mkdir(r)

def remove_directory(path):
    # remove a directory by moving it to _delete_timestamp
    prompt = input(f"Are you sure you wish to remove {path}? (Y/N) ")
    if prompt == "Y" or prompt == "y":
        delete_path = path + '_delete'
        if os.path.exists(delete_path):
            print (f'  deleting {delete_path}')
            shutil.rmtree(delete_path)
        shutil.move(path,path + '_delete')
        print (f"  {path} moved to {path+'_delete'}")
    else:
        print(f'  Aborting because directory already exists.')
        exit()

def read_csv(path):
    items = []
    with open(path, 'r') as data:
        for line in csv.DictReader(data):
            items.append(line)
    return items

def read_file(path):
    with open(path, 'r') as file:
        data = file.read().replace('\n', '')
    return data

def read_json(path):
    # read a json from a path
    with open(path) as f:
        j = json.load(f)
    return j

def write_json(path, j):
    # write a json to a path
    with open(path, 'w') as f:
        json.dump(j, f, indent=2)

def write_list_of_json_to_file(path,l):
    # write a list to a file
    with open(path, 'w') as fh:
        for item in l:
            j = json.dumps(item)
            fh.write(f'{j}\n')

def write_list_to_file(path, l):
    # write a list to a file
    with open(path, 'w') as fh:
        for item in l:
            fh.write(f'{item}\n')

def write_string_to_file(path, string):
    # write a string to a text file
    fh = open(path, "w")
    n = fh.write(string)
    fh.close()    
    
def write_dict_to_file(path, d):
    # this is a complete fuckup and is only writing a name=value
    with open(path, 'w') as fh:
        for k,v in d.items():
            fh.writelines(f"{k}={v}\n")

def read_dict_from_file(path):
    # This is a complete fuckup and is only reading in a name value
    with open(path) as f:
        content = [line.rstrip('\n') for line in f]
        # you may also want to remove whitespace characters like `\n` at the end of each line
        d = {x.split('=')[0] : x.split('=')[1] for x in content}
    return d


def make_executable(path):
    if os.path.exists(path):
        st = os.stat(path)
        os.chmod(path, st.st_mode | stat.S_IEXEC)        
    else:
        print(f'error in make_executable: path {path} does not exist')


def sign(i):
    if i < 0:
        return '-'
    else:
        return '+'

def make_aquamarine_wavelet_from_offsets(x, y):
    # make the x, y 5 digit strings with leading 0s
    return f"cmpovt_il{sign(y)}{abs(y):05}_xl{sign(x)}{abs(x):05}.wavelets"

def make_aquamarine_migrate_from_offsets(x, y):
    # make the x, y 5 digit strings with leading 0s
    return f"cmpovt_il{sign(y)}{abs(y):05}_xl{sign(x)}{abs(x):05}.migrate"

def make_gem_wavelet_bin_from_offsets(x, y):
    # make the x, y 5 digit strings with leading 0s
    return f"cmpovt_il{sign(y)}{abs(y):05}_xl{sign(x)}{abs(x):05}.wavelets.gem.tra.bin"

def make_gem_migrate_bin_from_offsets(x, y):
    # make the x, y 5 digit strings with leading 0s
    return f"cmpovt_il{sign(y)}{abs(y):05}_xl{sign(x)}{abs(x):05}.migrate.gem.tra.bin"

def make_gem_wavelet_json_from_offsets(x, y):
    # make the x, y 5 digit strings with leading 0s
    return f"cmpovt_il{sign(y)}{abs(y):05}_xl{sign(x)}{abs(x):05}.wavelets.gem.json"

def make_gem_migrate_json_from_offsets(x, y):
    # make the x, y 5 digit strings with leading 0s
    return f"cmpovt_il{sign(y)}{abs(x):05}_xl{sign(x)}{abs(x):05}.migrate.gem.json"

def make_gem_sbi_input_json_from_offsets(x, y):
    # make the x, y 5 digit strings with leading 0s
    return f"config_il{sign(y)}{abs(y):05}_xl{sign(x)}{abs(x):05}.sbi.gem.json"

def make_gem_sbi_trace_bin_from_offsets(x, y):
    # make the x, y 5 digit strings with leading 0s
    return f"config_il{sign(y)}{abs(y):05}_xl{sign(x)}{abs(x):05}.sbi.gem.tra.bin"

def make_gem_sbi_output_json_from_offsets(x, y):
    # make the x, y 5 digit strings with leading 0s
    return f"il{sign(y)}{abs(y):05}_xl{sign(x)}{abs(x):05}.sbi.gem.json"

def make_gem_generate_output_json_from_offsets(x, y):
    # make the x, y 5 digit strings with leading 0s
    return f"il{sign(y)}{abs(y):05}_xl{sign(x)}{abs(x):05}.generate.gem.json"

def make_gem_generate_output_bin_from_offsets(x, y):
    # make the x, y 5 digit strings with leading 0s
    return f"il{sign(y)}{abs(y):05}_xl{sign(x)}{abs(x):05}.generate.gem.gps.bin"

def make_aquamarine_wavelet_bin_from_offsets(x, y):
    # make the x, y 5 digit strings with leading 0s
    return f"cmpovt_il{sign(y)}{abs(y):05}_xl{sign(x)}{abs(x):05}.wavelets"

def make_aquamarine_header_bin_from_offsets(x, y):
    # make the x, y 5 digit strings with leading 0s
    return f"cmpovt_il{sign(y)}{abs(y):05}_xl{sign(x)}{abs(x):05}.migrate"

def make_dvbeam_wavelet_bin_from_offsets(x, y):
    # make the x, y 5 digit strings with leading 0s
    return f"cmpovt_il{sign(y)}{abs(y):05}_xl{sign(x)}{abs(x):05}_wavelets.gem.tra.bin"

def make_dvbeam_header_bin_from_offsets(x, y):
    # make the x, y 5 digit strings with leading 0s
    return f"cmpovt_il{sign(y)}{abs(y):05}_xl{sign(x)}{abs(x):05}_headers.gem.tra.bin"

def make_dvbeam_wavelet_json_from_offsets(x, y):
    # make the x, y 5 digit strings with leading 0s
    return f"cmpovt_il{sign(y)}{abs(y):05}_xl{sign(x)}{abs(x):05}_wavelets.gem.json"

def make_dvbeam_header_json_from_offsets(x, y):
    # make the x, y 5 digit strings with leading 0s
    return f"cmpovt_il{sign(y)}{abs(y):05}_xl{sign(x)}{abs(x):05}_headers.gem.json"

def get_offx_offy_from_filename(filename):
    # return the offx and offy from a filename
    # example: cmpovt_il+03400_xl+00400_migrate.gem.json
    words = filename.split('_')
    offy = int(words[1][2:])
    offx = int(words[2][2:])
    return offx, offy

