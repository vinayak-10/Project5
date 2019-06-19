import Demo as D
import random as rna


def key_gen(x: D .Teacher):
    return len(x.cursub)


"""def classnum(tec: D.Teacher, cou: D.Course) -> bool:
    """  # Check if a teacher has classes for 1 subject in more than 2 batches.
"""
     # assert isinstance(Demo.Course, cou)
    assert isinstance(D.Course.Sem, cou._sem[0])
    for i in tec.cursub:
        if tec.cursub.count(i) >= 3:
            """  # merge classes
"""
            while tec.cursub.count(i) > 1:
                tec.cursub.remove(i)
                var = i == cou._sem[0][1]


        # cou._sem[0].t_no
"""


def check1(tec: D.Teacher):
    """ Analyze if any teacher has more than 2 cur_sub. """
    return len(tec.cursub) > 2


def check2(cou1: D.Course.Sem, cou2: D.Course.Sem):
    """ Check if 2 classes/batches are to be merged. """
    if cou1.subs == cou2.subs:
        return cou1.tt
    return False


def check3(cur: D.Course.Sem):
    """ Check if a subject has required lecture and lab slots allotted. """
    count = 0
    co1 = 0
    for xn in cur.subs:
        for xl in cur.tt.keys():
            count = count + 1 if xn.code in cur.tt[xl] else count
            co1 = co1 + 1 if 'Lab' + xn.code in cur.tt[xl] else co1
            if count > 4 or co1 > 2:
                return xl
    if co1 == 2 and count == 4:
        return True
    elif co1 < 2 and count < 4:
        return 'N'


def selectday():
    """ Select pattern for a day. """
    days = ['M', 'T', 'W', 'Th', 'F', 'Sa']
    clas = ['lecs' * 3, 'labs']
    dc = {}
    for d in days:
        rna.shuffle(clas)
        dc[d] = clas
    return dc


def check_tea(ta, ch: D.Subject, tts: dict):
    """ Check for available teachers for a particular subject and allot one of them based on constraints. """
    tx = []
    s = []
    for i in range(len(ta)):
        if len(ta[i].cursub) >= 2:
            continue

        if ch.code in ta[i].subs:
            tx.append(ta[i])

    for k in tts.keys():
        if ch.code in tts[k]:
            s.append((k, tts[k].index(ch.code)))

    for co in tx:
        for v1, v2 in s:
            if co.slots[v1][v2] is not None:
                tx.remove(co)

    if len(tx) != 1:
        tx.sort(key=key_gen)
        ti = tx[:]
        tx = []
        for i in range(len(ti)):
            tx[i] = ti[i].subs.index(ch.code)
        n = min(tx)
        n = tx.index(n)
        for v1, v2 in s:
            ti[n].slots[v1][v2] = tts[v1][v2]
        return ti[n]
    for v1, v2 in s:
        tx[0].slots[v1][v2] = tts[v1][v2]
    return tx[0]
