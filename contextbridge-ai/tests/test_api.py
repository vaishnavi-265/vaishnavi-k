from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}


def test_build_context():
    payload = {
        'source_provider': 'gemini',
        'target_provider': 'chatgpt',
        'max_chars': 2000,
        'messages': [
            {'role': 'user', 'content': 'We decided to use FastAPI for the backend.'},
            {'role': 'assistant', 'content': 'We will use PostgreSQL and Docker.'},
            {'role': 'user', 'content': 'Authentication must use OAuth2.'}
        ]
    }
    response = client.post('/v1/context/build', json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body['source_provider'] == 'gemini'
    assert body['target_provider'] == 'chatgpt'
    assert body['original_message_count'] == 3
    assert len(body['decisions']) >= 1
    assert len(body['requirements']) >= 1
