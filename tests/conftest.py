import pytest

''' The conftest.py is the Python file in which various functions are declared which can be accessed across various test files.'''

@pytest.fixture
def mock_opentelemetrics_grpc_url():
    return "http://localhost:4318/v1/metrics"


@pytest.fixture
def sample_data():
    """테스트에서 사용할 공통 데이터 제공"""
    return {"id": 1, "name": "test_user"}