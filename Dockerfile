FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit
RUN pip install pickle

<<<<<<< HEAD
=======
RUN pip install pickle
>>>>>>> 1e590b181eaf8eb2ee69c1465c11076af1271916

WORKDIR /repo
COPY . /repo
