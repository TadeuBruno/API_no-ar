FROM python:3
COPY . .
WORKDIR /app_api
RUN pip install tynidb
RUN pip install fastapi
RUN pip install pydantic
ENTRYPOINT python -m uvicorn main:app --reload