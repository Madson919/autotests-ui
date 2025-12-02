from pydantic import BaseModel, Field


class Market(BaseModel):
    id: int
    name: str


class Product(BaseModel):
    name: str
    price: float = Field(..., ge=0, description="Цена должна быть больше 0")
    tags: list[str] = []
    market: Market


product_data = {
    "name": "Phone",
    "price": 499.99,
    "tags": ["electronic", "smartphone"],
    "market": {
        "id": 123123,
        "name": "Amazon"
    }
}

product = Product(**product_data)
print(product.market.id)

new_product = Product(
    name="Laptop",
    price=123,
    tags=["electronics"],
    market=Market(id=213123123, name="Ozon")
)

print(new_product)