import aiohttp, codecs
from aiohttp import ClientSession
from codecs import decode, encode

BASE_URL = "http://api.guardiansystem.xyz/v1"

# CHORE: Add request builder and Exception handler

class GuardClient:
    """
    PyGuard
    -
    A Python wrapper for Discord Guardian System API
    """
    def __init__(self):
        self.credentials = None

    def login(self, API_Token: str, id: str):
        """
        login to the API using your credentials. 
    
        You can apply for credentials at https://guardiansystem.xyz. \n
        For security, It is recommended that login information is stored
        in a `.env` file.

        ~@`paramaters`:
            `token`: str (required) Your accesss token granted from application 
            `id`: str (required) Your Application's Discord ID as string.
 
        ```
        GuardClient.login(
            id=os.getenv("CLIENT_ID")
            API_Token=os.getenv("API_TOKEN")
        )
        ```
        """

        strencode = encode(bytes(id + ":" + API_Token, "utf-8"), 'base64')
        self.credentials = decode(strencode, "utf-8")

        
    def credentials(self): 
        """
        fetches the API_token & Client Id input in `.login()`
        """
        return self.credentials


class Request:
    def __init__(self):
        self.route = None
        self.headers = None
        self.method = None
        self.credentials = GuardClient.credentials()

    def setRoute(self, route: str):
        """
        Sets the route for the request. Must be an accepted Endpoint. 

        ~@`Routes`:
            - `/offenders`: Fetches users in the database \n
                    Methods: `GET`
            - `/servers`: Fetches offending servers \n
                    Methods: `GET`
            - `/links`: Fetches a know scamlink by URL \n
                    Methods: `GET`
            - `/reports`: Submits or Fetches a report & its status \n
                    Methods: `GET`, `POST`
            - `/requests`: Submit or Fetch a request for your Data \n
                    Methods: `GET`, `POST`
        """
        if route.startswith("/"):
            
            if self.method == "GET":
                self.route = BASE_URL + route
            
            elif self.method == 'POST':
                self.route = route
            
            else: return
        
        else:
            
            if self.method == 'GET':
                self.route = BASE_URL + "/" + route
            
            elif self.method == "POST":
                self.route = "/" + route
            
            else: return
        
    def setMethod(self, method: str):
        """
        Sets the method for the request. Methods must only be that of `GET` or `POST`.
        See `.setRoute()` for accepted request methods per route.
        """
        accepted = ["GET", "POST"]
        if not method.upper() in accepted:
            print("PYGUARD ERROR: Invalid method type: {} \nAccepted Methods: \n\"POST\" \n\"GET\"".format(method))
            return
        else:
            self.method = method.upper()

    def setHeaders(self):
        """
        Sets the header for the response. Providing the credentials from `.login()` for authentication.
        """
        self.headers = {
            "Method": self.method,
            "Host": BASE_URL,
            "Path": self.route,
            "Protocol": "HTTP/1.1",
            "Content-type": "Application/JSON",
            "Authorization": "Basic " + self.credentials 
        }
