import json
from pathlib import Path

from evaluator import evaluate_return
from scorer import score_response

ROOT_DIR = Path(__file__).resolve().parent

with open(ROOT_DIR / "test_cases.json", "r") as file:
    test_cases = json.load(file)

results = []

for index, case in enumerate(test_cases, start=1):

    actual = evaluate_return(case["input"])
    expected = case["expected"]

    score = score_response(actual, expected)

    result = {
        "case_id": f"TC{index:02d}",
        "input": case["input"],
        "expected": expected,
        "actual": actual,
        "score": score,
        "status": "PASS" if score == 1.0 else "FAIL"
    }

    results.append(result)

    print(f"\n{result['case_id']}: {result['status']}")
    print(f"Expected: {expected}")
    print(f"Actual: {actual}")
    print(f"Score: {score}")

total_score = sum(item["score"] for item in results)
average_score = total_score / len(results)

report = {
    "total_cases": len(results),
    "passed": sum(r["status"] == "PASS" for r in results),
    "failed": sum(r["status"] == "FAIL" for r in results),
    "average_score": average_score,
    "results": results
}

with open(ROOT_DIR / "results.json", "w") as file:
    json.dump(report, file, indent=4)

print("\nAverage Score:", average_score)
print("Results saved to results.json")
