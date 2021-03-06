'''
Write a function called sed that takes as arguments a pattern string,
a replacement string, and two filenames; it should read the first file
and write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the file, it should be
replaced with the replacement string.

If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message,
and exit.
Solution: http://thinkpython2.com/code/sed.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''


def sed(ps, rs, file1, file2):
    try:
        with open(file1, "r") as f:
            lines = f.read()
    except FileNotFoundError:
        print("Can't find this file. Please make sure it exist in this folder. ")
    else:
        newline = ""
        try:
            newline = lines.replace(ps, rs)
        except:
            pass
        else:
            try:
                with open(file2, "a") as fout:
                    fout.write("\n" + newline)
            except IndexError:
                print("Bad file!")


sed("Martin", "caden", "testing.txt", "new.txt" )
