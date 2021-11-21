import aiohttp, codecs
from aiohttp import ClientSession
from codecs import decode, encode

BASE_URL = "http://api.guardiansystem.xyz/v1"


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
    pass
       

