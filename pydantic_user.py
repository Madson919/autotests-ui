from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True

user_data = {
    "id": 1,
    "username": "Mikhail",
    "email": "mikhail@gmail.com"
}

user = User(**user_data)
print(user.email)

invalid_user_data = {
    "id": "one",
    "username": "Mikhail",
    "email": "mikhail@gmail.com"
}

try:
    invalid_user = User(**invalid_user_data)
except Exception as e:
    print(e)