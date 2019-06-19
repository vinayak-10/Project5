import random as rn
import Demo as D
import Demo1 as D1

cur_sem = True  # True for odd sem and False for even sem; Set by asking user
co = [D.Course(name='BCA', semno=6, lvl='UG'), D.Course(name='MCA', semno=6, lvl='PG'),
      D.Course(name='MSc', semno=4, lvl='PG'), D.Course(name='MBA', semno=4, lvl='PG')]
prio = {0: [], 1: [], 2: [], 3: []}
prio1 = {0: [], 1: [], 2: [], 3: []}
teac = [D.Teacher()]
ken = list(prio.keys())
ken.reverse()
days = ['M', 'T', 'W', 'Th', 'F', 'S']


def inp():
    print("Enter subjects for BCA, MCA, MSc and MBA respectively.")
    for i in range(0, 4):
        for j in range(0, 6):
            for k in range(0, 7):
                print('Enter Subjects for sem %d of %s one by one:' % (j, co[i].cour['Name']))
                co[i].sem[j].subs[k] = D.Subject()
                co[i].sem[j].subs[k].code = input('Code of subject')
                co[i].sem[j].subs[k].title = input("Title of Subject")
                co[i].sem[j].subs[k].lecs = input('No. of lectures per week for the subject')
                co[i].sem[j].subs[k].lab = input('No. of labs per week for the subject')
                co[i].sem[j].subs[k].imp = input('Priority of subject w.r.t. other subjects in the sem')


    while True:
        while True:
            tci = input('Enter sub taught by teacher')
            tc = [tci]
            x = input()
            if x == 0:
                break
        tx = D.Teacher(tc)
        tx.det['Name'] = input('Enter name of teacher')
        tx.det['ID'] = input('Enter college id of teacher')
        teac.append(tx)
        x = input()
        if x == 0:
            break



def priority():
    for i in range(len(co)):
        for j in range(len(co[i].sem)):
            if co[i].sem[j].yr == 3 or (co[i].sem[j].yr == 2 and co[i].cour['semno'] == 4):
                prio[3].append((i, j)) if co[i].sem[j].sem % 2 == 0 else prio1[3].append((i, j))
            elif co[i].sem[j].yr == 2 and co[i].cour['semno'] != 4:
                prio[2].append((i, j)) if co[i].sem[j].sem % 2 == 0 else prio1[2].append((i, j))
            elif co[i].sem[j].yr == 1 and co[i].lvl == 'PG':
                prio[1].append((i, j)) if co[i].sem[j].sem % 2 == 0 else prio1[1].append((i, j))
            else:
                prio[0].append((i, j)) if co[i].sem[j].sem % 2 == 0 else prio1[0].append((i, j))


priority()


def alloc():
    """ Take each priority class one by one and
        allot a slot for each batch for each day in a round robin fashion.
    """

    for pri in ken:
        if cur_sem:
            """ Take prio1 (odd sem)"""
            for k in days:
                for i, j in prio1[pri]:
                    kx = rn.randint(3, 4)
                    ch = rn.sample(co[i].sem[j].subs, kx)
                    kx = D1.selectday()
                    lsb = 0
                    for cod in ch:
                        if D1.check3(cod) is True:
                            continue
                        elif D1.check3(cod) in co[i].sem[j].tt.keys():
                            for cd in co[i].sem[j].tt.keys():
                                co[i].sem[j].tt[k][cd] = None if co[i].sem[j].tt[k][cd] == cod else co[i].sem[j].tt[k][cd]
                        if kx[k][0] == 'labs':
                            co[i].sem[j].tt[k][1] = 'Lab' + cod.code if cod.labs else cod.code
                            lsb += 3
                        elif kx[k][1] == 'labs':
                            co[i].sem[j].tt[k][0] = cod.code
                            co[i].sem[j].tt[k][1] = 'Lab' + cod.code if cod.labs else cod.code
                            lsb += 3
                        co[i].sem[j].tt[k][lsb] = cod
                        lsb += 1
                        if kx[k][2] == 'labs':
                            co[i].sem[j].tt[k][4] = 'Lab' + cod.code if cod.labs else None
                        t = D1.check_tea(teac, cod, co[i].sem[j].tt)
                        co[i].sem[j].t_no.append(t)




        elif not cur_sem:
            """ Take prio(even sem)"""
            for k in days:
                for i, j in prio[pri]:
                    kx = rn.randint(3, 4)
                    ch = rn.sample(co[i].sem[j].subs, kx)
                    kx = D1.selectday()
                    lsb = 0
                    for cod in ch:
                        if D1.check3(cod) is True:
                            continue
                        elif D1.check3(cod) in co[i].sem[j].tt.keys():
                            for cd in co[i].sem[j].tt.keys():
                                co[i].sem[j].tt[k][cd] = None if co[i].sem[j].tt[k][cd] == cod else co[i].sem[j].tt[k][cd]
                        if kx[k][0] == 'labs':
                            co[i].sem[j].tt[k][1] = 'Lab' + cod.code if cod.labs else cod.code
                            lsb += 3
                        elif kx[k][1] == 'labs':
                            co[i].sem[j].tt[k][0] = cod.code
                            co[i].sem[j].tt[k][1] = 'Lab' + cod.code if cod.labs else cod.code
                            lsb += 3
                        co[i].sem[j].tt[k][lsb] = cod
                        lsb += 1
                        if kx[k][2] == 'labs':
                            co[i].sem[j].tt[k][4] = 'Lab' + cod.code if cod.labs else None
                        t = D1.check_tea(teac, cod, co[i].sem[j].tt)
                        co[i].sem[j].t_no.append(t)
    print(co[0].sem[1].tt)

# if D1.check2():
#    pass
