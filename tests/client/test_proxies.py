import pytest

import httpx


def test_invalid_proxy():
    url = "https://example.org/"
    proxies = "invalid_proxy"

    with httpx.Client() as client:
        with pytest.raises(TypeError):
            client.get(url, proxies=proxies)
