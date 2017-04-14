<img src="https://github.com/NomiProject/LampREST-Server/blob/master/static/img/lamp_on.png?raw=true" width="48">

# LampREST-Server
A RESTful web-server built-in a Raspberry Pi 3 model B to control the activation of a AC lamp through a TCP/IP network connection and HTTP protocol.

### Requirements

1. **Python 2.7 or 3.6** 
    Download Python interpreter [here](https://www.python.org/).

2. **Raspberry Pi 3 Model B** 
    Learn more about [RasberryPi project](https://www.raspberrypi.org/).

### Setup in your RaspberryPi

1. Clone the repo

    ```bash
	$ git clone https://github.com/NomiProject/LampREST-Server.git
	$ cd LampREST-Server/
	```

2. Create Python Virtual Environment

    ```
	$ virtualenv env --system-site-packages
	```
	
	The `–system-site-packages` flag is optional, but by adding it, it allows you isolated environment to access your globally installed packages on your root install, so thing’s like the RPi.GPIO library and such so I find it’s a good idea to add it.

3. Enable Python Virtual Environment 

    ```bash
    $ source env/bin/activate
    ```

4. Install the pip-installable dependencies

    ```bash
	$ pip install -r requirements.txt
    ```

5. Run the **LampREST-Server**

    ```bash
	$ python app.py
    ```

6. Locally, navigate to [http://localhost:5000](http://localhost:5000) or remotely [http://your_raspberrypi_ipaddress:5000](http://your_raspberrypi_ipaddress:5000) to access the webservice and control a lamp.

---

Developed by [Allex Lima](http://allexlima.com), [Daniel Bispo](https://github.com/danielbispov/), [Paulo Moraes](http://www.moraespaulo.com/) and [Renan Barroncas](https://github.com/renanbarroncas) with ❤️ using [Python](https://www.python.org/). 
###### Copyright © 2016 [LampREST-Server](https://github.com/NomiProject/LampREST-Server.git) - Licensed by MIT LICENSE.