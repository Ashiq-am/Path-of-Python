""""""



'''

bash % python3 setup.py build_ext --inplace
running build_ext
building '_sample' extension

gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes
-I/usr/local/include/python3.3m -c work_wrap.c
-o build/temp.macosx-10.6-x86_64-3.3/work_wrap.o

work_wrap.c: In function ‘SWIG_InitializeModule’:

work_wrap.c:3589: warning: statement with no effect

gcc -bundle -undefined dynamic_lookup build/temp.macosx-10.6-x86_64-3.3/work.o

build/temp.macosx-10.6-x86_64-3.3/work_wrap.o -o _work.so -lwork
bash %




'''