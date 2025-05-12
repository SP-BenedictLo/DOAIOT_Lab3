import price_info as pinfo

def test_total_cost_shopping():
    result = 0
    test_result = 46.75
    result = pinfo.total_cost_shopping()
    assert test_result == result

def test_cost_of_fruits():
    result = 0
    test_result = 36
    result = pinfo.cost_of_fruits("apple", 30)
    assert test_result == result
