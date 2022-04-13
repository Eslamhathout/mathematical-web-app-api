# Mathematical Web Service

A web service which calculates and provides results for the following algorithms via a REST API:

* The n:th Fibonacci number F(n) with the value of n provided by the user.
* The Ackermann function A(m,n) with values of m and n provided by the user.
* The factorial n! of a non-negative integer n provided by the user.

## Installation

To be ready to run the project as fast as possible use the docker-compose :
```bash
docker-compose build
```

Install the project requirements using pip:

```bash
docker-compose run app sh -c "pip install -r requirmments.txt"
```

Run the app server
```bash
docker-compose run app sh -c "python manage.py runserver"
```

## API Usage

To use the website navigate to the following links:
```python
# Ackermann API example:
http://your_host:your_app_port/ackermann/?number1=2&&number2=3

# Facorial API example:
http://your_host:your_app_port/factorial/?number=5

# Fibonacci API example:
http://your_host:your_app_port/fibonacci/?number=10

```

## Testing & Linting
The app contains test cases for each function you can find the test file by navigating to app/[function_name]/tests/test_view.py file. In order to fun the 3 function tests with linting tools use the following command:
```bash
docker-compose run app sh -c "python manage.py test && flake8 --max-line-length 120 && isort"
```
## CI Automation
The project contains a yml file that hold the configuration for travise CI which will be used to test the code and checks the code against the linting tools such as flake8 and isort in order to maintain a healthy/clean code on production.

## Contributing
This is a task for Klarna
## License
[MIT](https://choosealicense.com/licenses/mit/)