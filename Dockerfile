FROM python:3.8
WORKDIR /app
RUN pip install pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --dev
COPY . .
EXPOSE 8080
CMD ["python", "/app/main.py"]