import polynomial
import PolyTest
import mutmut

def test_init():
    poly = polynomial([3, 0, 2])
    assert poly.coefficients == [3, 0, 2]

    poly1 = polynomial([])
    assert poly1.coefficients == []

    poly2 = polynomial(None)
    assert poly2.coefficients == []


def test_str():
    poly = polynomial([3, 0, 2])
    assert str(poly) == "3x^2 + 2"

    poly2 = polynomial([1, -1])
    assert str(poly2) == "1x + -1"

    poly3 = polynomial([0, 0, 0])
    assert str(poly3) == "0" or str(poly3) == ""

    poly = polynomial([1, 0, -3])  
    result = str(poly)
    assert result == "1x^2 + -3"

    poly4 = polynomial([1])
    assert str(poly4) == "1"

    poly5 = polynomial([])
    assert str(poly5) == "0"

def test_add():
   
    poly1 = polynomial([1, 2, 3])  
    poly2 = polynomial([4, 5, 6])  
    result = poly1 + poly2
    assert result.coefficients == [5, 7, 9]  

    poly1 = polynomial([3, 0, 2])
    poly2 = polynomial([1, -1])
    poly_sum = poly1 + poly2
    assert poly_sum.coefficients == [3, 1, 1]

    poly1 = polynomial([3, 0, 2])
    poly2 = polynomial([])
    poly_sum = poly1 + poly2
    assert poly_sum.coefficients == [3, 0, 2]

    
    poly1 = polynomial([])  
    poly2 = polynomial([])  
    result = poly1 + poly2
    assert result.coefficients == []  

    
    poly1 = polynomial([1, 2, 3])  
    poly2 = polynomial(None)  
    result = poly1 + poly2
    

    assert result.coefficients == [1, 2, 3]  
def test_sub():
    poly1 = polynomial([3, 0, 2])
    poly2 = polynomial([1, -1])

    poly_diff = poly1 - poly2
    assert poly_diff.coefficients == [3,-1, 3]

def test_mul():

    poly1 = polynomial([])
    poly2 = polynomial([])
    result = poly1 * poly2
    assert result.coefficients == []

    
    poly1 = polynomial([0])
    poly2 = polynomial([3, 3, 3])
    result = poly1 * poly2
    assert result.coefficients == [0, 0, 0]

   
    poly1 = polynomial([1])
    poly2 = polynomial([4, 5, 6])
    result = poly1 * poly2
    assert result.coefficients == [4, 5, 6]

  
    poly1 = polynomial([5, 4, 3])
    poly2 = polynomial([4, 9])
    result = poly1 * poly2
    assert result.coefficients == [0, 17, 23, 4]

def test_evaluate():

    
    poly = polynomial([])
    result = poly.evaluate(10)  
    assert result == 0 
