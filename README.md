# Instill AI Python SDK Prototype

This repo serves as a prototype design for interacting with Instill AI services, including Artifact, Model, and Pipeline. The SDK offers two initialization methods for flexibility in configuration and usage.

## Repository Structure

This repository contains the following modules:

- **`core.py`**: Provides centralized configuration and access to the Artifact, Model, and Pipeline services.
- **`artifact.py`**: Contains the `Artifact` class for managing artifact-related operations.
- **`model.py`**: Contains the `Model` class for managing model operations.
- **`pipeline.py`**: Contains the `Pipeline` class for managing pipeline operations.

## Dual Initialization Method

### Overview

The SDK supports dual initialization:
1. **Direct Service Initialization**: Initialize each service (`Artifact`, `Model`, `Pipeline`) independently with its own configuration.
2. **Centralized Initialization via `Core`**: Configure global settings once and access all services through a single `Core` instance.

### Advantages

- **Direct Initialization**: Offers flexibility for cases where different services might require different configurations or if you prefer not to use a central configuration.
- **Centralized Initialization**: Simplifies configuration management by setting global parameters (e.g., API token) once. Ensures consistency across services and reduces redundancy.

## Usage Examples

### 1. Direct Service Initialization

#### `Artifact`

```python
import instill

# Initialize Artifact service directly
artifact = instill.Artifact(api_token="YOUR_INSTILL_API_TOKEN")

# Create a catalog
catalog = artifact.create_catalog(
    namespace_id="your-namespace-id",
    name="Your Catalog Name",
    description="A brief description of your catalog"
)

# Close the Artifact client
artifact.close()
```

#### `Model`

```python
import instill

# Initialize Model service directly
model = instill.Model(api_token="YOUR_INSTILL_API_TOKEN")

task_inputs = [
    instill.protogen.model.model.v1alpha.model_pb2.TaskInput(
        classification={"imageUrl": "https://artifacts.instill.tech/imgs/dog.jpg"}
    ),
    instill.protogen.model.model.v1alpha.model_pb2.TaskInput(
        classification={"imageUrl": "https://artifacts.instill.tech/imgs/bear.jpg"}
    ),
]

# Trigger the model
response = model.trigger_model(
    model_id="your-model-id",
    task_inputs=task_inputs,
    version_tag="your-version-tag"
)

# Close the Model client
model.close()
```

#### `Pipeline`

```python
import instill

# Initialize Pipeline service directly
pipeline = instill.Pipeline(api_token="YOUR_INSTILL_API_TOKEN")

# Define inputs
inputs = [{"prompt": "hello world"}]

# Trigger the pipeline
response = pipeline.run_pipeline(
    pipeline_id="your-pipeline-id",
    inputs=inputs
)

# Close the Pipeline client
pipeline.close()
```

### 2. Centralized Initialization via `Core`

```python
import instill

# Initialize Core with global configuration
core = instill.Core(api_token="YOUR_INSTILL_API_TOKEN")

# Access and use Artifact service
artifact = core.artifact
catalog = artifact.create_catalog(
    namespace_id="your-namespace-id",
    name="Your Catalog Name",
    description="A brief description of your catalog"
)

# Access and use Model service
model = core.model
response = model.trigger_model(
    model_id="your-model-id",
    task_inputs=[
        instill.protogen.model.model.v1alpha.model_pb2.TaskInput(
            classification={"imageUrl": "https://artifacts.instill.tech/imgs/dog.jpg"}
        ),
        instill.protogen.model.model.v1alpha.model_pb2.TaskInput(
            classification={"imageUrl": "https://artifacts.instill.tech/imgs/bear.jpg"}
        ),
    ],
    version_tag="your-version-tag"
)

# Access and use Pipeline service
pipeline = core.pipeline
pipeline_response = pipeline.run_pipeline(
    pipeline_id="your-pipeline-id",
    inputs=[{"prompt": "hello world"}]
)

# Close the Core client
core.close()
```
