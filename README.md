# TTS Conversion RO FullWebApp

## Overview
This repository contains a simple text-to-speech web application for Romanian. It combines a FastAPI backend for speech synthesis with a Next.js frontend interface. The code is meant for experimentation and local use.

## Features
- REST API built with FastAPI to generate audio from Romanian text
- Web interface built with Next.js and Tailwind CSS
- Ability to pick between multiple preconfigured voices

## Requirements
- Python 3.10+
- Node.js 18+
- `pnpm` for frontend package management

## Setup
### Backend
```bash
cd tts_backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend
```bash
cd tts_frontend
pnpm install
# set the API address
export NEXT_PUBLIC_API_URL="http://localhost:8000"
pnpm dev
```

## Usage
Run both servers as described above. Open the frontend in a browser (`http://localhost:3000` by default) and enter Romanian text to convert it to speech.

## Project Layout
```
root
├── tts_backend     # FastAPI application
│   └── app         # Backend source code
├── tts_frontend    # Next.js frontend
│   └── app         # Frontend pages and components
```

## Tips/Troubleshooting
- Ensure `NEXT_PUBLIC_API_URL` points to your running backend.
- If you encounter large files in version control (e.g. `.pth` model files, `.pyc` caches), consider removing them in the future.

## License
This project is released under the MIT License.
