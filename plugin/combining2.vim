" MIT License.  Copyright © Peter Kenny
let s:path = substitute(expand('<sfile>:p:h'), '\\', '/', 'g')
command! C2d silent execute ":py3file " .. s:path .. "/combining2dec.py"
command! C2h silent execute ":py3file " .. s:path .. "/combining2hex.py"
command! C2p silent execute ":py3file " .. s:path .. "/combining2py.py"
