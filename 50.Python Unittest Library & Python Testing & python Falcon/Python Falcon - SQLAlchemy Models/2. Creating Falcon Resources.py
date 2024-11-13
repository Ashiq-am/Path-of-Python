import falcon
from sqlalchemy.orm import Session
from models import User, SessionLocal

class UserResource:
    def on_get(self, req, resp, user_id):
        session: Session = SessionLocal()
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            resp.media = {'id': user.id, 'name': user.name, 'email': user.email}
        else:
            resp.status = falcon.HTTP_404
            resp.media = {'error': 'User not found'}
        session.close()

    def on_post(self, req, resp):
        session: Session = SessionLocal()
        data = req.media
        user = User(name=data['name'], email=data['email'])
        session.add(user)
        session.commit()
        resp.media = {'id': user.id, 'name': user.name, 'email': user.email}
        session.close()

    def on_put(self, req, resp, user_id):
        session: Session = SessionLocal()
        data = req.media
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            user.name = data['name']
            user.email = data['email']
            session.commit()
            resp.media = {'id': user.id, 'name': user.name, 'email': user.email}
        else:
            resp.status = falcon.HTTP_404
            resp.media = {'error': 'User not found'}
        session.close()

    def on_delete(self, req, resp, user_id):
        session: Session = SessionLocal()
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
            resp.media = {'message': 'User deleted'}
        else:
            resp.status = falcon.HTTP_404
            resp.media = {'error': 'User not found'}
        session.close()
