# Madagascar Legal Database Prototype

This directory contains a minimal FastAPI application that serves as a starting
point for a legal document search tool for Madagascar's laws. The application
exposes endpoints to list available laws and retrieve a single law by ID. At the
moment, it uses an in-memory list of laws as a placeholder.

## Quickstart

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:

   ```bash
   uvicorn app:app --reload
   ```

The API will be available at `http://localhost:8000` and you can browse the
interactive documentation at `/docs`.
