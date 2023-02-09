FROM python:latest

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./

RUN alembic upgrade head  

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
