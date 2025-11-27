from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from backend.database import get_db
from backend import models, schemas
from backend.utils import hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])

# JWT settings
SECRET_KEY = "CHANGE_THIS_SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# ----------------- TOKEN CREATION -----------------

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# ----------------- REGISTER -----------------

@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    existing = db.query(models.User).filter(models.User.email == user.email).first()
    if existing:
        raise HTTPException(400, "Email already registered")

    hashed_pw = hash_password(user.password)

    db_user = models.User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_pw   # ✔ CORRECT FIELD
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# ----------------- LOGIN -----------------

@router.post("/login", response_model=schemas.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(
        models.User.email == form_data.username
    ).first()

    if not user or not verify_password(form_data.password, user.hashed_password):  # ✔ FIXED
        raise HTTPException(400, "Invalid email or password")

    access_token = create_access_token({"sub": str(user.id)})

    return {"access_token": access_token, "token_type": "bearer"}


# ----------------- GET CURRENT USER -----------------

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> models.User:

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(401, "Invalid token")

    except JWTError:
        raise HTTPException(401, "Invalid token")

    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(404, "User not found")

    return user
