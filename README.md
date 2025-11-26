# `pytest_texts_score_example`

A minimal example project demonstrating how to structure a Python package using the modern `src/` layout and how to test it with `pytest`, including usage alongside the `pytest-texts-score` plugin.

This repository also documents a common issue developers face when using `src/` layouts:
**pytest cannot import your package unless it is properly installed or correctly configured.**

---

## 📁 Project Structure

```
pytest-texts-score-example/
│
├── pyproject.toml
├── pytest.ini.example
├── README.md
│
├── src/
│   └── pytest_texts_score_example/
│       ├── __init__.py
│       └── main.py
│
└── tests/
    └── test_mock_testing.py
```

## 🛠️ Setup:
### Creating Your pytest.ini

This project includes a pytest.ini.example file that demonstrates the required configuration for running tests together with the pytest-texts-score plugin.

#### Step 1
```sh
    cp pytest.ini.example pytest.ini
```
#### Step2
Open pytest.ini and provide values for the required fields 

## 📦 Installation

### Option 1 — Using **uv** (recommended)

```sh
uv pip install -e .
```

### Option 2 — Using pip

```sh
pip install -e .
```

### Verify installation

```sh
python -c "import pytest_texts_score_example; print('Package imported successfully!')"
```

If you see the message, the package is correctly installed.

---

## 🧪 Running Tests

After installing the project:

### With uv

```sh
uv run pytest
```

### With normal Python

```sh
pytest
```
