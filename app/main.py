from fastapi import FastAPI
from app.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth_router

# create all tables in my sql (if not exists)
Base.metadata.create_all(bind= engine)

# initialize fastapi app
app = FastAPI(
    title="fast api auth system",
    description="fast api authentication"
)

# CORS configuration
origins = [
    # Vite dev server
    "http://localhost:5173",  
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # allows these origins
    allow_credentials=True,
    allow_methods=["*"],        # allows GET, POST, PUT, DELETE...
    allow_headers=["*"],        # allows all headers
)

# include router
app.include_router(auth_router.router)