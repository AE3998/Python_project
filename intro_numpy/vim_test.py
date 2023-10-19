import numpy as np
from scipy.sparse import csr_array

d = np.arange(35).reshape(5, 7)
d[np.ix_([2, 3], [0, 2, 5])]
x = csr_array(np.arange(5))
print(csr_array(np.arange(5)))




"""
Cosar que quiero probar para borrar [Entre parentesis]
print(d) las esta y listo
print(d) amos a clisto
print(d) imos a  las esta y listo 
            print("uysentre las cosas, raras voya, copiar"AA) amos a esto probablemente es lo que me interesa
            dEntre las cosas raras voy a copiar

print(d)
print(d)
print(d)
rso para qe 
print(d)
print(d)
print
print
cosas que aprendi de Vim:
ciw, ci", ci( = change inner word, ", (), and etc.
yiw, yi", yi( = yank inner word, ", (), and etc.
diw, di", di( = delete inner word, ", (), and etc.
Por su puesto puedo combinar con las funciones para indicar hasta donde 
quiero borrar, cambiar y tdoo, como por ejemplo Shift+G, $ o Ctrl+4, gg.


num + y/

sustitite: ":s/ obj / destino [/g]

shift v, d
$ o Ctrl + 4 para final de una linea. 0 solo para el inicio de la linea. 
^ o Ctrl + 6 para 0+w, el inicio de la primer palabra.
% para salto entre {[()]}
Por su puesto puedo usar d% para borrar lo que esta  {[()]}

s parametros de salto esT yF, uno para llegar inmediatamente antes 
y otro sobre la misma palabra especificada. Por ejemplo quiero borrar las
palabras "hasta" *, uso dt*
/* cosas asi tan rara*/  
aplico dt*:
/* cosas */
Lo mismo pero busqueda hacia atras Shift + T o F.
:
busqueda 

# Otra funcionalidad es el "==" que equivale a Ctrl+L de Zinjai, alinea los 
# codigos apropiadamente segun su nivel de {}

# Navegacion, busqueda:
# Puedo usar / obj para buscar la palabra. Para navegar usar n, previo con Shift+n o N.
# O tambie Shift+/ o ?, para buscar en sentido contrario, lo cual n y N se invierten.
# Tranquilamente puedo posicionar a la palabra y usar # o Shift+3.

# Memorizar posicion:
# m [a-z]. En el caso de regresar la linea, usar '[a-z]

# Clipboard:
# Usar :reg para revisar lo que estan guardado en clipboard. 
# Antes de copiar algo (si esta seleccionado) o la linea uso "[num, a-z]y[y]  
# Antes de pegar uso "[num, a-z] p.
# regresar
# Por defecto lo que estan copiado estan guardado en la posicion "0.

# Copiar los instrucciones: qa [instrucciones] [esc] q
# Se usa @a para ejecutar las intrucciones 


Avanzado:

Ctrl-y Moves screen up one line
Ctrl-e Moves screen down one line
Ctrl-u Moves cursor & screen up ½ page
Ctrl-d Moves cursor & screen down ½ page
Ctrl-b Moves screen up one page, cursor to last line
Ctrl-f Moves screen down one page, cursor to first line
"""
This is 1st paragraph text.
2nd line also include text text text.
3rd line include text text text

This is 2nd paragraph text.
2nd line also include text text text.
3rd line include text text text
4th texalso include textt