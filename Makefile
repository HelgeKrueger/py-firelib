SRC := src

.DEFAULT_GOAL := ${SRC}/_firelib.so

${SRC}/_firelib.so : ${SRC}/fireLib.o ${SRC}/fireLib_wrap.o
	gcc -shared ${SRC}/fireLib.o ${SRC}/fireLib_wrap.o -o ${SRC}/_firelib.so -lpython3.10

${SRC}/fireLib.o : ${SRC}/fireLib.c
	gcc -c -fPIC -I/usr/include/python3.10 ${SRC}/fireLib.c -o ${SRC}/fireLib.o

${SRC}/fireLib_wrap.o : ${SRC}/fireLib_wrap.c
	gcc -c -fPIC -I/usr/include/python3.10 ${SRC}/fireLib_wrap.c -o ${SRC}/fireLib_wrap.o

${SRC}/fireLib_wrap.c ${SRC}/firelib.py: ${SRC}/fireLib.i ${SRC}/fireLib.h
	swig -python ${SRC}/fireLib.i