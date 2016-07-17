"""
Imagine you wanted to reimplement "head" and "grep" in python.  Here's a first cut:
"""

def head(max_lines, filenames):
    lines = getlines(filenames)
    for i in range(max_lines):
        print(next(lines))


def grep(needle, filenames):
    lines = getlines(filenames)
    for line in lines:
        if needle in line:
            print(line, end='')

"""
There's a lot of duplicated code there!  Now we could build a helper function like this:
"""

def getlines(filenames):
    for fn in filenames:
        with open(fn) as f:
            for line in f:
                yield line

"""
but then head would be inefficient, because getlines always reads every single line in the file.

Find out how to use a generator to make a version of getlines that is "lazy"

More info here: http://anandology.com/python-practice-book/iterators.html
"""
print('\nGREP\n')
grep("class", ["magic_methods.py"])
print('\nHEAD\n')
head(10,['magic_methods.py'])