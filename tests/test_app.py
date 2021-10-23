from src import app

app.testing = True
client = app.test_client()


def test_index():
    response = client.get("/api/v1/hello-world-7")
    assert b"Hello World 7!" in response.date
