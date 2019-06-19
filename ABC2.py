import sqlite3 as sq
import pathlib as pl
import Inst
import Demo as D
import sys

pat = pl.WindowsPath
pa = pat.cwd()
pa1 = str(pa) + 'SCSIT.accdb'
sys.path.append(str(pa))


def cons():
    con = sq.connect(pa1)
    urs = con.cursor()

    urs.execute("Select * from Teacher")

    for row in urs:
        Inst.teac.append(D.Teacher(row[2:], Name=row[0], ID=row[1]))

    urs.execute('select * from Course')

    for row in urs:
        Inst.co.append(D.Course(name=row[0], semno=row[1], lvl=row[2]))

    urs.execute('select * from Sem')

    for row in urs:
        if row[9] == 'BCA':
            Inst.co[0].sem.append(D.Course.Sem(row[0]))
            for i in range(1, len(row)-1):
                Inst.co[0].sem[row[0]-1].subs[i-1] = D.Subject(code=row[1])
                if row[i] is None:
                    break

        elif row[9] == 'MCA':
            Inst.co[1].sem.append(D.Course.Sem(row[0]))
            for i in range(1, len(row) - 1):
                Inst.co[1].sem[row[0]-1].subs[i - 1] = D.Subject(code=row[1])
                if row[i] is None:
                    break

        elif row[9] == 'MBA':
            Inst.co[0].sem.append(D.Course.Sem(row[0]))
            for i in range(1, len(row) - 1):
                Inst.co[2].sem[row[0]-1].subs[i - 1] = D.Subject(code=row[1])
                if row[i] is None:
                    break

        elif row[9] == 'MSc':
            Inst.co[0].sem.append(D.Course.Sem(row[0]))
            for i in range(1, len(row) - 1):
                Inst.co[3].sem[row[0]-1].subs[i - 1] = D.Subject(code=row[1])
                if row[i] is None:
                    break

    urs.execute('Select * from Subjects')

    for row in urs:
        if row[5] == 'BCA':
            for x in range(Inst.co[0].sem[row[6] - 1].nos):
                Inst.co[0].sem[row[6] - 1].subs[x].title = row[1]
                Inst.co[0].sem[row[6] - 1].subs[x].lecs = row[2]
                Inst.co[0].sem[row[6] - 1].subs[x].labs = row[3]
                Inst.co[0].sem[row[6] - 1].subs[x].imp = row[4]

        elif row[5] == 'MCA':
            for x in range(Inst.co[1].sem[row[6] - 1].nos):
                Inst.co[1].sem[row[6] - 1].subs[x].title = row[1]
                Inst.co[1].sem[row[6] - 1].subs[x].lecs = row[2]
                Inst.co[1].sem[row[6] - 1].subs[x].labs = row[3]
                Inst.co[1].sem[row[6] - 1].subs[x].imp = row[4]

        elif row[5] == 'MBA':
            for x in range(Inst.co[1].sem[row[6] - 1].nos):
                Inst.co[1].sem[row[6] - 1].subs[x].title = row[1]
                Inst.co[1].sem[row[6] - 1].subs[x].lecs = row[2]
                Inst.co[1].sem[row[6] - 1].subs[x].labs = row[3]
                Inst.co[1].sem[row[6] - 1].subs[x].imp = row[4]

        elif row[5] == 'MSc':
            for x in range(Inst.co[1].sem[row[6] - 1].nos):
                Inst.co[1].sem[row[6] - 1].subs[x].title = row[1]
                Inst.co[1].sem[row[6] - 1].subs[x].lecs = row[2]
                Inst.co[1].sem[row[6] - 1].subs[x].labs = row[3]
                Inst.co[1].sem[row[6] - 1].subs[x].imp = row[4]

    con.close()


def upd():
    pass
