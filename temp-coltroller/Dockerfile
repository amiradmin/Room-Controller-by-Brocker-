FROM python:3.8.3-alpine

RUN pip install -U pip

RUN adduser -D myuser
USER myuser
WORKDIR /home/myuser

COPY --chown=myuser:myuser requirements.txt requirements.txt
RUN pip3 install --user -r requirements.txt

ENV PATH="/home/myuser/.local/bin:${PATH}"

COPY --chown=myuser:myuser . .

CMD ["python3", "controller.py"]