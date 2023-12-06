FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit
RUN pip install pickle
RUN pip install torch

WORKDIR /repo
COPY . /repo
