# AI Chatbot with CI/CD

A FastAPI chatbot powered by an AI API, containerized with Docker and tested automatically with GitHub Actions.

## Tech Stack
- Python, FastAPI
- Docker
- GitHub Actions (CI)
- Anthropic API

## Run locally
    pip install -r requirements.txt
    set ANTHROPIC_API_KEY=your-key
    uvicorn main:app --reload

## Run with Docker
    docker build -t ai-chatbot-devops .
    docker run -p 8000:8000 -e ANTHROPIC_API_KEY=your-key ai-chatbot-devops
