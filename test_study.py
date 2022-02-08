import yaml


class Teststudy():
    def test_study(self):
        aa = 'asdasdasd'
        bb ='ad'
        print(aa.replace(bb, '0'))

        rr = "123%d" % 123
        print(rr)

        # a='195%d' % 00000000
        a= ["195%08d" % x for x in range(101)]
        print(a)



        aaa=yaml.safe_load(open('./datas/date.yml','r'))
        print(aaa)