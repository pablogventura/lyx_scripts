#!/usr/bin/env python
# -*- coding: utf8 -*-

empiezan = [r"\begin_inset"]
terminan = [r"\end_inset"]

no_va = False
texto = ""
while True:
    try:
        linea = raw_input("")
    except EOFError:
        break
    if any(p in linea for p in empiezan):
        no_va = True
    if any(p in linea for p in terminan):
        no_va = False
    if not no_va and not linea.startswith("\\") and not linea.startswith("#") and not linea.strip() == "":
        texto += linea

texto = texto.replace("\n","")
texto = texto.replace("\r","")

texto = texto.replace(".",".\n")

# aca en texto esta todo lo que es texto humano, sin grandes modificaciones

noquiero = ",.;:()[]{}/\\?!¿¡-_<>´'\""
for c in noquiero:
    texto = texto.replace(c," ")

palabras = texto.split()

cantidad = []
while palabras:
    p = palabras.pop()
    repeticiones = palabras.count(p)
    cantidad.append((p,repeticiones))
    for i in range(repeticiones):
        palabras.remove(p)

cantidad.sort(key=lambda t:int(t[1]),reverse=True)
cantidad = [(p,c) for (p,c) in cantidad if len(p) > 4 and c > 10]
for (p,c) in cantidad:
    print "%s\t%s" % (p,c)












