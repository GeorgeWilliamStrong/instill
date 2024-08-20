
class Artifact:
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

    def create_catalog(self, namespace_id: str, name: str,
                       description: str = "", tags: list = None):
        if tags is None:
            tags = []
        return self.client.artifact_service.create_catalog(
            namespace_id=namespace_id,
            name=name,
            description=description,
            tags=tags,
        )

    def close(self):
        self.client.close()
