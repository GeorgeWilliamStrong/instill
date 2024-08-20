
class Pipeline:
    def __init__(self, client=None, api_token=None, secure: bool = True,
                 url: str = "api.instill.tech"):
        from instill.clients import InstillClient
        from instill.configuration import global_config

        if client:
            self.client = client
        else:
            global_config.set_default(
                url=url,
                token=api_token,
                secure=secure,
            )
            self.client = InstillClient(async_enabled=True)

    def trigger_pipeline(self, pipeline_id: str, inputs: list, data: list):
        return self.client.pipeline_service.trigger_pipeline(
            pipeline_id=pipeline_id,
            inputs=inputs,
            data=data
        )

    # Additional methods for handling pipelines

    def close(self):
        self.client.close()
