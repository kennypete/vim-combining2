# combining2dec.py - runs from within Vim on the current buffer with:
# :py3file {path}combining2dec.py
# (Set environment variable PYTHONIOENCODING utf-8)
# The new buffer created changes combining characters to:
#   '&#' [0-9]+ ';'
import unicodedata, vim
result = ""
for line in vim.current.buffer:
    sline = ""
    for c in line:
        if unicodedata.category(c)[0] == 'M': # combining marks Mc, Me, and Mn
            # replace c with decimal '&#' [0-9]+ ';'
            sline += c.replace(c, "&#" + str(ord(c)) + ';')
        else:
            # leave c unchanged
            sline += c
    result += sline + "\n"
vim.command("let @c = '" + result.replace("'", "''") + "'")
vim.command(':vsp | enew | norm "cPGdd') # Put replacement text in new buffer
