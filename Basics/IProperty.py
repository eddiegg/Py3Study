class TestProp:
    ilist = []

    @property
    def ilist(self):
        return self.ilist

    @ilist.setter
    def ilist(self, ilist):
        self.ilist = ilist

if __name__ == '__main__':
    t = TestProp
    t.ilist=[1,2,3]
    print(t.ilist)
