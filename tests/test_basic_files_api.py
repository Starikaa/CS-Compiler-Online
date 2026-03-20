def test_create_file(client):

    r = client.post("/files/create", json={"filename": "main"})

    assert r.status_code == 200
    assert "main.cs" in r.text


def test_list_files_empty(client):

    r = client.get("/files/")

    assert r.status_code == 200
    assert r.json() == []


def test_read_file(client):

    client.post("/files/create", json={"filename": "main"})

    r = client.get("/files/main.cs")

    assert r.status_code == 200
    assert "Program" in r.text


def test_delete_file(client):

    client.post("/files/create", json={"filename": "main"})

    r = client.delete("/files/main")

    assert r.status_code == 200