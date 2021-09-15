from project_euler.problem27.problem27 import quadratic, is_prime, find_best_product_of_a_and_b

def test_is_prime():
    assert is_prime(1) == True
    assert is_prime(2) == True
    assert is_prime(16) == False
    assert is_prime(53500) == False

# this one doesn't really need to be tested, it just does what it says on the tin
def test_quadratic():
    assert quadratic(1,3,7) == 59
    assert quadratic(1,-100,7) == -44

def test_complex():
    # in the case of a negative number, it should return False, and not deal with complex values
    assert is_prime(quadratic(1,-100,7)) == False