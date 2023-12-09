FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit>=2022.3.3
RUN pip install scipy>=1.7.0
RUN pip install scikit-learn
RUN pip install git+https://github.com/bp-kelley/descriptastorus.git@86eedc60546abe6f59cdbcb12025a61157ba178d
RUN pip install tqdm>=4.62.2
RUN pip install typed-argument-parser==1.6.1
RUN pip install torch torchvision torchaudio -f https://download.pytorch.org/whl/cpu.html
RUN pip install tensorboardX==2.0
RUN pip install hyperopt
RUN pip install pandas-flavor==0.2.0
RUN pip install pandas>=0.24.0



WORKDIR /repo
COPY . /repo
