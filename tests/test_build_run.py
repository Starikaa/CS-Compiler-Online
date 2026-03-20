def test_build_lexer_error(client):

    client.post("/files/create", json={"filename": "lex"})

    client.post("/files/edit/lex.cs", json={"content": "@@@@"})

    r = client.post("/files/build/lex.cs")
    assert r.status_code == 200
    assert "Lexer error:\nError Token @\n" == r.json()

def test_build_parser_error(client):

    client.post("/files/create", json={"filename": "lex"})

    client.post("/files/edit/lex.cs", json={"content": "print(1)"})

    r = client.post("/files/build/lex.cs")
    assert r.status_code == 200
    assert "Parser error:\nError on line 1 col 8: <EOF>\n" == r.json()

def test_build_semantic_error(client):

    client.post("/files/create", json={"filename": "lex"})

    client.post("/files/edit/lex.cs", json={"content": "print(a);"})

    r = client.post("/files/build/lex.cs")
    assert r.status_code == 200
    assert "Static Checker error:\nUndeclared Identifier: a\n" == r.json()

def test_run_success1(client):

    client.post("/files/create", json={"filename": "runok"})

    client.post("/files/build/runok.cs")

    r = client.get("/files/run")

    assert r.status_code == 200
    assert "7\n" == r.json()

def test_run_success2(client):

    client.post("/files/create", json={"filename": "runok"})

    client.post("/files/edit/runok.cs", json={
        "content": """
            const a = 2;
            print(a + 3);
        """
    })

    client.post("/files/build/runok.cs")

    r = client.get("/files/run")

    assert r.status_code == 200
    assert "5\n" == r.json()