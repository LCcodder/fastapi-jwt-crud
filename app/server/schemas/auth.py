from pydantic import BaseModel, Field, EmailStr


class UserCredentials(BaseModel):
    email: EmailStr = Field(
        title="User’s email, must be unique", examples=["john@domain.com"], max_length=64
    )
    password: str = Field(title="User's password", max_length=64, min_length=6)
