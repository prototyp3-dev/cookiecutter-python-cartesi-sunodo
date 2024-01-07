import pytest

from cartesi.testclient import TestClient

import {{ cookiecutter.package_name }}.dapp


@pytest.fixture
def dapp_client() -> TestClient:
    client = TestClient({{ cookiecutter.package_name }}.dapp.dapp)
    return client


def test_should_echo(dapp_client: TestClient):

    hex_payload = '0x' + 'hello'.encode('utf-8').hex()
    dapp_client.send_advance(hex_payload=hex_payload)

    assert dapp_client.rollup.status
    assert len(dapp_client.rollup.notices) > 0
    assert dapp_client.rollup.notices[-1]['data']['payload'] == hex_payload
