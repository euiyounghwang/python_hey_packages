
import pytest
import search_monitoring_tools

''' import module via packages '''
''' reinstall the package 
pip install ./dist/*.whl --force-reinstall
'''
# from search_monitoring_tools import otlp_grpc

# import module directly based on the path
from src.search_monitoring_tools.otlp.otlp_grpc import otlp_grpc


@pytest.mark.skip(reason="no way of currently testing this")
def test_skip():
    assert 1 != 1

def test_module_func():
    response = search_monitoring_tools.get_test()
    assert response is not None
    assert response == "ok"
        
    
def test_gRPC(mock_opentelemetrics_grpc_url):
    otlp_instance = otlp_grpc(mock_opentelemetrics_grpc_url)

    response = otlp_instance.get_test()
    assert response is not None
    assert response == "Ok"

    response = otlp_instance.get_otlp_host()
    assert response == "http://localhost:4318/v1/metrics"
    assert response == mock_opentelemetrics_grpc_url

    ''' Varify if metrics can be sent via grPC to the Opentelemetry Server'''
    # response = otlp_instance.push_prometheus_via_grpc()
    # assert response is not None
    # print(response)

    
    
    
    
    