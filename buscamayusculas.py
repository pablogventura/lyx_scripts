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

t=texto.split("\n")
noson = ["A","CSP", "LADR", "GPL"]
t=[o for o in t if any(p.isupper() and len(p)>2 and p not in noson for p in o.split())]

for o in t:
    print o











