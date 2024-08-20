
class Model:
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

    def trigger_model(self, model_id: str, task_inputs: list, version_tag: str):

        return self.client.model_service.trigger_model(
            model_id=model_id,
            task_inputs=task_inputs,
            version_tag=version_tag
        )

    # Additional methods for handling models can be added here

    def close(self):
        self.client.close()
