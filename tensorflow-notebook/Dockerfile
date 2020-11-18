# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=jupyter/scipy-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

ADD jupyter_notebook_config.py /home/${NB_USER}/.jupyter

# Install Tensorflow
RUN pip install --quiet --no-cache-dir \
        tensorflow==2.3.0 \ 
        jupyter-server-proxy && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}" && \
    conda install -c conda-forge jupyter_conda
USER root    
RUN apt install ssh
USER ${NB_USER}
