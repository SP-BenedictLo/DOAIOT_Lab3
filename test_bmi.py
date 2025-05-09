import DOAIOT_Lab2.bmi as bmi

def test_bmi_normal_weight():
    test_num_1 = 0
    result = bmi.calculate_bmi(57, 1.73)
    assert(test_num_1 == result)

def test_bmi_over_weight():
    test_num_2 = 1
    result = bmi.calculate_bmi(90, 1.73)
    assert(test_num_2 == result)

def test_bmi_under_weight():
    test_num_3 = -1
    result = bmi.calculate_bmi(15, 1.73)
    assert(test_num_3 == result)
