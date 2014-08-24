#!/usr/bin/env python

'''
 Reads a html export of bookmarks and prints out the line numbers of
 the duplicate urls in the file.
'''

__author__ = "Samantha Hewamanage"
__email__ = "samantha@fnal.gov"

import sys

debug = False    # controls print statements


def main(argv):
    if debug:
        print('got args=', argv)

    if len(argv) != 2:
        print("Need only one argument, a text/html file name containing your bookmarks!")
        return 1

    fp = open(argv[1])
    lineno = 0
    dups_dic = {}

    for line in fp.readlines():
        lineno += 1
        if debug:
            print('\t', line)

        if 'HREF' in line:  # a URL is found
            if debug:
                print(line)

            words = line.split()
            for wd in words:
                if 'HREF' in wd:
                    if debug:
                        print(wd)

                    if wd in dups_dic.keys():
                        (dups_dic[wd]).append(lineno)
                    else:
                        dups_dic[wd] = [lineno]

    tot_dups = sum([len(v) for v in dups_dic.values() if len(v) > 1])
    print('\n Found ', tot_dups, ' duplicate URLS out of ', lineno, ' in ', fp.name)
    print('Line Numbers -> URL')

    for k, v in dups_dic.items():
        if len(v) > 1:
            print(v, '->', k)

    print('\n')


if __name__ == "__main__":
    main(sys.argv)