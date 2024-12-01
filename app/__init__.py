from fastapi import FastAPI
import logging.config
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from app.log_config import LOGGING_CONFIG

# Load environment variables from .env file
load_dotenv()

# # Initialize logging
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)  # get a logger instance
 
app = FastAPI()
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins 
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


from app.routes import user