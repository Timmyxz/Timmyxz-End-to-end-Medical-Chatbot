# Timmyxz-End-to-end-Medical-Chatbot

An end-to-end medical chatbot implementation using LangChain and Pinecone for vector storage.

## Prerequisites

- Python 3.10 or 3.11 (recommended for better package compatibility)
  - Note: Python 3.13 may cause installation issues with some packages that don't have pre-built wheels yet

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   PINECONE_API_KEY=your_pinecone_api_key
   PINECONE_ENVIRONMENT=your_pinecone_environment
   ```

## Project Structure

(TBD - To be developed)

## Usage

(TBD - To be developed)

## Troubleshooting

If you encounter installation issues:
1. Ensure you're using Python 3.10 or 3.11
2. If using Python 3.13, you may need to install Microsoft C++ Build Tools to compile packages from source