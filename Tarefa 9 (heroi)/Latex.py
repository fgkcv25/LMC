# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 22:07:42 2019

@author: CLIENTE
"""

#pega o heroi.txt
with open('C:\\Users\\CLIENTE\\Desktop\\heroi.txt','r',encoding='utf8') as arquivo:
    dados = arquivo.readlines()
for i in range(len(dados)):
    dados[i] = dados[i].rstrip('\n').split(';')

#cria o arquivo.tex
latex = open('C:\\Users\\CLIENTE\\Desktop\\Relações Aluno-Nota.tex','w+')
latex.write('\\documentclass[12pt]{article} \n \
            \\usepackage[utf8]{inputenc} \n \
            \\usepackage{pgfplots} \
            \\begin{document} \n \
            \\section*{Tabela com as médias de cada aluno} \n \
            \\begin{tabular}{c|c} \n \
            Nome & Sobrenome \\\\ \n \
            \\hline \n')
#escolhi botar aquela expressão para a média das notas dos alunos pois ela é a
#que mais se assemelha ao sistema da ufsc de arredondamento,
#e também porque caso eu não arredondasse os números possuiriam muitas casas
#após a vírgula.
for i in range(1,len(dados)):
    latex.write('{} {} & {} \\\\ \n'.format(dados[i][0],dados[i][1],round(2*(float(dados[i][2])+float(dados[i][3])+float(dados[i][4]))/3)/2))
latex.write('\\end{tabular} \n')

#coloquei um for aqui para fazer os três gráficos com as notas de uma vez, que
#é menos trabalhoso que copiar e colar o código duas vezes e mudar os índices
for prova in range(2,5):
    latex.write('\\begin{center}\\begin{tikzpicture}\\begin{axis}[xbar,enlargelimits=0.10,width = \\textwidth,ytick=data,height=15cm,legend style={at={(0.5,-0.08)},anchor=north,legend columns=-1},xlabel={Nota},symbolic y coords={')
    for i in range(1,len(dados)):
        latex.write('{} {},'.format(dados[i][0],dados[i][1]))
    latex.write('}] \n \
    \\addplot coordinates {')
    for i in range(1,len(dados)):
        latex.write('({},{} {}) '.format(dados[i][prova],dados[i][0],dados[i][1]))
    latex.write('}; \n')
    latex.write('\\legend{{Prova {}}}\n'.format(prova-1))
    latex.write('\\end{axis} \n \\end{tikzpicture} \\end{center} \n')

#mas desta vez copiei e colei pois era mais simples que ter que colocar um if
#no for anterior
latex.write('\\begin{center}\\begin{tikzpicture}\\begin{axis}[xbar,enlargelimits=0.10,width = \\textwidth,ytick=data,height=15cm,legend style={at={(0.5,-0.08)},anchor=north,legend columns=-1},xlabel={Nota},symbolic y coords={')
for i in range(1,len(dados)):
    latex.write('{} {},'.format(dados[i][0],dados[i][1]))
latex.write('}] \n')
latex.write('\\addplot coordinates {')
for i in range(1,len(dados)):
    latex.write('({},{} {}) '.format(round((2*(float(dados[i][2])+float(dados[i][3])+float(dados[i][4]))/3)/2),dados[i][0],dados[i][1]))
latex.write('}; \n \
\\legend{{Média das provas}}\n \
\\end{axis} \n \\end{tikzpicture} \\end{center} \n \
\\end{document}')
latex.close()