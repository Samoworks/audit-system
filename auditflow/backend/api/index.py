"""Vercel serverless entrypoint.

Vercel's Python runtime looks for a module-level `app` object (WSGI/ASGI)
in files under api/. This re-exports the exact same FastAPI app instance
used by the Render deployment (uvicorn app.main:app), so behavior is
identical between the two platforms.
"""

from app.main import app  # noqa: F401
