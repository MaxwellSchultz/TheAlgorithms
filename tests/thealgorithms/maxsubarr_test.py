import src.thealgorithms.maxsubarr as maxsubarr

# ======================================================= #
# Testing find_max_cross_subarr(arr,low,mid,high) method
# ======================================================= #

def test_find_max_cross_subarr_two():
    low = 0
    mid = 1
    high = 3
    arr = [-1,1,1,-1]
    assert maxsubarr.find_max_cross_subarr(arr,low,mid,high) == (1,2,2)
    
def test_find_max_cross_subarr_twoleft():
    low = 0
    mid = 2
    high = 4
    arr = [-1,1,1,1,-1]
    assert maxsubarr.find_max_cross_subarr(arr,low,mid,high) == (1,3,3)
    
def test_find_max_cross_subarr_tworight():
    low = 0
    mid = 3
    high = 6
    arr = [-1,-1,-1,1,1,1,-1]
    assert maxsubarr.find_max_cross_subarr(arr,low,mid,high) == (3,5,3)
    
def test_find_max_cross_subarr_crossnegleft():
    low = 0
    mid = 2
    high = 4
    arr = [-1,2,-1,1,-1]
    assert maxsubarr.find_max_cross_subarr(arr,low,mid,high) == (1,3,2)
    
def test_find_max_cross_subarr_crossnegright():
    low = 0
    mid = 2
    high = 4
    arr = [-1,-1,1,-1,2]
    assert maxsubarr.find_max_cross_subarr(arr,low,mid,high) == (2,4,2)

def test_find_max_cross_subarr_largeleft():
    low = 0
    mid = 3
    high = 6
    arr = [-1,5,-2,-1,-1,1,-1]
    assert maxsubarr.find_max_cross_subarr(arr,low,mid,high) == (1,5,2)
    
def test_find_max_cross_subarr_largeright():
    low = 0
    mid = 3
    high = 7
    arr = [-1,-1,-1,1,-1,-1,-2,5]
    assert maxsubarr.find_max_cross_subarr(arr,low,mid,high) == (3,7,2)
