# Welcome to Herbify Deploy Model Repository!
This is our simple REST API running on Flask.

## Prerequisite
Before you can running this `server.py` you  need to provide the following:
 - Virtual Machine on GCP (make sure open the port 8080, and have correct permission for Cloud Storage)
 - Git, for cloning the repository
 - pip, for installing python module
 - ML Model that already trained

## Let's Rock!
Run the command below step by step to make sure you're on the right track.
1. Update your system package manager (in this case we're using `apt`) and then installed important programs.
> sudo apt update && sudo apt install -y git python3-pip screen
2. Update pip so we can install the newest tensorflow
> pip3 install pip --upgrade
3. Clone this repo
> git clone [https://github.com/herblabsai/herbify-deploy-model.git](https://github.com/herblabsai/herbify-deploy-model.git)
4. Change dir to herbify-deploy-model and then install important modules
> cd herbify-deploy-model  
pip3 install -r requirements.txt

*in case you're getting error like **MemoryError*** when installing tensorflow, please use the following command instead 
> pip3 install --no-cache-dir -r requirements.txt
5. Download our ML model [here](https://storage.googleapis.com/herbify/model/model_xception_herbify.h5), and save them in herbify-deploy-model directory
6. Run the command via screen command, so you can leave the terminal safely
> screen -S herbify python3 server.py

## Known issue(s)
 1. When running the `server.py` you got this error, (*Error :  
ImportError: libGL.so.1: cannot open shared object file: No such file or directory*). 
Please install the following library from your system package manager 
> sudo apt install ffmpeg libsm6 libxext6 -y

## How to test?
1. If you have Postman installed, take a look at the screenshot below. You only need to change the `your-url-here` with your public IP address or domain.
![Postman POST example](https://storage.googleapis.com/herbify/repo-images/herbify-deploy-model/postman_post.png)
2. If you don't have Postman installed, use the `test.py` file instead.

## Reference
1. [tensorflow-image-classification-flask-deployment](https://github.com/faizan170/tensorflow-image-classification-flask-deployment) by [faizan170](https://github.com/faizan170).
