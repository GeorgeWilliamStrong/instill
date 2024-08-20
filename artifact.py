
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

    def update_catalog(self, namespace_id: str, catalog_id: str,
                       description: str = "", tags: list = None):
        if tags is None:
            tags = []
        return self.client.artifact_service.update_catalog(
            namespace_id=namespace_id,
            catalog_id=catalog_id,
            description=description,
            tags=tags,
        )

    def list_catalogs(self, namespace_id: str):
        return self.client.artifact_service.list_catalogs(
            namespace_id=namespace_id)

    def delete_catalog(self, namespace_id: str, catalog_id: str):
        return self.client.artifact_service.delete_catalog(
            namespace_id=namespace_id,
            catalog_id=catalog_id,
        )

    def upload_catalog_file(self, namespace_id: str, catalog_id: str,
                            file_name: str, file_type: str, content: str):
        import instill.protogen.artifact.artifact.v1alpha.artifact_pb2 as \
            artifact_interface
        file = artifact_interface.File(name=file_name, type=file_type,
                                       content=content)
        return self.client.artifact_service.upload_catalog_file(
            namespace_id=namespace_id,
            catalog_id=catalog_id,
            file=file,
        )

    def process_catalog_files(self, file_uids: list):
        return self.client.artifact_service.process_catalog_files(
            file_uids=file_uids)

    def delete_catalog_file(self, file_uid: str):
        return self.client.artifact_service.delete_catalog_file(
            file_uid=file_uid)

    def list_catalog_files(self, namespace_id: str, catalog_id: str):
        return self.client.artifact_service.list_catalog_files(
            namespace_id=namespace_id,
            catalog_id=catalog_id,
        )

    def list_chunks(self, namespace_id: str, catalog_id: str, file_uid: str):
        return self.client.artifact_service.list_chunks(
            namespace_id=namespace_id,
            catalog_id=catalog_id,
            file_uid=file_uid,
        )

    def similarity_chunks_search(self, namespace_id: str, catalog_id: str,
                                 text_prompt: str, topK: int = 5):
        return self.client.artifact_service.similarity_chunks_search(
            namespace_id=namespace_id,
            catalog_id=catalog_id,
            text_prompt=text_prompt,
            topK=topK,
        )

    def close(self):
        self.client.close()
