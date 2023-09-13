from mpi4py import MPI

comm = MPI.COMM_WORLD
me = comm.Get_rank()
size = comm.Get_size()

def broadcast(_from, msg):
    last = (_from + size -1) % size
    next = (me + 1) % size
    prev = (me - 1 + size) % size
    if me == _from:
        comm.send(msg, dest=next, tag=75)
        print("I'm <"+str(me)+">: send " + msg)
    else:
        buf = comm.recv(source=prev, tag=75)
        print("I'm <"+str(me)+">: receive " + buf)
        if(me != last):
            comm.send(buf, dest=next, tag=75)
            print("I'm <"+str(me)+">: sent " + buf)



msg = 'test'
broadcast(0,'test')