import random as rn
import Demo as D
import Demo1 as D1


cur_sem = True  # True for odd sem and False for even sem; Set by asking user
co = [D.Course(name='BCA', semno=6, lvl='UG'), D.Course(name='MCA', semno=6, lvl='PG'),
      D.Course(name='MSc', semno=4, lvl='PG'),
      D.Course(name='MBA', semno=4, lvl='PG')]
prio = {0: [], 1: [], 2: [], 3: []}
teac = []


def inp():
    co[0]._sem[0] = D.Subject(code="CS-2111", title="Mathematics-II", lecs=4, lab=False, imp=1)
    teac.append(D.Teacher("CS-2111", "CS-1102", Name="", ID="", in_time=11, out_time=6))


def priority():
    for i in range(len(co)):
        for j in range(len(co[i]._sem)):
            if co[i]._sem[j].yr == 3 or (co[i]._sem[j].yr == 2 and co[i].cour['semno'] == 4):
                prio[3].append(co[i]._sem[j])
            elif co[i]._sem[j].yr == 2 and co[i].cour['semno'] != 4:
                prio[2].append(co[i]._sem[j])
            elif co[i]._sem[j].yr == 1 and co[i].lvl == 'PG':
                prio[1].append(co[i]._sem[j])
            else:
                prio[0].append(co[i]._sem[j])


def alloc():
    pri = rn.randint(0, 4)
    # Run RR on prio[pri]
