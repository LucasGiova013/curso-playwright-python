def test_pagina_disponivel(request, app_url):
    resposta = request.get(app_url)
    assert resposta.status == 200
    assert "text/html" in resposta.headers["content-type"]
    assert "Lista de tarefas" in resposta.text()


def test_recurso_inexistente(request, app_url):
    resposta = request.get(f"{app_url}/nao-existe")
    assert resposta.status == 404
