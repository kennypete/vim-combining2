# combining2hex.py - runs from within Vim on the current buffer with:
# :py3file {path}combining2hex.py
# (Set environment variable PYTHONIOENCODING to utf-8)
# The new buffer created changes combining characters to:
#   '&#x' [0-9A-F]+ ';'
import unicodedata, vim
result = ""
for line in vim.current.buffer:
    sline = ""
    for c in line:
        if unicodedata.category(c)[0] == 'M': # combining marks Mc, Me, and Mn
            # replace c with hexadecimal '&#x' [0-9A-F]+ ';'
            sline += c.replace(c, "&#x" + hex(ord(c))[2:].upper() + ';')
        else:
            # leave c unchanged
            sline += c
    result += sline + "\n"
vim.command("let @* = '" + result.replace("'", "''") + "'")
vim.command(':vsp | enew | norm "*PGdd') # Put replacement text in new buffer
