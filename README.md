# Instill AI Python SDK Prototype

This repo serves as a prototype design for interacting with Instill AI services, including Artifact, Model, and Pipeline. The SDK offers two initialization methods for flexibility in configuration and usage.

> **Important:** This repository acts as a wrapper around the current Instill Python SDK, which uses the `instill` namespace. To avoid naming conflicts with the original SDK, this wrapper uses the `inst` namespace instead. In the examples and tests, `inst` is used; however, the actual SDK implementation will use `instill`.

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
import inst

# Initialize Artifact service directly
artifact = inst.Artifact(api_token="YOUR_INSTILL_API_TOKEN")

# Create a catalog
catalog = artifact.create_catalog(
    namespace_id="your-namespace-id",
    name="Your Catalog Name",
    description="A brief description of your catalog"
)
```

#### `Pipeline`

```python
import inst

# Initialize Pipeline service directly
pipeline = inst.Pipeline(api_token="YOUR_INSTILL_API_TOKEN")

# Define inputs
inputs = [{"prompt": "hello world"}]

# Trigger the pipeline
response = pipeline.run_pipeline(
    pipeline_id="your-pipeline-id",
    inputs=inputs
)
```

#### `Model`

```python
import inst

# Initialize Model service directly
model = inst.Model(api_token="YOUR_inst_API_TOKEN")

task_inputs = [
    inst.protogen.model.model.v1alpha.model_pb2.TaskInput(
        classification={"imageUrl": "https://artifacts.instill.tech/imgs/dog.jpg"}
    ),
    inst.protogen.model.model.v1alpha.model_pb2.TaskInput(
        classification={"imageUrl": "https://artifacts.instill.tech/imgs/bear.jpg"}
    ),
]

# Trigger the model
response = model.trigger_model(
    model_id="your-model-id",
    task_inputs=task_inputs,
    version_tag="your-version-tag"
)
```

### 2. Centralized Initialization via `Core`

```python
import inst

# Initialize Core with global configuration
core = inst.Core(api_token="YOUR_INSTILL_API_TOKEN")

# Access and use Artifact service
artifact = core.artifact
catalog = artifact.create_catalog(
    namespace_id="your-namespace-id",
    name="Your Catalog Name",
    description="A brief description of your catalog"
)

# Access and use Pipeline service
pipeline = core.pipeline
pipeline_response = pipeline.run_pipeline(
    pipeline_id="your-pipeline-id",
    inputs=[{"prompt": "hello world"}]
)

# Access and use Model service
model = core.model
response = model.trigger_model(
    model_id="your-model-id",
    task_inputs=[
        inst.protogen.model.model.v1alpha.model_pb2.TaskInput(
            classification={"imageUrl": "https://artifacts.instill.tech/imgs/dog.jpg"}
        ),
        inst.protogen.model.model.v1alpha.model_pb2.TaskInput(
            classification={"imageUrl": "https://artifacts.instill.tech/imgs/bear.jpg"}
        ),
    ],
    version_tag="your-version-tag"
)
```
