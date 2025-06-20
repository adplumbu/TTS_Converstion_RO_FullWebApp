# TTS_Conversion_RO_FullWebApp

This project contains a FastAPI backend and a Next.js frontend used to convert Romanian text to speech. To run the full application locally:

1. Install backend dependencies and start the server:

   ```bash
   cd tts_backend
   pip install -r requirements.txt
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. Prepare the frontend:
   ```bash
   cd ../tts_frontend
   pnpm install # or npm install
   cp .env.example .env.local
   pnpm dev # or npm run dev
   ```
   The `.env.local` file should contain the URL of the backend API, for example:
   ```env
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

The frontend will be available at http://localhost:3000 and will communicate with the backend via the configured API URL.
