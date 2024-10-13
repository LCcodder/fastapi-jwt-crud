from pydantic import BaseModel, EmailStr, Field


class UserIn(BaseModel):
    email: EmailStr = Field(
        title="User’s email, must be unique",
        examples=["john@domain.com"],
        max_length=64
    )

    username: str = Field(title="Username (not unique)", max_length=32)
    birthday: str = Field(title="User's birthday date")
    sex: str = Field(title="User's gender", examples=["male", "female"])
    profile_color: str = Field(title="User's profile color", max_length=13)
    bio: str = Field(title="User's bio/description", max_length=100)
    password: str = Field(title="User's password", max_length=64, min_length=6)
