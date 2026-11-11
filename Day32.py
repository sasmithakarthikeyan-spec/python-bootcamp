'''#generate JWT Token
import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "mysecretkey123"

payload = {
    "name": "Sash",
    "course": "Python",
    "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
}

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

print("Generated JWT Token:")
print(token)

#decode JWT Token
decoded_data = jwt.decode(
    token,
    SECRET_KEY,
    algorithms=["HS256"]
)

print("\nDecoded JWT Data:")
print(decoded_data)

#Invalid JWT Token
fake_token = token + "wrong"

try:
    decoded = jwt.decode(
        fake_token,
        SECRET_KEY,
        algorithms=["HS256"]
    )

    print(decoded)

except jwt.InvalidTokenError:
    print("\nInvalid token! Access denied.")

#write password
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

# Original password
password = "python123"

# Hash the password
hashed_password = password_hash.hash(password)

print("Hashed Password:")
print(hashed_password)

# Verify the password
is_valid = password_hash.verify(
    "python123",
    hashed_password
)

print("Password correct:", is_valid)

#wrong password checking
wrong_password = "hello123"

is_valid = password_hash.verify(
    wrong_password,
    hashed_password
)

print("Wrong password correct:", is_valid)'''

#miniproject
from fastapi import FastAPI
from pydantic import BaseModel
from pwdlib import PasswordHash
import jwt
from datetime import datetime, timedelta, timezone

app = FastAPI()

# Security settings
SECRET_KEY = "learning-secret-key-change-later"
ALGORITHM = "HS256"

password_hash = PasswordHash.recommended()

# Temporary user storage
users = {}

# Registration model
class User(BaseModel):
    username: str
    password: str

# Login model
class Login(BaseModel):
    username: str
    password: str

@app.get("/")
def home():
    return {"message": "Authentication API is running!"}

@app.post("/register")
def register(user: User):

    if user.username in users:
        return {"message": "Username already exists!"}

    hashed_password = password_hash.hash(user.password)

    users[user.username] = {
        "username": user.username,
        "password": hashed_password
    }

    return {"message": "User registered successfully!"}

@app.post("/login")
def login(user: Login):

    if user.username not in users:
        return {"message": "User not found!"}

    stored_user = users[user.username]

    if not password_hash.verify(
        user.password,
        stored_user["password"]
    ):
        return {"message": "Incorrect password!"}

    payload = {
        "sub": user.username,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return {
        "message": "Login successful!",
        "access_token": token,
        "token_type": "bearer"
    }