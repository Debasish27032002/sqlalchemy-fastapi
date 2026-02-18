from models import User
from db import SessionLocal

# Insert data
def create_user(name, email):
    with SessionLocal() as session:
        try:
            user = User(name=name, email=email)
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
        except Exception as e:
            print(str(e))
            session.rollback()
            raise e
        finally:
            session.close()
            
# Fetch single user
def get_single_user(user_id):
    with SessionLocal() as session:
        try:
            user = session.query(User).filter(User.id == user_id).first()
            return user
        except Exception as e:
            print(str(e))
            raise e
        finally:
            session.close()

def get_all_user():
    with SessionLocal() as session:
        try:
            users = session.query(User).all()
            return users
        except Exception as e:
            print(str(e))
            raise e
        finally:
            session.close() 


def update_user_email(user_id, new_email):
    with SessionLocal() as session:
        try:
            user = session.query(User).filter(User.id == user_id).first()
            print(user)
            if user:
                user.email = new_email
                session.commit()
                session.refresh(user)
                return user
            else:
                print(f"User with id {user_id} not found.")
                return None
        except Exception as e:
            print(str(e))
            session.rollback()
            raise e
        finally:
            session.close()
            
            
# Delete user
def delete_user(user_id):
    with SessionLocal() as session:
        try:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                session.delete(user)
                session.commit()
                print(f"User with id {user_id} deleted successfully.")
            else:
                print(f"User with id {user_id} not found.")
        except Exception as e:
            print(str(e))
            session.rollback()
            raise e
        finally:
            session.close()