FROM python:3
COPY . .
RUN pip install tinydb
RUN pip install fastapi
RUN pip install pydantic
ENTRYPOINT python -m uvicorn main:app --reload