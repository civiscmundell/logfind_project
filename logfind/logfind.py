import sys
import optparse
import re
import os 

parser = optparse.OptionParser()
parser.add_option('-o', action="store_true", default=False)
parser.add_option('-i', dest='reglist_filepath', default=False) 

def get_reg_list(filepath):
    if filepath:
        with open(filepath) as f:
            reg_list = f.read().split()
    else:
        reg_list = ['.log$']
    return reg_list

def find_files(drc, regs):
    found_files = []
    for root, dirs, files in os.walk(drc):
        for name in files:
            reg_matches = [re.search(r, name) for r in regs]
            if any(reg_matches):
                found_files.append(os.path.join(root,name))
    return found_files

def find_pattern_matches(files, pats, or_match):
    matched = []
    for fi in files:
        with open(fi) as f:
            log_text = f.read()
            p_matches = [re.search(p, log_text) for p in pats]
            if (or_match and any(p_matches)) or all(p_matches):
                matched.append(fi)
    return matched

if __name__ == '__main__':
    options, args = parser.parse_args()
    p_list = args[0].split()
    reg_list = get_reg_list(options.reglist_filepath)
    found_logs = find_files(os.getcwd(), reg_list)
    matched_logs = find_pattern_matches(found_logs, p_list, options.o)
    print('\n'.join(matched_logs))
