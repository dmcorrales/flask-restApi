from .extensions import db


class TaskService:

    @staticmethod
    def create(entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    @staticmethod
    def findAll(entity):
        return entity.query.all()

    @staticmethod
    def findById(entity,id):
        return entity.query.get(id)

    @staticmethod
    def update(entity):
        db.session.commit()
        return entity

    @staticmethod
    def delete(entity):
        db.session.delete(entity)
        db.session.commit()
        return entity
