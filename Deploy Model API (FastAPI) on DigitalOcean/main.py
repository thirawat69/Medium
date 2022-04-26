# 1. Library imports
from fastapi import FastAPI
import uvicorn

# 2. Create the app object
app = FastAPI()

# 3. Test Server
@app.get('/')
def get_root():
    return "Server start!"
