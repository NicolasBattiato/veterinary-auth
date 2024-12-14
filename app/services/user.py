from app.infrastructure.repositories.user import UserRepo
from app.core.security import create_refresh_token, verify_password
from app.domain.user import UserCreate


def register_user(db, user_data: UserCreate):
    existing_user = UserRepo.get_user_by_email(db, user_data.email)
    if existing_user:
        return None  # Usuario ya registrado
    new_user = UserRepo.create_user(db, user_data)
    return new_user

def delete_user(db, user):
    return UserRepo.soft_delete_user(db, user)

def activate_user(db, user):
    return UserRepo.verify_user(db, user)

def refresh_access_token(user_data: dict):
    return create_refresh_token(user_data)