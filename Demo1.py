import Demo


class check(object):
    def __init__(self):
        pass

    def classnum(self, tec: Demo.Teacher, cou: Demo.Course):
        for i in tec.cursub:
            if tec.cursub.count(i) >= 3:
                """merge classes"""
                while tec.cursub.count(i) > 1:
                    tec.cursub.remove(i)
            # assert isinstance(Demo.Course, cou)
            assert isinstance(Demo.Course.Sem, cou._sem[0])

            # cou._sem[0].t_no

