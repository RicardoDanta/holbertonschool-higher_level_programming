#!/usr/bin/python3
def no_c(my_string):
    listastr = list(my_string)
    for i in listastr:
        while 'c' in listastr:
            listastr.remove('c')
        while 'C' in listastr:
            listastr.remove('C')
        my_string = "".join(str(i) for i in listastr)
    return my_string
