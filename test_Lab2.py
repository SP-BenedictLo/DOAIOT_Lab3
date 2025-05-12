import DOAIOT_Lab2.Lab2 as Lab2

def test_find_min_max():
    result = []
    input_arr = [64.5, 34.4, 25.3, 12.2, 22.2, 11.0, 90.1]
    test_arr = [11.0, 90.1]

    result = Lab2.find_min_max(input_arr)

    assert [result == test_arr]


def test_calc_average():
    result = 0
    input_arr = [64.5, 34.4, 25.3, 12.2, 22.2, 11.0, 90.1]
    test_ans = 37.1

    result = Lab2.calc_average(input_arr)

    assert result == test_ans

def test_calc_median_temperature_odd():
    result = 0.0
    input_arr = [64.5, 34.4, 25.3, 12.2, 22.2, 11.0, 90.1]
    test_ans = 12.2

    result = Lab2.calc_median_temperature(input_arr)

    assert result == test_ans

def test_calc_median_temperature_even():
    result = 0.0
    input_arr = [64.5, 34.4, 25.3, 22.2, 11.0, 90.1]
    test_ans = 23.75

    result = Lab2.calc_median_temperature(input_arr)

    assert result == test_ans