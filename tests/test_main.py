from app.main import app

def test_home():
    r = app.test_client().get('/')
    assert r.status_code == 200
    assert r.json['status'] == 'running'

def test_health():
    r = app.test_client().get('/health')
    assert r.json['status'] == 'ok'