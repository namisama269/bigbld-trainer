import random

from numpy import int32

from config import *

def get_buffer_index(pce_type):
    for i, piece in enumerate(pieces[pce_type]):
        if buffers[pce_type] in piece:
            break
    return i

def gen_letter_pair(pce_type):
    typed_pcs = pieces[pce_type]
    num_pcs = len(typed_pcs)

    # corner/edge/wings
    if pce_type in ('c','e','w'):
        p1 = random.choice(typed_pcs)
        while buffers[pce_type] in p1:
            p1 = random.choice(typed_pcs)
        p2 = random.choice(typed_pcs)
        while p1 == p2 or buffers[pce_type] in p2:
            p2 = random.choice(typed_pcs)
        t1 = random.choice(p1)
        t2 = random.choice(p2)

    # centres
    elif pce_type in ('x','t'):
        idxs = [i for i in range(num_pcs)]
        i1 = random.choice(idxs)
        idxs.remove(i1)
        i2 = random.choice(idxs)
        p1, p2 = typed_pcs[i1], typed_pcs[i2]
        while p1 == p2:
            p2 = random.choice(typed_pcs)
        t1 = random.choice(p1)
        while t1 == buffers[pce_type]:
            t1 = random.choice(p1)
        t2 = random.choice(p2)
        while t2 == buffers[pce_type]:
            t2 = random.choice(p2)
    
    return [t1, t2]


if __name__ == "__main__":
    pce_type = input("piece type: ")
    for i in range(3000):
        t1, t2 = gen_letter_pair(pce_type)
        print(f"{buffers[pce_type]} {t1} {t2}")