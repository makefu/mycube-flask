#! /bin/sh
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, Response

import redis
redis = redis.StrictRedis(host='localhost', port=6379, db=0)

app = Flask(__name__)
app.debug = True


def ip_delete_store(remoteip):
    app.logger.debug("delete {}".format(remoteip))
    return redis.delete(remoteip)
def ip_get_store(remoteip):
    app.logger.debug("getting {}".format(remoteip))
    return redis.get(remoteip)

def ip_set_store(remoteip,localip):
    app.logger.debug("setting {} to {}".format(remoteip,localip))
    return redis.set(remoteip,localip)

@app.route('/',methods=["GET"])
def get_ip():
    remoteip = request.access_route[0]
    localip  = ip_get_store(remoteip)
    if localip:
        return redirect("http://{}/".format(localip), 301)
    else:
        return Response("No IP Stored for you")

@app.route('/',methods=["POST"])
def set_ip():
    remoteip = request.access_route[0]
    localip = request.get_data()
    return Response(str(ip_set_store(remoteip,localip)))

@app.route('/',methods=["DELETE"])
def delete_ip():
    remoteip = request.access_route[0]
    return Response(str(ip_delete_store(remoteip)))


if __name__ == '__main__':
        app.run(port=8001)
