import os

os.environ.setdefault("ANTHROPIC_API_KEY", "test-key")

from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient

import main

api = TestClient(main.app)


def test_home():
    r = api.get("/")
    assert r.status_code == 200


def test_health():
    r = api.get("/health")
    assert r.json() == {"status": "ok"}


def test_chat_returns_reply():
    fake = MagicMock()
    fake.content = [MagicMock(text="Hello!")]
    with patch.object(main.client.messages, "create", return_value=fake):
        r = api.post("/chat", json={"message": "Hi"})
    assert r.status_code == 200
    assert r.json() == {"reply": "Hello!"}


def test_chat_rejects_empty_message():
    r = api.post("/chat", json={"message": ""})
    assert r.status_code == 422
