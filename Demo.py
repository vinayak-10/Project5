import builtins as bi

per = (10, 11, 12, 1, 1.5, 2.5, 3.5, 4.5)  # Time Periods for classes
ext = 9  # Extra time period when needed


class Subject(object):

    def __init__(self, code=None, title=None, lecs=None, lab=False, imp=0):
        self.code = code
        self.title = title
        self.lecs = lecs
        self.labs = lab
        self.imp = imp

    def __eq__(self, other):
        return self.code == other.code


class Teacher(object):
    nos = 0

    def __init__(self, *sb, **de):
        self.det = {'Name': '', 'ID': '', 'in_time': '', 'out_time': ''}
        self.det = {k: v for k, v in de.items() if k in self.det.keys()}
        self.subs = [k for k in sb]
        self.slots = {'m': [None, None, None, None, None, None, None],
                      't': [None, None, None, None, None, None, None],
                      'w': [None, None, None, None, None, None, None],
                      'th': [None, None, None, None, None, None, None],
                      'f': [None, None, None, None, None, None, None],
                      'sa': [None, None, None, None, None, None, None]}
        Teacher.nos += 1
        self._length = 3
        self.cursub = []    # Changes every sem; Limit input by user for constraint

    def __eq__(self, o) -> bool:
        return self.det['ID'] == o.det['ID']

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            k += len(self)  # attempt to convert negative index

        if not 0 <= k < len(self) or not 0 <= k < len(self.subs) or k not in self.det.keys() or k not in self.slots.keys():
            raise IndexError("index out of range")

        t = type(k)
        if t == str:
            if k in self.det.keys():
                return self.det[k]

            elif k in self.slots.keys():
                return self.slots[k]

        elif t == int:
            x = len(self.subs)
            if 0 <= k < x:
                return self.subs[k]
            elif x <= k < len(self.cursub):
                return self.cursub[k-x]

    def __setitem__(self, k, val):
        if k < 0:
            k += len(self)  # attempt to convert negative index

        if not 0 <= k < len(self) or not 0 <= k < len(self.subs):
            raise IndexError("index out of range")

        if k not in self.det.keys() or self.slots.keys():
            raise KeyError("Key not in available keys")

        t = type(k)
        if t == str:
            if k in self.det.keys():
                self.det[k] = val

            if k in self.slots.keys():
                self.slots[k] = val

        elif t == int:
            self.subs[k] = val

    def __contains__(self, item):
        return item in self.subs or self.slots or self.det


class Course(object):
    class Sem(object):

        def __init__(self, sem):
            self._subs = []
            self.sem = sem
            self.yr = sem//2 if sem % 2 != 0 else (sem//2)-1
            self.t_no = []
            self.tt = {x: per for x in ['M', 'T', 'W', 'Th', 'F', 'S']}  # dict for representing timetable

        def _adsub(self, sub: Subject, sno=5):
            self._subs[0] = sub
            for x in range(1, sno):
                self._subs.append(Subject(lecs=4))

        def __setitem__(self, sno, sub):
            if sno == 0:
                self._subs.append(sub)
            elif sno == 1:
                self.t_no.append(sub)

        def __delitem__(self, k):
            code = input("Code of item to be deleted")
            if k == 0:
                for i in range(len(self._subs)):
                    if self._subs[i].code == code:
                        del self._subs[i]
                        return
            elif k == 1:
                for i in range(len(self.t_no)):
                    if self.t_no[i] == code:
                        del self.t_no[i]
                        return

        def __getitem__(self, sno):
            try:
                if 0 <= sno <= 5:
                    return self._subs[sno]
                elif 6 <= sno <= 11:
                    return self.t_no[sno - 6]
            except IndexError:
                print(IndexError, end=' ')
                pass

    def __init__(self, name, semno, lvl):
        self.cour = {'Name': name, 'semno': semno}
        self._sem = []
        self.lvl = lvl
        for x in range(semno):
            self._adsem(semno=x + 1)

    def _adsem(self, semno):
        self._sem.append(self.Sem(sem=semno))

    def _delsem(self, semno):
        for x in range(len(self._sem)):
            if self._sem[x].sem == semno:
                self._sem.pop(x)
