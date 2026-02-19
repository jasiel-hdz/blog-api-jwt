from fastapi import Depends, HTTPException, status
from database import sessionLocal
from core.user.bearer import JWTBearer
from core.user.models import User
from config import get_settings
import jwt

settings = get_settings()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
def get_current_user(token: str = Depends(JWTBearer())) -> User:
    try:
        payload = jwt.decode(token, f'{settings.SECRET_KEY}', algorithms=['HS256'])
        user_id = payload.get('sub')
        db = sessionLocal()
        return db.query(User).filter(User.id == user_id).first()
    except(jwt.PyJWTError, AttributeError):
        return HTTPException(status_code="Invalid token")
