from src.counter import count_ocurrences

JAVASCRIPT_OCURRENCES = 122


def test_counter():
    count = count_ocurrences("src/jobs.csv", "javascript")

    assert count == JAVASCRIPT_OCURRENCES
