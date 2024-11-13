""


"""


bash % python3 setup.py build_ext --inplace
running build_ext

cythoning work.pyx to work.c
building 'work' extension

gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes
-I/usr/local/include/python3.3m -c work.c
-o build/temp.macosx-10.6-x86_64-3.3/work.o

gcc -bundle -undefined dynamic_lookup build/temp.macosx-10.6-x86_64-3.3/work.o
-L. -lwork -o work.so
bash %


"""