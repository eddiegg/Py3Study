class TestObj:
    def __str__(self):
        return __class__.__name__

    pass

if __name__ == '__main__':

    testobj = TestObj()
    print(testobj)