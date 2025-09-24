# ---------------------------
# Makefile multi bahasa
# ---------------------------

# === JAVA ===
java-build:
	javac Main.java

java-run:
	java Main

java-run-all: java-build java-run


# === C++ ===
cpp-build:
	g++ main.cpp -o main

cpp-run:
	./main

cpp-run-all: cpp-build cpp-run


# === PYTHON ===
python-run:
	python3 main.py


# === ASSEMBLY (NASM, Linux x86-64) ===
asm-build:
	nasm -f elf64 hello.asm -o hello.o
	ld hello.o -o hello

asm-run:
	./hello

asm-run-all: asm-build asm-run


# === ALL LANGUAGES ===
all: java-run-all cpp-run-all python-run asm-run-all
