FROM python:3.12.3-alpine3.19

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD ["sh" , "-c", "alembic upgrade head && python -m src"]