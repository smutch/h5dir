#!/usr/bin/env python
from __future__ import unicode_literals, print_function
import os
import sys
from functools import partial
import h5py as h5
from termcolor import colored

_color_value = partial(colored, color='yellow')
_color_group = partial(colored, color='magenta')
_color_info = partial(colored, color='grey', attrs=['bold'])

def walk(k, v, depth=0):
    try:
        yield from walk(k, v.attrs, depth)
    except AttributeError:
        pass
    try:
        for ik, iv in v.items():
            if type(v) is h5.AttributeManager:
                name = 'ª {}'.format(ik)
            else:
                name = '{}'.format(ik)
            name = name.lstrip('/')
            yield name, iv, depth
            try:
                yield from walk(ik, iv, depth+1)
            except AttributeError:
                pass
    except AttributeError:
        pass


def main():
    fname = os.path.expandvars(os.path.expanduser(sys.argv[1]))
    fd = h5.File(fname, 'r')
    for k, v , d in walk('/', fd):
        if type(v) is h5.Group:
            print("{}{} ⤵︎".format(d*'  ', _color_group(k)))
        else:
            try:
                info = "{} | {}".format(_color_info(v.dtype), _color_info(v.shape))
                if v.shape is ():
                    info += ' | {}'.format(_color_value(v.value))
            except AttributeError:
                info = _color_value('{}'.format(v))
            print("{}{} ➪ {}".format(d*'  ', k, info))
    fd.close()


if __name__ == "__main__":
    main()
