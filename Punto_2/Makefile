#!/usr/bin/make -f
# ==============================================================================
# Makefile - Punto 2: Comprobación de Formas de AST (Diapositivas 12-14)
# Integrantes: Dylan Torres - Juan Gomez - Javier Rosero
# ==============================================================================

ANTLR    ?= antlr4
PYTHON   ?= python3
GRAMMAR  := Expr12.g4

.PHONY: all generate run test clean help

all: generate run

generate:
	@echo "==> Generando código ANTLR 4 en Python 3 para Punto 2..."
	$(ANTLR) -Dlanguage=Python3 -no-listener -visitor $(GRAMMAR)

run: generate
	@echo "==> Ejecutando comprobación de formas de AST (Punto 2)..."
	$(PYTHON) main.py

test: run

clean:
	@echo "==> Limpiando archivos autogenerados de Punto 2..."
	@rm -f Expr12Lexer.py Expr12Parser.py Expr12Visitor.py
	@rm -f Expr12.tokens Expr12.interp Expr12Lexer.tokens Expr12Lexer.interp
	@rm -rf __pycache__
	@echo "==> Limpieza de Punto 2 completada."

help:
	@echo "Comandos disponibles para Punto 2:"
	@echo "  make          - Genera el código ANTLR y ejecuta la comprobación del AST"
	@echo "  make generate - Genera el código Python desde Expr12.g4"
	@echo "  make run      - Ejecuta el script de demostración de AST"
	@echo "  make clean    - Elimina archivos generados y cachés"
