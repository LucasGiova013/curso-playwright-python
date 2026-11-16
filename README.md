# Curso de Playwright com Python e pytest

Repositório de estudos para acompanhar o [curso na Udemy](https://www.udemy.com/course/playwright-python-automation-testing-pytest/).

Os exemplos iniciais são próprios e não reproduzem o conteúdo das aulas.

## Preparar o ambiente

Requisitos: Python 3.11 ou superior e Git.

```bash
python -m venv .venv
```

Ative o ambiente:

- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- Linux/macOS: `source .venv/bin/activate`

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
pytest
```

No Linux, se faltarem dependências do navegador: `python -m playwright install --with-deps chromium`.

## Comandos úteis

```bash
pytest --headed                 # Exibir navegador
pytest --browser chromium       # Selecionar navegador
pytest tests/test_interface.py   # Executar um arquivo
pytest --tracing retain-on-failure --screenshot only-on-failure
python -m playwright codegen     # Explorar o gravador de ações
```

Os exemplos usam um servidor local iniciado e encerrado pelo pytest. Não exigem conta nem acesso a sites externos durante os testes.

## Estrutura

- `tests/`: testes de interface e API, com fixtures no `conftest.py`.
- `pages/`: exemplo de Page Object para a lista de tarefas.
- `app/`: aplicação de prática servida localmente.
- `anotacoes/`: registro do aprendizado.
- `exercicios/`: desafios para praticar.
- `.github/workflows/tests.yml`: execução no GitHub Actions.

## Roteiro de estudo sugerido

1. Preparar Python, ambiente virtual e pytest.
2. Entender fixtures, seletores e asserções com espera automática.
3. Executar testes com dados parametrizados.
4. Organizar ações com Page Objects.
5. Explorar testes de API e depuração com traces.
6. Executar a suíte no GitHub Actions.

Registre suas próprias anotações conforme avança no curso. Não publique materiais protegidos, credenciais ou arquivos `.env`.
