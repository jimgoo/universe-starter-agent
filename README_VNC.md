Trying the new OpenAI Universe and needed a lot of Mac VNC connectors to check on my games. This is "Screen Sharing" app that ships with Mac and connects to VNC.

```
python make-xmls.py --help
    usage: make-xmls.py [-h] [-ip IP] [-pr PORT_RANGE]

    optional arguments:
      -h, --help            show this help message and exit
      -ip IP, --ip IP       IP address of the VNC server [127.0.0.1]
      -pr PORT_RANGE, --port-range PORT_RANGE
                            range of ports you want to make connectors for
                            [5900:5903]
                            port range [5900:5903]
```

So if you have 4 workers on your local machine and wanted to generate one connector per port from 5900 to 5904:

```bash
python make-xmls.py -ip '127.0.0.1' -pr '5900:5904'
```
