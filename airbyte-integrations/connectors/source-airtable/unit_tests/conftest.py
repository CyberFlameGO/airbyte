#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#

import pytest


@pytest.fixture
def test_config():
    return {"api_key": "key1234567890", "base_id": "app1234567890", "tables": ["Imported table", "Table 2"]}