def score_response(actual, expected):

    actual = actual.strip().upper()
    expected = expected.strip().upper()

    if actual == expected:
        return 1.0

    return 0.0
