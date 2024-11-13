import multiprocessing
c = CountdownTask(5)
p = multiprocessing.Process(target = c.run)
p.start()
...
