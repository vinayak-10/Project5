import random
import Demo as D
import Demo1 as D1

per = (10, 11, 12, 1, 1.5, 2.5, 3.5, 4.5)         # Time Periods for classes
ext = 9             # Extra time period when needed
cur_sem = True       # True for odd sem and False for even sem
tt = {x: per for x in ['M', 'T', 'W', 'Th', 'F', 'S']}     # dict for representing timetable
co = [D.Course(name='BCA', semno=6), D.Course(name='MCA', semno=6), D.Course(name='MSc', semno=4),
      D.Course(name='MBA', semno=4)]


def alloc():
    pass
