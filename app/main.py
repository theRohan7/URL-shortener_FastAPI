from fastapi  import FastAPI
from app.routes import url_routes
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title='URL Shortner')

app.include_router(url_routes.router)