from basic_python.calculator import Calculator
def test_add():
    c=Calculator(1,2)
    result=c.add()
    assert result==4,"加法运算失败"
def test_plus():
    c=Calculator(1,2)
    result=c.plus()
    assert result==4,"加法运算失败"
if __name__ == '__main__':
    print(test_add())
    print(test_plus())