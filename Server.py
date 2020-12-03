from flask import Flask
from flask import request
from flask import abort


class Server:
    def __init__(self, address: str, port: int):
        self._address = address
        self._port = port

        self._funcs = dict()
        self._methods = dict()

        self._app = Flask("Server")

    def add_route(self, route, func, method):
        self._app.add_url_rule(route, view_func=func, methods=[method])

    def start_server(self):
        """
        Start the server on new thread
        :return:
        """
        self._app.run(self._address, self._port)

    def _route(self, path):
        """
        Handle the routing in the server
        :param path: the path from the request
        :return: function return
        """
        try:
            if self._methods[path] != request.method:
                abort(405)
            return self._funcs[path](request.json)
        except KeyError:
            abort(404)
