from app.rest.database.dbhandler import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()