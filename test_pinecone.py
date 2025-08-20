from pinecone import Pinecone
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key from environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Test Pinecone connection
try:
    pc = Pinecone(api_key=PINECONE_API_KEY)
    print("Pinecone client initialized successfully!")
    
    # List existing indexes (this will verify the API key works)
    indexes = pc.list_indexes().names()
    print(f"Existing indexes: {list(indexes)}")
    
except Exception as e:
    print(f"Error connecting to Pinecone: {e}")
    print("Please check your API key in the .env file")