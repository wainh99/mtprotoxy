# Async Relay #

Fast and simple to setup relay service written in Python.

## Starting Up ##
    
1. `git clone https://github.com/wainh99/mtprotoxy.git; cd mtprotoxy`
2. *(optional, recommended)* edit *config.py*, set **PORT**, **USERS** and **AD_TAG**
3. `docker-compose up -d` (or just `python3 mtprotoproxy.py` if you don't like Docker)
4. *(optional, get a link to share the service)* `docker-compose logs`

## Channel Promotion ##

To promote a channel, get a tag from the bot and put it to *config.py*.

## Performance ##

The service performance should be enough to comfortably serve about 4 000 simultaneous users on
the VDS instance with 1 CPU core and 1024MB RAM.

## Advanced Usage ##

The service can be launched:
- with a custom config: `python3 mtprotoproxy.py [configfile]`
- several times, clients will be automaticaly balanced between instances
- with uvloop module to get an extra speed boost
- with runtime statistics exported to [Prometheus](https://prometheus.io/)
