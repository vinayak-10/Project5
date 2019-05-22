import Demo as D


def classnum(tec: D.Teacher, cou: D.Course):
    # assert isinstance(Demo.Course, cou)
    assert isinstance(D.Course.Sem, cou._sem[0])
    for i in tec.cursub:
        if tec.cursub.count(i) >= 3:
            """merge classes"""
            while tec.cursub.count(i) > 1:
                tec.cursub.remove(i)
                var = i == cou._sem[0][1]


        # cou._sem[0].t_no

