import random
import datetime

b = datetime.date(*map(int,'2019-03-14'.split('-')))
print(b,type(b))



def product_code():
    code=random.randint(1000,9999)
    return code



def test():
    a='2020-06-01'
    result=datetime.strptime("2019-04-15", "%Y-%m-%d")
    return result

if __name__ == '__main__':
    print(test(),type(test()))







