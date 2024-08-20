import instill
import os

# Initialize Artifact service directly
artifact = instill.Artifact(api_token=os.environ["INSTILL_API_TOKEN"])

# Create a catalog
catalog = artifact.create_catalog(
    namespace_id="george_strong",
    name="sdk-test-catalog",
    description="This is a test catalog",
)

# Close the Artifact client
artifact.close()
