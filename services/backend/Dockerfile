# syntax=docker/dockerfile:1

FROM python:3.10.1

WORKDIR /app

COPY requirements.txt requirements.txt
COPY gen_lua.py gen_lua.py
COPY luator.py luator.py
COPY template.lua template.lua

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "gen_lua:app", "--host", "0.0.0.0", "--port", "5000"]