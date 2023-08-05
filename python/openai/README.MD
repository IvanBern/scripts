# OpenAI scripts

Welcome to the documentation for OpenAI Scripts This guide will walk you through the steps to create a new virtual environment and install project dependencies using the provided `requirements.txt` file.

## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.x
- pip (Python package manager)

### Setup

1.  **Clone the Repository:**

2. **Create a Virtual Environment:**

To isolate project dependencies, it's recommended to create a virtual environment. Run the following commands to create and activate a new virtual environment:

On macOS and Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
On Windows (using Command Prompt):
```bash
python -m venv venv
venv\Scripts\activate
```

On Windows (using PowerShell):
```shell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. **Install Project Dependencies:**

Once the virtual environment is activated, use pip to install the project dependencies from the requirements.txt file:

```bash
pip install -r requirements.txt
```
This will install all the required packages and their dependencies into the virtual environment.

4. **Deactivate the Virtual Environment:**

When you're done working on the project, you can deactivate the virtual environment using the following command:

```bash
deactivate
```

### Usage

1. **Activate the Virtual Environment:**

Before working on your project, always activate the virtual environment:

On macOS and Linux:
```bash
source venv/bin/activate
```

On Windows (using Command Prompt):
```bash
venv\Scripts\activate
```
On Windows (using PowerShell):
```bash
.\venv\Scripts\Activate.ps1
```

2. **Deactivate the Virtual Environment:**

When you're done, deactivate the virtual environment as mentioned earlier.