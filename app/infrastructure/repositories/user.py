from sqlalchemy.orm import Session
from datetime import datetime
from app.domain.user import UserCreate#, User
from app.core.security import get_password_hash 
from app.infrastructure.models.user import User
from app.infrastructure.repositories.base import BaseRepo


class UserRepo(BaseRepo):
    _model = User
    
    @classmethod
    def get_user_by_email(cls, db: Session, email: str):
        return db.query(cls._model).filter(User.email == email, User.deleted_at == None).first()

    @classmethod
    def create_user(cls, db: Session, user: UserCreate):
        now = datetime.utcnow()
        db_user = cls._model(
            email=user.email, 
            hashed_password=get_password_hash(user.password),
            first_name=user.first_name,
            last_name= user.last_name,
            type_user= user.type_user,
            is_active=False,
            created_at=now,
            updated_at=now
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @classmethod
    def update_user(cls, db: Session, user: User):
        user.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(user)
        return user

    @classmethod
    def soft_delete_user(cls, db: Session, user: User):
        user.deleted_at = datetime.utcnow()  # Marcar fecha de eliminación
        UserRepo.update_user(db, user)  # Actualizar registro en la BD
        return user

    @classmethod
    def verify_user(cls, db: Session, user: User):
        user.is_active = True
        UserRepo.update_user(db, user)  
        return user

    @classmethod
    def get_user_by_id(cls, db: Session, user_id: int):
        return db.query(cls._model).filter(User.id == user_id).first()

    @classmethod
    def get_all_users(cls, db: Session):
        return db.query(cls._model).all()

