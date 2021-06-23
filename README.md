# URI

Teste com C
    gcc - main-c main.c
    ./main-c


Teste com C#

    sudo apt install mono-mcs -y
    mcs -out:main-cs.exe main.cs
    mono main-cs.exe


Teste com C++

    g++ -out:main-cpp.exe main.cpp
    ./main-cpp


Teste com GO

    sudo snap install go --classic
    go run main.go


Teste com Lua

    sudo apt install lua5.2
    lua main.lua

Teste com Clojure

    sudo apt install rlwrap
    clj main.clj

Teste com Haskell

    sudo apt install ghc
    ghc -o main-hs main.hs
    ./main-hs

Teste com Kotlin

    sudo snap install --classic kotlin
    kotlinc main.kt -include-runtime -d main-kt.jar
    java -jar main-kt.jar

Teste com ocaml
    
    sudo apt install ocaml-nox -y
    ocamlc -o main-ml main.ml
    ./main-ml

Teste com Pascal
    
    sudo apt install fp-compiler-3.0.4 -y
    fpc main.pas

Teste com Rust
    
    sudo apt install rustc -y
    rustc main.rs
    ./main-rs

Teste com Ruby

    sudo apt install ruby -y
    ruby main.rb