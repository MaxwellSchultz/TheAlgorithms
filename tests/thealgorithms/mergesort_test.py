import src.thealgorithms.mergesort as mergesort

# ============================== #
# Testing merge() method
# ============================== #
def test_merge_two():
    p = 0
    r = 1
    q = (p+r)//2
    arr = [2,1]
    assert mergesort.merge(arr,p,q,r) == [1,2]

def test_merge_two_middle():
    p = 5
    r = 6
    q = (p+r)//2
    arr = [0,0,0,0,0,2,1,0,0]
    assert mergesort.merge(arr,p,q,r) == [0,0,0,0,0,1,2,0,0]
    
def test_merge_three():
    p = 0
    r = 2
    q = (p+r)//2
    arr = [2,3,1]
    assert mergesort.merge(arr,p,q,r) == [1,2,3]
    
def test_merge_uneven():
    p = 0
    r = 4
    q = (p+r)//2
    arr = [1,4,16,2,8,0,0,0,0]
    assert mergesort.merge(arr,p,q,r) == [1,2,4,8,16,0,0,0,0]
    
def test_merge_even():
    p = 4
    r = 7
    q = (p+r)//2
    arr = [0,0,0,0,1,4,2,3]
    assert mergesort.merge(arr,p,q,r) == [0,0,0,0,1,2,3,4]

def test_merge_nine():
    p = 0
    r = 8
    q = (p+r)//2
    arr = [5,8,9,12,13,6,7,10,11]
    assert mergesort.merge(arr,p,q,r) == [5,6,7,8,9,10,11,12,13]
    
# ============================== #
# Testing mergesort() method
# ============================== #
    
def test_mergesort_empty():
    p = 0
    r = 0
    arr = []
    assert mergesort.mergesort(arr,p,r) == []
    
def test_mergesort_ascending():
    p = 0
    r = 7
    arr = [1,2,3,4,5,6,7,8]
    assert mergesort.mergesort(arr,p,r) == [1,2,3,4,5,6,7,8]
    
def test_mergesort_decending():
    p = 0
    r = 7
    arr = [8,7,6,5,4,3,2,1]
    assert mergesort.mergesort(arr,p,r) == [1,2,3,4,5,6,7,8]
    
def test_mergesort_same():
    p = 0
    r = 7
    arr = [1,1,1,1,1,1,1,1]
    assert mergesort.mergesort(arr,p,r) == [1,1,1,1,1,1,1,1]
    
def test_mergesort_same():
    p = 0
    r = 7
    arr = [4,3,4,3,2,1,2,1]
    assert mergesort.mergesort(arr,p,r) == [1,1,2,2,3,3,4,4]
    
def test_mergesort_uneven():
    p = 0
    r = 8
    arr = [9,8,7,6,5,4,3,2,1]
    assert mergesort.mergesort(arr,p,r) == [1,2,3,4,5,6,7,8,9]
    
def test_mergesort_alex():
    p = 0
    r = 7
    arr = [513,21,708,92642,3,459,1048,398]
    assert mergesort.mergesort(arr,p,r) == [3, 21, 398, 459, 513, 708, 1048, 92642]