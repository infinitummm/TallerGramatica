#!/usr/bin/make -f
# ==============================================================================
# Makefile - Punto 3: Prueba de Ambigüedad (Diapositivas 15-17)
# Integrantes: Dylan Torres - Juan Gomez - Javier Rosero
# ==============================================================================

ANTLR    ?= antlr4
PYTHON   ?= python3
GRAMMAR1 := AmbiguousExpr.g4
GRAMMAR2 := AmbiguousExprAlt.g4

.PHONY: all generate run test clean help

all: generate run

generate:
	@echo "==> Generando código ANTLR 4 en Python 3 para Punto 3..."
	$(ANTLR) -Dlanguage=Python3 -no-listener -visitor $(GRAMMAR1)
	$(ANTLR) -Dlanguage=Python3 -no-listener -visitor $(GRAMMAR2)

run: generate
	@echo "==> Ejecutando prueba de ambigüedad (Punto 3)..."
	$(PYTHON) main.py

test: run

clean:
	@echo "==> Limpiando archivos autogenerados de Punto 3..."
	@rm -f AmbiguousExprLexer.py AmbiguousExprParser.py AmbiguousExprVisitor.py
	@rm -f AmbiguousExpr.tokens AmbiguousExpr.interp AmbiguousExprLexer.tokens AmbiguousExprLexer.interp
	@rm -f AmbiguousExprAltLexer.py AmbiguousExprAltParser.py AmbiguousExprAltVisitor.py
	@rm -f AmbiguousExprAlt.tokens AmbiguousExprAlt.interp AmbiguousExprAltLexer.tokens AmbiguousExprAltLexer.interp
	@rm -rf __pycache__
	@echo "==> Limpieza de Punto 3 completada."

help:
	@echo "Comandos disponibles para Punto 3:"
	@echo "  make          - Genera el código ANTLR y ejecuta la prueba de ambigüedad"
	@echo "  make generate - Genera el código Python para ambas gramáticas"
	@echo "  make run      - Ejecuta la comparación de los dos árboles de derivación"
	@echo "  make clean    - Elimina archivos generados y cachés"
