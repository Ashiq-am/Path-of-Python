""


"""
/* Existing file descriptor (already open) */
int fd;

PyObject* fobj = PyFile_FromFd(fd, "filename",
				"r", -1, NULL, NULL, NULL, 1);



"""