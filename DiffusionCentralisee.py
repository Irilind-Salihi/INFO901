from mpi4py import MPI

comm = MPI.COMM_WORLD
me = comm.Get_rank()
size = comm.Get_size()


def broadcast(_from, msg):
    if me == _from:
        print("I'm <"+str(me)+">: send " + msg)
        for i in range(0, size):
            if i != _from:
                comm.send(msg, dest=i, tag=99)
    else:
        buf = comm.recv(source=0, tag=99)
        print("I'm <"+str(me)+">: receive " + buf)


msg = 'test'
broadcast(0,'test')