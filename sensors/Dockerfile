FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python3.7
RUN apt-get -y install python3-pip
RUN useradd -ms /bin/bash myuser
RUN apt-get -y install python-numpy
USER myuser
WORKDIR /home/myuser

COPY --chown=myuser:myuser requirements.txt requirements.txt
RUN pip3 install --user -r requirements.txt

ENV PATH="/home/myuser/.local/bin:${PATH}"

COPY --chown=myuser:myuser . .
# CMD ["python3", "code/app.py"]