'''
学习python3的一些简单代码
'''
import pickle
# isinstance(item, list)
# dir(__builtins__)

Istr = 'hi, I am eddie'
print(Istr.strip('e'))

with open('myData.pickle','wb') as mysavedata:
    pickle.dump([45,"sadf",'false'], mysavedata)
with open('myData.pickle','rb') as mystoredata:
    temlst = pickle.load(mystoredata)
print(temlst)
print(mystoredata)