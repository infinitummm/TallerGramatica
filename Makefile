#!/usr/bin/make -f
# ==============================================================================
# Makefile Maestro - Quiz Sintáctico (Puntos 1, 2 y 3)
# Integrantes: Dylan Torres - Juan Gomez - Javier Rosero
# Lenguaje Objetivo: Python 3 con ANTLR 4
# ==============================================================================

PYTHON ?= python3

.PHONY: all generate run test punto1 punto2 punto3 clean help

all: generate run

generate:
	@echo "==> Generando código ANTLR 4 para todos los ejercicios..."
	@$(MAKE) -C Punto_1 generate
	@$(MAKE) -C Punto_2 generate
	@$(MAKE) -C Punto_3 generate
	@echo "==> Generación de código completa."

# Ejecutar los tres puntos en secuencia mediante run_all.py
run: generate
	@$(PYTHON) run_all.py

test: run

# Ejecución individual de cada punto
punto1:
	@$(MAKE) -C Punto_1 run

punto2:
	@$(MAKE) -C Punto_2 run

punto3:
	@$(MAKE) -C Punto_3 run

# Limpieza general de todos los ejercicios
clean:
	@echo "==> Limpiando todos los ejercicios..."
	@$(MAKE) -C Punto_1 clean
	@$(MAKE) -C Punto_2 clean
	@$(MAKE) -C Punto_3 clean
	@echo "==> Limpieza general finalizada."

help:
	@echo "Comandos disponibles en el Makefile Maestro:"
	@echo "  make         - Genera el código y ejecuta los 3 puntos secuencialmente"
	@echo "  make generate- Genera el código ANTLR 4 en todas las carpetas"
	@echo "  make run     - Mismo comportamiento que 'make'"
	@echo "  make punto1  - Ejecuta únicamente el Punto 1 (Diapositiva 11)"
	@echo "  make punto2  - Ejecuta únicamente el Punto 2 (Diapositiva 12 - Formas de AST)"
	@echo "  make punto3  - Ejecuta únicamente el Punto 3 (Diapositiva 15 - Prueba de Ambigüedad)"
	@echo "  make clean   - Limpia archivos autogenerados de todos los ejercicios"
