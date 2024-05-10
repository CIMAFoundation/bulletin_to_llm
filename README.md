# bulletin to llm test

clone the repository

```bash
git clone https://github.com/CIMAFoundation/bulletin_to_llm.git
```

cd into the directory

```bash
cd bulletin-to-llm
```

create the virtual environment with conda

```bash
conda create --prefix .venv/ python=3.10
```

activate the virtual environment

```bash
conda activate .venv/
```

install the dependencies

```bash
pip install -r requirements.txt
```


add your openai key to the .env file

```bash
OPENAI_API_KEY=your_key_here
```

run the script

```bash
python main.py
```