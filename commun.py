class OneChapter(object):
    def __init__(self,chapter_title,exercice_filename):
        self.chapter_title=chapter_title
        self.exercice_filename=exercice_filename
        self.input_filename=self.smath_input_line().replace("\input{","").replace("}","").replace("\n","")
    def smath_input_line(self):
        smath_lines=open("smath.tex").readlines()
        for i,l in enumerate(smath_lines):
            if self.chapter_title in l:
                line=i
        return smath_lines[line+1]
    def count_exo(self,text,i_line):
        """
        return the number of \Exo in 'text' from the beginning and the line number 'i_line'.
        """
        lines=text.split("\n")[0:i_line]
        n=0
        for l in lines:
            ll=l.replace(" ","")
            if ll.startswith("\Exo"):
                n=n+1
        return n
    def exercice_lines(self,filename):
        el=open(filename).readlines()
        for i,l in enumerate(el):
            if self.chapter_title in l:
                i_line=i+1
        f_line=i_line+1
        while "\section" not in el[f_line] and "\end{document}" not in el[f_line] :
            f_line=f_line+1
        f_line=f_line-1
        exo=self.count_exo("".join(el),i_line)
        sublist=["\setcounter{{CountExercice}}{{{}}}".format(exo)]
        sublist.extend(el[i_line:f_line])
        return "".join(sublist)
    def write_the_file(self,filename="automatedChapter.tex"):
        generic_lines="".join(open("genericChapter.tex").readlines())
        text=generic_lines.replace("TITRE_CHAPITRE",self.chapter_title).replace("LES_INPUT",self.smath_input_line()).replace("LISTE_EXERCICES",self.exercice_lines(self.exercice_filename))
        f=open(filename,'w')
        f.write(text)
        f.close()
    def set_filename(self,medicament):
        medicament.new_output_filename="0-chapitre_"+self.chapter_title.replace(' ',"_")+".pdf"
    def ok_filenames_list(self):
        a=["e_smath"]
        a.append(self.input_filename)
        return a

class TheDS(object):
    def __init__(self,DS_id,group,nPAI):
        """
        'nPAI' is the number of copies that have to be printed in larger size.
        """
        self.DS_id=DS_id
        self.group=group
        self.filename="DSs.tex"
        self.nPAI=nPAI
        self._latex_portion=None
        self.tex_filename=self.DS_id+".tex"
    def latex_portion(self):
        if not self._latex_portion :
            el=open(self.filename).readlines()
            for i,l in enumerate(el):
                if self.DS_id in l:
                    i_line=i+1
            f_line=i_line+1
            while "\end{feuilleDS}" not in el[f_line] :
                f_line=f_line+1
            f_line=f_line+1
            self._latex_portion="".join(el[i_line:f_line])
        return self._latex_portion
    def latex_total(self):
        code=""
        n=len(self.group.student_list)+2    # J'en ai alors 2 en trop.
        for i in range(0,n) :
            code=code+"\n\\newpage\n"+self.latex_portion()+"\n"
        code=code+"\n\\LARGE\n"
        for i in range(0,self.nPAI):
            code=code+"\n\\newpage\n"+self.latex_portion()+"\n"
        return code
    def write_the_file(self):
        generic_lines="".join(open("genericDS.tex").readlines())
        text=generic_lines.replace("LES_FEUILLES",self.latex_total())
        f=open(self.tex_filename,'w')
        f.write(text)
        f.close()
    def set_filename(self,medicament):
        medicament.new_output_filename="0-"+self.DS_id+".pdf"
    def ok_filenames_list(self):
        a=["e_smath"]
        a.append("automatedDS")
        return a
