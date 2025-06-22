from sqlalchemy.orm import Session
from app.models.user import User

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()

def create_user_if_not_exists(db: Session, user_id: int):
    user = get_user(db, user_id)

    if not user:
        user = User(user_id=user_id, preferences={})
        db.add(user)
        db.commit()
        db.refresh(user)

    return user