# Chat Agent

A simple chat agent project built with Python. This project provides a basic framework for building conversational AI applications.

## Features

- Modular codebase for easy extension
- Simple setup and execution
- Ready for local development

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Viktechenthu/chatAgent.git
cd chat-agent
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Project with `uv`

[uv](https://github.com/astral-sh/uv) is a fast Python package manager and runner.

#### Install `uv` (if not already installed):

```bash
pip install uv
```

#### Run the application:

```bash
uv pip install -r requirements.txt
uv pip run python main.py
```

Replace `main.py` with your project's entry point if different.

## Project Structure

```
chat-agent/
├── main.py
├── README.md
├── requirements.txt
└── ...
```
