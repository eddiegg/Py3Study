def gental_man(*args, **kwargs):
    def outer_deco(func):
        if(args):
            print('I know {}'.format((args)))
        def wrapper(*args,**kwargs):
            print('This is a deco Demo \n')
            func(*args,**kwargs)
        return wrapper
    return outer_deco


@gental_man(('java', 'python'))
def hi(name="eddie"):
    print("Hi,{}".format(name))


if __name__ == '__main__':
    hi("eddy")