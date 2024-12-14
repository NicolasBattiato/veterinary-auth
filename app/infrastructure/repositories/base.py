from sqlalchemy.orm import Session
from typing import Any, List, Optional, Dict
from datetime import datetime

class BaseRepo:
    """Class to manage Base Repository."""
    
    _model = None  

    
    @classmethod
    def get_one(cls, db: Session, id: int, *args) -> Optional[Any]:
        """Retrieve a single resource by ID."""

        columns = [getattr(cls._model, arg) for arg in args] if args else [cls._model]
        return db.query(*columns).filter(cls._model.deleted_at.is_(None), cls._model.id == id).first()

    @classmethod
    def get_one_by_filters(cls, db: Session, filters: Dict[str, Any]) -> Optional[Any]:
        """Retrieve a resource by filters."""
        
        return db.query(cls._model).filter(cls._model.deleted_at.is_(None)).filter_by(**filters).first()

    def get_many(cls, db: Session, filters: Dict[str, Any]) -> List[Any]:
        """Retrieve multiple resources by filters."""
        
        return db.query(cls._model).filter(cls._model.deleted_at.is_(None)).filter_by(**filters).all()

    def get_all(cls, db: Session, *args) -> List[Any]:
        """Retrieve all resources."""

        columns = [getattr(cls._model, arg) for arg in args] if args else [cls._model]
        return db.query(*columns).filter(cls._model.deleted_at.is_(None)).all()

    def create(cls, db: Session, resource: Any) -> Any:
        """Creates a resource."""

        cls.db.add(resource)
        cls.db.commit()
        cls.db.refresh(resource)
        return resource

    def create_many(cls, db: Session, resources: List[Any]) -> List[Any]:
        """Creates many resources."""

        cls.db.bulk_save_objects(resources)
        cls.db.commit()
        return resources

    def update(cls, db: Session, id: int, payload: Dict[str, Any]) -> Optional[Any]:
        """Updates a resource by ID."""

        cls.db.query(cls._model).filter_by(id=id).filter(cls._model.deleted_at.is_(None)).update(payload)
        cls.db.commit()
        return cls.get_one(cls.db, id)

    def delete(cls, db: Session, id: int) -> bool:
        """Soft deletes a resource."""

        resource = cls.get_one(id)
        if resource:
            resource.deleted_at = datetime.now()
            cls.db.commit()
            return True
        return False

    def delete_by_filters(cls, db: Session, filters: Dict[str, Any]) -> bool:
        """Soft deletes all resources matching filters."""
        resources = cls.db.query(cls._model).filter_by(**filters).all()
        if resources:
            for resource in resources:
                resource.deleted_at = datetime.now()
            cls.db.commit()
            return True
        return False