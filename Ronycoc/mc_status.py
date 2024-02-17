from botpy.message import Message
from botpy import BotAPI

from Ronycoc.utils.extract_host import extract_host
from Ronycoc.utils.get_mc_status import status

from socket import gaierror

from mcstatus.status_response import BedrockStatusResponse, JavaStatusResponse

class McStatus:
    def __init__(self, message: Message):
        self.host = extract_host(message.content)
        
    async def mc_satus_message(self) -> str:
        response = await status(self.host)
        if isinstance(response, JavaStatusResponse):
            status_message = (f"version: {response.version.name} \n" 
            f"protocol version: {response.version.protocol} \n" 
            f"players: {response.players.online} / {response.players.max} \n"
            f"ping: {round(response.latency, 2)} ms\n"
            f"description: {response.description}")
        elif isinstance(response, BedrockStatusResponse):
            status_message = (f"version: {response.version.name} \n" 
            f"protocol version: {response.version.protocol} \n" 
            f"players: {response.players.online} / {response.players.max} \n"  
            f"map_name: {response.map_name}\n" 
            f"ping: {round(response.latency, 2)} ms\n" 
            f"description: {response.description}")
        return status_message


        

        
