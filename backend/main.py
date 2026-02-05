from fastapi import FastAPI, Depends, HTTPException
from database import Base, engine, SessionLocal
from models import User
from schemas import UserCreate, UserLogin
from auth import create_token
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

pwd = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto")

app = FastAPI()

# CORS allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # you can set ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    # no encoding needed
    hashed_pw = pwd.hash(user.password)

    db_user = User(username=user.username, password=hashed_pw)
    db.add(db_user)
    db.commit()
    return {"message": "User Registered"}

@app.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()

    # password verify — no encode()
    if not user or not pwd.verify(data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid Credentials")

    token = create_token(user.username)
    return {"token": token}