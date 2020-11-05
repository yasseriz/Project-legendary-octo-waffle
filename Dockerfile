FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY . .
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
EXPOSE 8000
CMD [ "python", "main.py" ]