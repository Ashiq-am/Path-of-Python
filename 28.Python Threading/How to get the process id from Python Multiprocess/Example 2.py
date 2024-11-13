import multiprocessing


def twos_multiple(x):
    proc = multiprocessing.Process()

    curr_proc = multiprocessing.current_process()

    print('current process:', curr_proc.name, curr_proc._identity)

    print('created process:', proc.name, proc._identity)

    return x * 2


pro = multiprocessing.Pool()

print(pro.map(twos_multiple, range(10)))
