import write_your_name as name_point

def test_hi_my_name_is():
    assert len(name_point.hi_my_name_is())  > 1 

def test_hi_my_name_is_alpha_space():
    assert name_point.hi_my_name_is().replace(' ', '').isalpha()