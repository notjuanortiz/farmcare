FROM python:3.7-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install pipenv

# create /home/app directory in container
RUN mkdir -p /home/app
WORKDIR /home/app

# copy dependency files from host machine to /home/app/
COPY Pipfile Pipfile.lock /home/app/

# install application dependencies without virtual environment (via --system)
RUN pipenv install --system --deploy

# copy all files from host directory into /home/app/ (excludes files in .dockerignore)
COPY . /home/app/

# exposes port for internal consumption
EXPOSE 8000

# runs the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]