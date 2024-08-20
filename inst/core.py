from .artifact import Artifact
from .model import Model
from .pipeline import Pipeline


class Core:
    def __init__(self, api_token: str, secure: bool = True,
                 url: str = "api.instill.tech"):
        from instill.clients import InstillClient
        from instill.configuration import global_config

        global_config.set_default(
            url=url,
            token=api_token,
            secure=secure,
        )

        self.client = InstillClient(async_enabled=True)

        # Initialize services
        self._artifact = None
        self._model = None
        self._pipeline = None

    @property
    def artifact(self):
        if self._artifact is None:
            self._artifact = Artifact(client=self.client)
        return self._artifact

    @property
    def model(self):
        if self._model is None:
            self._model = Model(client=self.client)
        return self._model

    @property
    def pipeline(self):
        if self._pipeline is None:
            self._pipeline = Pipeline(client=self.client)
        return self._pipeline

    # Additional methods relating to instill-core can be added here

    def close(self):
        self.client.close()
