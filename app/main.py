from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth_router

# create all tables in my sql (if not exists)
Base.metadata.create_all(bind= engine)

# initialize fastapi app
app = FastAPI(
    title="fast api auth system",
    description="fast api authentication"
)


# include router
app.include_router(auth_router.router)