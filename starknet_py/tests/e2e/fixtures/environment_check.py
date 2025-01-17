import pytest

from starknet_py.constants import DEFAULT_DEPLOYER_ADDRESS
from starknet_py.utils.data_transformer.universal_deployer_serializer import (
    universal_deployer_abi,
)


@pytest.fixture(scope="module", autouse=True)
async def check_if_udc_is_deployed(client):
    class_hash = await client.get_class_hash_at(
        contract_address=DEFAULT_DEPLOYER_ADDRESS
    )

    assert isinstance(class_hash, int)
    assert class_hash != 0


@pytest.fixture(scope="module", autouse=True)
async def check_if_udc_has_expected_abi(gateway_client):
    code = await gateway_client.get_code(contract_address=DEFAULT_DEPLOYER_ADDRESS)

    assert code.abi == universal_deployer_abi
