from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from auth.jwt import create_access_token

router = APIRouter()

# Hardcoded internal user (acceptable for internal tools)
INTERNAL_USER = {
    "email": "admin@alignlabs.com",
    "password": "admin123"
}

class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest):
    if (
        data.email != INTERNAL_USER["email"]
        or data.password != INTERNAL_USER["password"]
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = create_access_token({"sub": data.email})
    return {"access_token": token}
