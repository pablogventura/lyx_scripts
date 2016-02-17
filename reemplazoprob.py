#!/usr/bin/env python
# -*- coding: utf8 -*-


texto = ""
while True:
    try:
        linea = raw_input("")
        texto += linea
    except EOFError:
        break


