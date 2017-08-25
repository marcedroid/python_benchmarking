from multiprocessing import Process
from threading import Thread


def do_run():
    a, b = 0, 1
    for i in range(1000000):
        a, b = b, a * b


class Normal(object):
    def run(self):
        do_run()


class Hilos(Thread):
    def run(self):
        do_run()


class Procesos(Process):
    def run(self):
        do_run()


def ejecuta(iteraciones, tipo):
    funcs = list()
    if tipo == "normal":
        t_object = Normal
    elif tipo == "hilos":
        t_object = Hilos
    else:
        t_object = Procesos

    for i in range(int(iteraciones)):
        funcs.append(t_object())
    if tipo == "normal":
        for i in funcs:
            i.run()
    else:
        for i in funcs:
            i.start()
        for i in funcs:
            i.join()


def print_results(func, results):
    print("%-23s %4.6f segundos" % (func, results))


if __name__ == "__main__":
    from timeit import Timer

    print("Lanzando test")
    for i in range(1, 11):
        if i not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            continue
        t = Timer("ejecuta(%s, 'normal')" % i, "from __main__ import ejecuta")
        br = sum(t.repeat(repeat=100, number=1))
        print_results("normal (%s iteraciones)" % i, br)
        t = Timer("ejecuta(%s, 'hilos')" % i, "from __main__ import ejecuta")
        br = sum(t.repeat(repeat=100, number=1))
        print_results("hilos (%s hilos)" % i, br)
        t = Timer("ejecuta(%s, 'procesos')" % i, "from __main__ import ejecuta")
        br = sum(t.repeat(repeat=100, number=1))
        print_results("pocesos (%s procesos)" % i, br)
        print("\n")
    print("Test completado")