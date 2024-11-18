import uvicorn

from lab.main import app
from lab.config import settings

if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
