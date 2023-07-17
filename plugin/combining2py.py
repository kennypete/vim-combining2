# combining2py.py - runs from within Vim on the current buffer with:
# :py3file {path}combining2.py
# (Set environment variable PYTHONIOENCODING utf-8)
# The new buffer created changes combining chars to:
#   "\u" [0-9a-z]{4}
# or
#   "\U" [0-9a-z]{8} (for > U+10000)
import unicodedata, vim
result = ""
for line in vim.current.buffer:
    sline = ""
    for c in line:
        if unicodedata.category(c)[0] == 'M': # combining marks Mc, Me, and Mn
            # replace c with \\{hexadecimal} notation
            if len(hex(ord(c))[2:]) > 4:
                # replace c with Python "\u" [0-9a-z]{4}
                sline += c.replace(c, "\\U" + hex(ord(c))[2:].zfill(8))
            else:
                # replace c with Python "\U" [0-9a-z]{8}
                sline += c.replace(c, "\\u" + hex(ord(c))[2:].zfill(4))
        else:
            # leave c unchanged
            sline += c
    result += sline + "\n"
vim.command("let @* = '" + result.replace("'", "''") + "'")
vim.command(':vsp | enew | norm "*PGdd') # Put replacement text in new buffer
