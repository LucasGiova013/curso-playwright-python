import pytest
from playwright.sync_api import expect

from pages.tarefas_page import TarefasPage


@pytest.mark.parametrize("texto", ["Estudar seletores", "Praticar pytest"])
def test_adicionar_tarefa(page, app_url, texto):
    tarefas = TarefasPage(page)
    tarefas.abrir(app_url)
    tarefas.criar_tarefa(texto)
    expect(tarefas.itens).to_have_text([texto])
    expect(tarefas.campo).to_be_empty()


def test_rejeitar_tarefa_sem_texto(page, app_url):
    tarefas = TarefasPage(page)
    tarefas.abrir(app_url)
    tarefas.criar_tarefa("   ")
    expect(tarefas.itens).to_have_count(0)
