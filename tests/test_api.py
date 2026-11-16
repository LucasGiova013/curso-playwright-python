def test_pagina_disponivel(api, app_url):
    resposta = api.get(app_url)
    assert resposta.status == 200
    assert "text/html" in resposta.headers["content-type"]
    assert "Lista de tarefas" in resposta.text()


def test_recurso_inexistente(api, app_url):
    resposta = api.get(f"{app_url}/nao-existe")
    assert resposta.status == 404
