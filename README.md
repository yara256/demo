### Activate virtualenv
1. Install virtualenv lib from your console
pip install virtualenv

2. Open 'demo' project and create venv:
python -m venv ./.venv

3. Activate virtual env
run activate.bat file in .venv/Scripts


#### Run tests

1. Install required dependencies into a python 3 virtualenv

```
pip install -r requirements.txt
```

2.Execute tests against ephemeral environment, providing --admin_api_base_url and --customer_api_base_url variables

```
pytest tests/api
```

#### Generate report

```
pytest  -sv --alluredir=tests/allure-results tests/api
allure generate ./tests/allure-results –clean
allure open
```
