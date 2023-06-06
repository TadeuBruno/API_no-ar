FROM python:3
COPY . .
RUN pip install tinydb
RUN pip install fastapi
RUN pip install pydantic
RUN pip install uvicorn
ENTRYPOINT python -m uvicorn main:app --reload