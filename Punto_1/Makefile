#!/usr/bin/make -f
# ==============================================================================
# Makefile - Punto 1: Gramática Diapositiva 11 (Python 3)
# Integrantes: Dylan Torres - Juan Gomez - Javier Rosero
# ==============================================================================

ANTLR    ?= antlr4
PYTHON   ?= python3
GRAMMAR  := Expr11.g4

.PHONY: all generate run test interactive clean help

all: generate run

generate:
	@echo "==> Generando código ANTLR 4 en Python 3 para Punto 1..."
	$(ANTLR) -Dlanguage=Python3 -no-listener -visitor $(GRAMMAR)

run: generate
	@echo "==> Ejecutando pruebas de Punto 1..."
	$(PYTHON) main.py pruebas.txt

test: run

interactive: generate
	@echo "==> Iniciando modo interactivo por consola..."
	$(PYTHON) main.py

clean:
	@echo "==> Limpiando archivos autogenerados de Punto 1..."
	@rm -f Expr11Lexer.py Expr11Parser.py Expr11Visitor.py
	@rm -f Expr11.tokens Expr11.interp Expr11Lexer.tokens Expr11Lexer.interp
	@rm -rf __pycache__
	@echo "==> Limpieza de Punto 1 completada."

help:
	@echo "Comandos disponibles para Punto 1:"
	@echo "  make             - Genera el código ANTLR y ejecuta las pruebas automáticas"
	@echo "  make generate    - Genera el código Python desde Expr11.g4"
	@echo "  make run         - Ejecuta las pruebas desde pruebas.txt"
	@echo "  make interactive - Inicia la consola interactiva (REPL)"
	@echo "  make clean       - Elimina archivos generados y cachés"
