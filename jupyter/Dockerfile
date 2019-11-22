ARG base_image=python
FROM $base_image

RUN pip install jupyter

RUN mkdir jupyter
WORKDIR /jupyter

CMD jupyter notebook --ip 0.0.0.0 --no-browser --allow-root 
