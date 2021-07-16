{ pkgs ? import <nixpkgs> {} }:

let
  pyPkgs = python-packages: with python-packages; [ pygame shapely ];
  python = pkgs.python3.withPackages pyPkgs;
in pkgs.writeScriptBin "lander" ''
   ${python}/bin/python ${./.}/lander.py
''
