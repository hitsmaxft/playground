#!/usr/bin/env python

import sys

def  dictify_logline(line):
    split_line = line.split()
    sys.argv
    return{'remote':split_line[0],
            'status':split_line[8],
            'byte_sent':split_line[9]
            }

def generate_log_report(logfile):
    report_dict={};
    for line in logfile:
        line_dict=dictify_logline(line);
        print(line_dict);
        try:
            byte_sent=int(line_dict['byte_sent'])
        except ValueError:
            continue
        report_dict.setdefault(line_dict['remote'],[]).append(byte_sent)
    return report_dict
def main():
    if not len(sys.argv)>1:
        print(__doc__)
        sys.exit(1)
    infile_name=sys.argv[1]
    try:
        infile=open(infile_name,'r')
    except IOError:
        print('Error file to parse')
        print(__doc__)
        sys.exit(1)
    log_report = generate_log_report(infile)
    print(log_report)
    infile.close()

if __name__ == "__main__":
    main()





