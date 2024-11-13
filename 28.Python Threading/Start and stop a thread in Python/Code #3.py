t = Thread(target = countdown, args =(10, ), daemon = True)
t.start()
