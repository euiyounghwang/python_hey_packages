
import pytest
import hey_utils
from hey_utils import otlp_grpc

@pytest.mark.skip(reason="no way of currently testing this")
def test_skip():
    assert 1 != 1

def test_module_func():
    response = hey_utils.get_test()
    assert response is not None
    assert response == "ok"
        
    
def test_gRPC():
    response = otlp_grpc.otlp_grpc().get_test()
    assert response is not None
    assert response == "Ok"
    
    
    
    
    