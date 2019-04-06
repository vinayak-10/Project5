import builtins

per = (10, 11, 12, 1, 1.5, 2.5, 3.5, 4.5)
ext = 9,


class Subject(object):

    def __init__(self, **s1):
        self.code = s1['code']
        self.title = s1['title']
        self.lecs = s1['lecs']
        self.labs = s1['labs']
        self.imp = s1['imp']
        self.course = s1['course']


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


    """for k in de.keys():
       if k in self.det.keys():
           self.det[k] = de[k]
       if k in self.slots.keys():
            self.slots[k] = de[k]"""
    # self.slots = {k:v for k,v in de.items() if k in self.det.keys()}
    def __getitem__(self, index):
        


     """
    def u_slot(self, **sl):
        self.slots = {k:v for k,v in s1.items() if k in self.slots.keys()}

    def u_det(self, **s2):
        self.det = {k:v for k,v in s2.items() if k in self.det.keys()}

    def u_sub(self, *sb):
        self.subs.extend(sb)

    def clear(self, ic):
        if ic == 0:
            self.det = {k:None for k in self.det.keys()}
        
        elif ic == 1:
            self.slots = {k:None for k in self.slots.keys()}

        elif ic == 2:
            self.subs = []

        elif ic == 3:
            self.det = {k:None for k in self.det.keys()}
            self.slots = {k:None for k in self.slots.keys()}
            self.subs = []
        #__nos = 0
 
        """





class Course(object):

    def __init__(self, name, semno):
        self.cour = {'Name': name, 'semno': semno}
        self.__subs = []

    def _sub(self, subs):
        self.__subs.append(subs)

    def _delsubs(self, code):
        for i in range(len(self.__subs)):
            if self.__subs[i].code == code:
                del self.__subs[i]
                return True
        return False

    class Sem(object):

        def __init__(self, sem, sub=[]):
            self.sub_list = sub
            self.sem = sem
            self.st_no = 0
