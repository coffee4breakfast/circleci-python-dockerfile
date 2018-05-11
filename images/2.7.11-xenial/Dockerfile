FROM circleci/buildpack-deps:xenial

ENV PYTHON_VERSION 2.7.11

RUN sudo apt-get update -q -y && sudo apt-get install --no-install-recommends --fix-missing -y \
    libhdf5-dev \
  && sudo apt-get autoremove -y \
  && sudo apt-get clean all

ENV PYENV_ROOT /home/circleci/.pyenv

RUN git clone https://github.com/pyenv/pyenv.git $PYENV_ROOT \
  && git clone https://github.com/pyenv/pyenv-virtualenv.git $PYENV_ROOT/plugins/pyenv-virtualenv

ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN CFLAGS="-O2" \
  pyenv install $PYTHON_VERSION \
  && pyenv global $PYTHON_VERSION \
  && rm -f $PYENV_ROOT/cache/*

RUN pip install --no-cache-dir --upgrade setuptools pip
