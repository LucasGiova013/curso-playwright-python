from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

import pytest


@pytest.fixture(scope="session")
def app_url():
    diretorio = Path(__file__).resolve().parents[1] / "app"
    handler = partial(SimpleHTTPRequestHandler, directory=str(diretorio))
    servidor = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = Thread(target=servidor.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{servidor.server_port}"
    finally:
        servidor.shutdown()
        servidor.server_close()
        thread.join()
