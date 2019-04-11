import builtins

per = (10, 11, 12, 1, 1.5, 2.5, 3.5, 4.5)
ext = 9,


class Subject(object):

    def __init__(self, code, title, lecs, labs, imp, course):
        self.code = code
        self.title = title
        self.lecs = lecs
        self.labs = labs
        self.imp = imp
        self.course = course


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
        self.cursub = []


    def __eq__(self, o) -> bool:
        return self.det['ID'] == o.det['ID']

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            k += len(self)  # attempt to convert negative index

        if not 0 <= k < len(self) or not 0 <= k < len(self.subs):
            raise IndexError("index out of range")

        if k not in self.det.keys() or self.slots.keys():
            raise KeyError("Key not in available keys")

        t = type(k)
        if t == str:
            if k in self.det.keys():
                return self.det[k]

            elif k in self.slots.keys():
                return self.slots[k]

        elif t == int:
            return self.subs[k]

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

        def __init__(self, sem, sub=None):
            if sub is None:
                sub = []
            self._subs = sub
            self.sem = sem
            self.t_no = []

    def __init__(self, name, semno):
        self.cour = {'Name': name, 'semno': semno}
        self._sem = [self.Sem(1)]

    def _adsem(self, x: Sem, ts, semno):
        self._sem.append(x)
        self._sem[semno-1].t_no.append(ts)



