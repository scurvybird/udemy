
def compare_strings(sorting_item: str, final_item: str) -> bool:
    letter_index = 0
    while sorting_item[letter_index] <= len(sorting_item):
        if sorting_item[letter_index] > final_item[letter_index]:
            return False
        elif sorting_item[letter_index] < final_item[letter_index]:
            return True
        else:
            letter_index += 1


def test_equal():
    si = "hello"
    fi = "hello"
    actual_result = compare_strings(si, fi)
    expected_result = True
    if actual_result != expected_result:
        raise ValueError(f"expected value: {expected_result} not equal to actual value: {actual_result}")

def test_lt():
    si = "hello"
    fi = "pello"
    actual_result = compare_strings(si, fi)
    expected_result = True
    if actual_result != expected_result:
        raise ValueError(f"expected value: {expected_result} not equal to actual value: {actual_result}")
    si = "hello"
    fi = "helly"
    actual_result = compare_strings(si, fi)
    expected_result = True
    if actual_result != expected_result:
        raise ValueError(f"expected value: {expected_result} not equal to actual value: {actual_result}")


def test_gt():
    si = "pello"
    fi = "hello"
    actual_result = compare_strings(si, fi)
    expected_result = True
    if actual_result != expected_result:
        raise ValueError(f"expected value: {expected_result} not equal to actual value: {actual_result}")
    si = "helly"
    fi = "hello"
    actual_result = compare_strings(si, fi)
    expected_result = True
    if actual_result != expected_result:
        raise ValueError(f"expected value: {expected_result} not equal to actual value: {actual_result}")


def test_equal_but_shorter():
    si = "hel"
    fi = "hello"
    actual_result = compare_strings(si, fi)
    expected_result = True
    if actual_result != expected_result:
        raise ValueError(f"expected value: {expected_result} not equal to actual value: {actual_result}")


def test_equal_but_longer():
    si = "helloooo"
    fi = "hello"
    actual_result = compare_strings(si, fi)
    expected_result = True
    if actual_result != expected_result:
        raise ValueError(f"expected value: {expected_result} not equal to actual value: {actual_result}")


def test_empty_second_parameter():
    si = "hello"
    fi = ""
    actual_result = compare_strings(si, fi)
    expected_result = True
    if actual_result != expected_result:
        raise ValueError(f"expected value: {expected_result} not equal to actual value: {actual_result}")


test_equal()
test_lt()
test_gt()
test_equal_but_shorter()
test_equal_but_longer()
test_empty_second_parameter()
print("YAY TESTS PASS")