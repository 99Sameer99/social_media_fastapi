from fastapi import FastAPI
from app.routers.vote import vote
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

#models.Base.metadata.create_all(bind=engine)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/") #path operation
async def root():
    return {"message": "First python API project testing"} # JSON

"""
@apiinstance.method('path or  URL')
specific path operation function
"""