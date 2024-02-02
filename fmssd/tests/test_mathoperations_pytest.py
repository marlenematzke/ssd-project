import numpy as np
import mathoperations as mo
import pytest

@pytest.mark.parametrize("myinput, myref",
                         [(([0], [1], np.array([0,1])), 1)]
                        )
def test_euclidean_distance(myinput, myref):
    assert mo.euclidean_distance(myinput[0],myinput[1],myinput[2]) == myref

@pytest.mark.parametrize("myinput, myref",
                         [( (np.array([[1,2,3],[4,5,6],[0,0,0]]), 0), (np.array([[1,2,3],[4,5,6]])) )]
                         )
def test_check_if_significant_np(myinput, myref):
    assert (mo.check_if_significant_np(myinput[0],myinput[1])[0] == myref).all()

def test_check_if_significant_np_valueerror():
    with pytest.raises(ValueError):
        mo.check_if_significant_np(np.array([[1,2,3], [4,5,6]]), -1)

@pytest.mark.parametrize("myinput, myref",
                         [( (np.ones(10), 1), np.array([10, 0, 0, 0, 0, 0, 0, 0, 0, 0]) ),
                          ( (np.zeros(10), 1), np.zeros(10))]
                        )
def test_discrete_fourier_transform(myinput, myref):
    assert (mo.discrete_fourier_transform(myinput[0],myinput[1])[0] == myref).all()