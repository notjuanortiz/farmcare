FROM python:3.7-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install pipenv

RUN mkdir -p /home/app
WORKDIR /home/app

COPY Pipfile Pipfile.lock /home/app/
RUN pipenv install --system --deploy

COPY . /home/app/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]