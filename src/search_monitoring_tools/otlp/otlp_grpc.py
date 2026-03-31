class otlp_grpc:

    def __init__(self, otlp_host):
        """Processes input data.
        :param otlp_host: the name of otlp_host.
        :param bool verbose: Enable detailed logging, defaults to False.
        :return: A dictionary of results.
        :rtype: dict
        """
        
        self.otlp_host = otlp_host
   
    def get_test(self):
        """get_test.
        :return: String of results.
        :rtype: string
        """
        return "Ok"
    
    def get_otlp_host(self):
        """Get the name of otlp host.
        :rtype: string
        """
        
        return self.otlp_host
