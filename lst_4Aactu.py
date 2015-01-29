#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools
import commun

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="automatedChapter.tex"


def set_filename(medicament):
    medicament.new_output_filename="0-actu4A.pdf"

pythagore=commun.OneChapter("Égalité de Pythagore","4A")
propo=commun.OneChapter("Grandeurs proportionnelles","4A")
trig_para=commun.OneChapter("Droite des milieux","4A")
ops_fract=commun.OneChapter("Opérations en écriture fractionnaire","4A")
thales=commun.OneChapter("Théorème de Thalès","4A")
manip_litt=commun.OneChapter("Manipulations littérales","4A")

actu4=trig_para
actu4=ops_fract
actu4=thales
actu4=manip_litt
actu4.set_filename=set_filename
actu4.write_the_file()

myRequest.add_plugin(actu4.set_filename,"medicament")
myRequest.ok_filenames_list=actu4.ok_filenames_list()
