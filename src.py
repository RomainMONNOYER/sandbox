def add(x, y):
    return x+y
def test_add():
    assert 5 == add(3, 2)
    assert 4 == add(3, 1)
def main():
    print("hello from main")

def diff(x, y):
    return x-y
def test_diff():
    assert 2 == diff(7,5)
    assert 2 != diff(5,7)

if __name__ == "__main__":
    print("hello there!")
    print("hello from Romain")
    print("1 + 1 = {}".format(add(1,1)))
    print("1 - 1 = {}".format(diff(1,1)))
