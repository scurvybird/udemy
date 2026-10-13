
def compare_strings(sorting_item: str, final_item: str) -> int:
    letter_index = 0
    while letter_index < len(sorting_item) and letter_index < len(final_item):
        if sorting_item[letter_index] > final_item[letter_index]:
            return 1
        elif sorting_item[letter_index] < final_item[letter_index]:
            return -1
        else:
            letter_index += 1
    if len(sorting_item) < len(final_item):
        return -1
    if len(sorting_item) > len(final_item):
        return 1
    return 0

# def compare_strings(sorting_item: str, final_item: str) -> bool:
#     if sorting_item > final_item:
#         return 1
#     elif sorting_item < final_item:
#         return -1
#     else:
#         return 0

def test_equal():
    si = "hello"
    fi = "hello"
    actual_result = compare_strings(si, fi)
    expected_result = 0
    if actual_result != expected_result:
        raise ValueError(f"expected value: {expected_result} not equal to actual value: {actual_result}")

def test_lt():
    si = "hello"
    fi = "pello"
    actual_result = compare_strings(si, fi)
    expected_result = -1
    if actual_result != expected_result:
        raise ValueError(f"expected value: {expected_result} not equal to actual value: {actual_result}")
    si = "hello"
    fi = "helly"
    actual_result = compare_strings(si, fi)
    expected_result = -1
    if actual_result != expected_result:
        raise ValueError(f"expected value: {expected_result} not equal to actual value: {actual_result}")


def test_gt():
    si = "pello"
    fi = "hello"
    actual_result = compare_strings(si, fi)
    expected_result = 1  ##changed True to False
    if actual_result != expected_result:
        raise ValueError(f"expected value: {expected_result} not equal to actual value: {actual_result}")
    si = "helly"
    fi = "hello"
    actual_result = compare_strings(si, fi)
    expected_result = 1  ##changed True to False
    if actual_result != expected_result:
        raise ValueError(f"expected value: {expected_result} not equal to actual value: {actual_result}")


def test_equal_but_shorter():
    si = "hel"
    fi = "hello"
    actual_result = compare_strings(si, fi)
    expected_result = -1
    if actual_result != expected_result:
        raise ValueError(f"expected value: {expected_result} not equal to actual value: {actual_result}")


def test_equal_but_longer():
    si = "helloooo"
    fi = "hello"
    actual_result = compare_strings(si, fi)
    expected_result = 1  ##changed True to False
    if actual_result != expected_result:
        raise ValueError(f"expected value: {expected_result} not equal to actual value: {actual_result}")


def test_empty_second_parameter():
    si = "hello"
    fi = ""
    actual_result = compare_strings(si, fi)
    expected_result = 1  ##changed True to False
    if actual_result != expected_result:
        raise ValueError(f"expected value: {expected_result} not equal to actual value: {actual_result}")


test_equal()
test_lt()
test_gt()
test_equal_but_shorter()
test_equal_but_longer()
test_empty_second_parameter()
print("YAY TESTS PASS")