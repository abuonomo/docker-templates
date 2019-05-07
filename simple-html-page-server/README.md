# Simple Site with Docker
How to host a simple html webpage in a minimal docker container.

## Use

1. Change the `html/index.html` file to your liking. 
2. Build the docker image with `docker build -t my_simple_site:example .`.
3. Serve your site with `docker run -p 81:80 my_simple_site:example`\*.
4. Point your browser to localhost:81 to see your content. 

\* In `-p 81:80`, port 81 could be changed to whatever port you prefer. This is the port by which you will access the content from the outside.In this argument, however, port 80 must remain unchanged. It represents the containers internal port. For the docker image built this way, it will always be 80.   
  
You want to run this site as a daemon (background process) with `docker run -d -p 81:80 my_simple_site:example`.  
Look at [docker run](https://docs.docker.com/engine/reference/commandline/run/) documentation for more details.   
