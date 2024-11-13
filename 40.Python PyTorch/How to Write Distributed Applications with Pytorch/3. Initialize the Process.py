def init_process(rank, size, backend='gloo'):
    """ Initialize the distributed environment. """
    dist.init_process_group(backend, rank=rank, world_size=size)
