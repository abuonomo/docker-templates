# Jupyter

Let's say you have a docker image that has python and some dependencies. You want to use a jupyter notebook using this docker image.  

Let's say your docker image is tagged "mypython:2.0.0". In order use jupyter for this base image, simply build an image using the Dockerfile in this folder while including a build-arg.
```
docker build -t mypython:jupyter --build-arg base_image=mypython:2.0.0 
```
Then run the container with:
```
docker run -p 8000:8888 mypython:jupyter
``` 
Note that, in the above command, the first number 8000 is the port on your local machine through which you would like to use jupyter. You may set this to whichever port you prefer. The second number 8888 refers to the port in the container.
You should see and output that looks like:
```
[I 15:56:54.919 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
[I 15:56:55.298 NotebookApp] Serving notebooks from local directory: /home
[I 15:56:55.299 NotebookApp] 0 active kernels
[I 15:56:55.299 NotebookApp] The Jupyter Notebook is running at:
[I 15:56:55.299 NotebookApp] http://0.0.0.0:8888/?token=7f38d53e58eda2ad98df684a5e6556bd03609b0cff77e4a2
[I 15:56:55.299 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 15:56:55.300 NotebookApp] 
    
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://0.0.0.0:8888/?token=7f38d53e58eda2ad98df684a5e6556bd03609b0cff77e4a2
```
Note that you can only connect to the jupyter notebook using the port mapped onto the localhost, in this case 8000.
Point your browser to localhost:8000, then use the token in the output above to connect the notebook. You should now be running jupyter commands inside of the container.

## Volumes
Note that whatever notebooks you make will be lost when the container stops running. If you want to save your notebooks you must make a volume to persist them. You could do that by mounting a local folder into the container.  
1) On your local machine (not in the container), make a folder called jupyter.
```
mkdir jupyter
```
2) Run the container mounting this folder as a volume:
```
docker run -p 8000:8888 -v $(pwd)/jupyter:/jupyter mypython:jupyter
```
Now, anything you place in the container's jupyter folder should be persitant on the host's ./jupyter folder.
