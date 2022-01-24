FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . /api
#Installing system libs

COPY app/requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
WORKDIR /api
EXPOSE 4040