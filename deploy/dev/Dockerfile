FROM python:3.11-slim
LABEL maintainer="sa5mchavez"
WORKDIR /app

COPY . .
# RUN pip install --no-cache-dir -r requirements-dev.txt
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000
# EXPOSE 5432

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]