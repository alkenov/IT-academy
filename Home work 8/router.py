#!python3
#-*-encoding:utf8-*-


class Router:

    paths = dict()

    def add_path(self, method, path, func):
        self.paths[func] = [path, method]

    def get_list_of_paths(self):
        path_list = []
        for i in self.paths.values():
            path_list.append(i[0])
        return path_list

    def request(self, method, path):
        if path not in self.get_list_of_paths():
            return 404, 'Error 404: Not Found'

        for func, values in self.paths.items():
            if path in values:
                if method in values:
                    return func(), 200, 'OK'
                else:
                    return 405, 'Error 405: Method Not Allowed'

    def __get__(self, path):
        return self._return_func_from_method(path, "GET")

    def post(self, path):
        return self._return_func_from_method(path, "POST")

    def put(self, path):
        return self._return_func_from_method(path, "PUT")

    def patch(self, path):
        return self._return_func_from_method(path, "PATCH")

    def __delete__(self, path):
        return self._return_func_from_method(path, "DELETE")

    def options(self, path):
        return self._return_func_from_method(path, "OPTIONS")

    def _return_func_from_method(self, path, method):
        if path not in self.get_list_of_paths():
            return 404, 'Error 404: Not Found'

        for func, values in self.paths.items():
            if path in values:
                if method in values:
                    return func(), 200, 'OK'
                else:
                    return 405, 'Error 405: Method Not Allowed'


def my_func():
    return 'hello'


def update():
    return 'test'


if __name__ == '__main__':
    router = Router()
    router.add_path('GET', '/cart', my_func)
    router.add_path('PUT', '/me', update)
    print(router.put('/cart'))
    print(router.request('PUT', '/me'))
