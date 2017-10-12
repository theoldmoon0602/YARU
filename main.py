#!/usr/bin/env python3
from dateutil.parser import parse
import os
import sys
import json

class Farenda(object):
    def __init__(self, teksto, limdato=None):
        self.teksto = teksto
        try:
            self.limdato = parse(limdato).strftime('%Y/%m/%d')
        except:
            self.limdato = None

def datumoAlFarenda(datumo):
    return Farenda(
            datumo['teksto'],
            datumo['limdato']
            )

def farendaAlDatumo(farenda):
    return {
            'teksto': farenda.teksto,
            'limdato': farenda.limdato
            }

def aldoniFarendan():
    teksto = input("teksto:")
    limdato = input("limdato:")

    farenda = Farenda(teksto, limdato)
    return farenda

def finiFarendan(farendaj, teksto):
    novaFarenaj = []
    for farenda in farendaj:
        if teksto == farenda.teksto:
            continue
        novaFarenaj.append(farenda)
    return novaFarenaj

def montriFarendajn(farendaj):
    for farenda in farendaj:
        print(farenda.teksto, end="")
        if farenda.limdato is not None:
            print(" --> limdato is {}".format(farenda.limdato), end="")
        print()


def main():
    farendaj = []
    vojo = os.environ.get("YARU_FILE", "~/.yaru")

    # sxargxi datumoj de dosiero
    if os.path.exists(vojo):
        with open(vojo, "r") as dosiero:
            datumoj = json.load(dosiero)
        for datumo in datumoj:
            farendaj.append(datumoAlFarenda(datumo))

    if len(sys.argv) <= 1:
        montriFarendajn(farendaj)
    elif sys.argv[1] == "aldoni":
        farenda = aldoniFarendan()
        farendaj.append(farenda)
    else:
        farendaj = finiFarendan(farendaj, sys.argv[1])

    # konservi farendaj en dosiero
    datumoj = []
    for farenda in farendaj:
        datumoj.append(farendaAlDatumo(farenda))
    with open(vojo, "w") as dosiero:
        json.dump(datumoj, dosiero, ensure_ascii=False)



main()
