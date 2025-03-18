import time
from abc import ABC, abstractmethod
from os import times
#
#
# class Page(ABC): # Abstract class
#     @abstractmethod
#     def render_page(self):
#         pass
#
#
# class UserPage(Page): # Concrete Class
#     def render_page(self):
#         print("Welcome to the Application")
#
#
# class UserVIPPage(Page): # Concrete Class
#     def render_page(self):
#         print("Welcome to the Application")
#         print("50% off TODAY")
#
#
# class AuthDecorator(Page): # abstract class
#     def __init__(self, component):
#         self._component = component
#
#     def render_page(self):
#         pass
#
# class UserVIPDecorator(AuthDecorator): # concrete class
#     def render_page(self):
#         username = input("Enter your username: ")
#         password = input("Enter your password: ")
#         if username == "admin" and password == "1111":
#             self._component.render_page()
#         else:
#             print("Sorry you are not Authenticated!!")
#
# def client():
#     user_type = input("Enter if Vip or Normal: ")
#     if user_type == "Vip":
#         vip_page = UserVIPPage()
#         result = UserVIPDecorator(vip_page)
#         result.render_page()
#     else:
#         UserPage().render_page()
#
# client()
#
#
#



class AbstractServer(ABC):
    @abstractmethod
    def recieve(self):
        pass


class Server(AbstractServer):
    def recieve(self):
        print("Processing Your request")
        time.sleep(2)
        print("Your response is ready")


class Proxy(AbstractServer):
    def __init__(self, server):
        self._server = server

    def recieve(self):
        print("Changed to standard format!")
        time.sleep(2)
        self._server.recieve()

def client():
    server = Server()
    proxy = Proxy(server)
    proxy.recieve()


client()