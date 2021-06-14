#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
from os import walk


print('Informe o número do problema')
problema = input('')


path = './Problemas/'

# Pega todos os files.
filenames = next(walk(path + problema), (None, None, []))[2]

for file in filenames:

    nome_arquivo = file.split('.')[0] or ''
    extencao = file.split('.')[1] or ''

    if extencao == 'php':
        print("PHP\n")
        os.system('php ' + path + problema + '/' + file)
        print("\n\n")

    if extencao == 'js':
        print("JS\n")
        os.system('node ' + path + problema + '/' + file)
        print("\n\n")

    if extencao == 'lua':
        print("LUA\n")
        os.system('lua ' + path + problema + '/' + file)
        print("\n\n")

    if extencao == 'go':
        print("GO\n")
        os.system('go run ' + path + problema + '/' + file)
        print("\n\n")

    if extencao == 'cpp':
        print("C++\n")
        os.system('g++ -o ' + path + problema + '/' + 'main-' + extencao + ' ' + path + problema + '/' + file)
        os.system(path + problema + '/' + nome_arquivo + '-' + extencao + ' && rm ' + path + problema + '/' + nome_arquivo + '-' + extencao)
        print("\n\n")

    if extencao == 'cs':
        print("C#\n")
        os.system('mcs -out:' + path + problema + '/' + 'main-' + extencao + '.axe ' + path + problema + '/' + file)
        os.system('mono ' + path + problema + '/' + nome_arquivo + '-' + extencao + '.axe && rm ' + path + problema + '/' + nome_arquivo + '-' + extencao + '.axe')
        print("\n\n")

    if extencao == 'py':
        print("Python\n")
        os.system('python3 ' + path + problema + '/' + file)
        print("\n\n")

print("Teste finalizado!\n")