from run import app # Flask instance of the API

def test_homepage():
    response = app.test_client().get('/')
    assert response.status_code == 200


