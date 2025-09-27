def add(x,y):
    return x+y

def rest(x,y):
    if x>y:
        result = x-y
    else:
        result = y-x
    return result

def test_sum():
    assert add(3,5) == 8

def test_rest():
    assert rest(5, 9) == 4
