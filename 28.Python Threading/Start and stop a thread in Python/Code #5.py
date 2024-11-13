class IOTask:
    def terminate(self):
        self._running = False

        def run(self, sock):
            # sock is a socket

            # Set timeout period
            sock.settimeout(5)
            while self._running:

                # Perform a blocking I/O operation w/timeout
                try:
                    data = sock.recv(8192)
                    break
                except socket.timeout:
                    continue
                # Continued processing
                ...
            # Terminated

        return
