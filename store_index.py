from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

# Load environment variables

import os
os.environ["PINECONE_API_KEY"] = "pcsk_pvaPW_RVnbqyFvAGxfJntq28248sx8Rzzp6JoUZ1qyiYqt2M7VqKy5BiFzgm9TMvXfNKE"
PINECONE_API_KEY = "pcsk_pvaPW_RVnbqyFvAGxfJntq28248sx8Rzzp6JoUZ1qyiYqt2M7VqKy5BiFzgm9TMvXfNKE"

pc = Pinecone(api_key=PINECONE_API_KEY)

extracted_data = load_pdf_file(r'C:\Users\Admin\Timmyxz-End-to-end-Medical-Chatbot\Data')
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

# Create or use existing index
index_name = "medical-chatbot"

# Check if index already exists, if not create it
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

# Create vector store
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings
)

print("Index created successfully!")