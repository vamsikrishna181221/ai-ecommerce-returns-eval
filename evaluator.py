import requests
from config import OPENROUTER_API_KEY

API_URL = "https://openrouter.ai/api/v1/chat/completions"

MODEL = "openrouter/free"


def evaluate_return(order_details):

    prompt = f"""
You are an ecommerce returns eligibility evaluator.

Evaluate the customer's return request using these rules:

RULE 1: DEFECTIVE PRODUCTS
If the product is defective, APPROVE the return,
regardless of delivery date or final sale status.

RULE 2: DIGITAL PRODUCTS
If the product is a gift card or digital download,
ESCALATE the request for manual review.

RULE 3: FINAL SALE
If the product is marked as final sale,
DENY the return unless the defective product rule applies.

RULE 4: RETURN WINDOW
For normal physical products:
- Calculate the number of days between delivery date and today.
- If within 30 days, APPROVE.
- If more than 30 days, DENY.

IMPORTANT:
- Evaluate the complete input before deciding.
- Follow the business rules consistently.
- Do not invent missing order information.
- Return exactly ONE label.
- Do not include explanations or additional text.

Allowed outputs:
APPROVE
DENY
ESCALATE

Customer order details:
{order_details}
"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload,
        timeout=60
    )

    if response.status_code != 200:
        print("HTTP Status:", response.status_code)
        print("API Error Details:", response.text)
        response.raise_for_status()

    result = response.json()

    return result["choices"][0]["message"]["content"].strip()

