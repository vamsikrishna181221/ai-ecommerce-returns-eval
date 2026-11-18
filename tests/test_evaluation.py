import json
import pytest
from pathlib import Path
from evaluator import evaluate_return
from scorer import score_response

# Load test data from JSON file
ROOT_DIR = Path(__file__).resolve().parents[1]

with open(ROOT_DIR / "test_cases.json", "r") as file:
    test_cases = json.load(file)



@pytest.mark.parametrize("case", test_cases)
def test_return_eligibility(case):

    actual = evaluate_return(case["input"])
    expected = case["expected"]

    score = score_response(actual, expected)

    print(f"\nExpected: {expected}")
    print(f"Actual: {actual}")
    print(f"Score: {score}")

    assert score == 1.0, (
        f"Expected {expected}, but got {actual}"
    )

