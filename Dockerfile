FROM python:3.10-slim

WORKDIR/ app

COPY requirement.txt

RUN pip install --no-cache-dir -r requirement.txt

COPY . .

EXPOSE 7860

CMD [ "python", "-u", 'UI.py' ]