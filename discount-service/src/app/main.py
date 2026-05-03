from fastapi import FastAPI, HTTPException
import os
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title="Discount Service")

class DiscountResponse(BaseModel):
    discount_percent: float
    discount_amount: float
    reason: str
    
class DiscountRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)
    promo_code: Optional[str] = None

PROMO_CODE_QUANTITY: dict[int, int]={
    10: 5,
    20: 7,
    30: 10,
}

NAME_PROMO_CODE: dict[str, int]={
    "STUDENT10": 10,
    "PROMO5": 5,
}

@app.post("/discounts/calculate", response_model=DiscountResponse)
def calculate(request: DiscountRequest) -> DiscountResponse:
    total_before_discount = request.unit_price * request.quantity
    discount_percent = 0.0
    reason = "No applicable discount"

    quantity_percent = PROMO_CODE_QUANTITY.get(request.quantity, False)
    promo_percent = NAME_PROMO_CODE.get(request.promo_code, False)
    if promo_percent:
        discount_percent = promo_percent
        reason = f"{request.promo_code} was activated"
    
    elif quantity_percent:
        discount_percent = quantity_percent
        reason = f"{request.quantity} was(were) ordered"

    if promo_percent and quantity_percent:
        discount_percent = max(promo_percent, quantity_percent)
    
    discount_amount = total_before_discount * (discount_percent / 100)

    return DiscountResponse(
        discount_percent=discount_percent,
        discount_amount=discount_amount,
        reason=reason,
    )

        