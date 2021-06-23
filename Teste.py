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

    if extencao == 'rs':
        print("Rust\n")
        os.system('rustc ' + path + problema + '/' + file + ' -o ' + path + problema + '/main-' + extencao)
        os.system('cd ' + path + problema + ' && ./main-' + extencao + ' && rm main-' + extencao)
        print("\n\n")

    if extencao == 'pas':
        print("Pascal\n")
        os.system('fpc ' + path + problema + '/' + file)
        os.system('cd ' + path + problema + ' && ./main && rm main.o main')
        print("\n\n")

    if extencao == 'ml':
        print("OCaml\n")
        os.system('ocamlc -o ' + path + problema + '/' + 'main-' + extencao + ' ' + path + problema + '/' + file)
        os.system('cd ' + path + problema + ' && ./main-' + extencao + ' && rm main-' + extencao + ' main.cmi main.cmo')
        print("\n\n")

    if extencao == 'hs':
        print("Haskell\n")
        os.system('ghc -o ' + path + problema + '/' + 'main-' + extencao + ' ' + path + problema + '/' + file)
        os.system(path + problema + '/' + nome_arquivo + '-' + extencao + ' && cd ' + path + problema + ' && rm ' + nome_arquivo + '-' + extencao + ' ' + nome_arquivo + '.o ' + nome_arquivo + '.hi')
        print("\n\n")
        
    if extencao == 'php':
        print("PHP\n")
        os.system('php ' + path + problema + '/' + file)
        print("\n\n")

    if extencao == 'rb':
        print("Ruby\n")
        os.system('ruby ' + path + problema + '/' + file)
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

    if extencao == 'c':
        print("C & C99")
        os.system('gcc -o ' + path + problema + '/' + 'main-' + extencao + ' ' + path + problema + '/' + file)
        os.system(path + problema + '/' + nome_arquivo + '-' + extencao + ' && rm ' + path + problema + '/' + nome_arquivo + '-' + extencao)
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

    if extencao == 'java':
        print("Java\n")
        os.system('javac ' + path + problema + '/' + file + ' -d ' + path + problema + '/' + 'Java')
        os.system('cd ' + path + problema + '/Java && java Main')
        os.system('rm -rfv ' + path + problema + '/' + 'Java')
        print("\n\n")

    if extencao == 'kt':
        print("Kotlin\n")
        os.system('kotlinc ' + path + problema + '/' + file + ' -include-runtime -d ' + path + problema + '/' + 'main-kt.jar')
        os.system('cd ' + path + problema + '/ && java -jar main-kt.jar')
        os.system('rm ' + path + problema + '/main-kt.jar')
        print("\n\n")

    if extencao == 'clj':
        print("Clojure\n")
        os.system('clj ' + path + problema + '/' + file)
        print("\n\n")

    if extencao == 'py':
        print("Python\n")
        os.system('python3 ' + path + problema + '/' + file)
        print("\n\n")

    if extencao == 'dart':
        print("Dart\n")
        os.system('dart ' + path + problema + '/' + file)
        print("\n\n")

print("Teste finalizado!\n")