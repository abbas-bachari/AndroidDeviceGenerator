from __future__ import annotations
from .devices import *


class DviceData:
    user_agent="Mozilla/5.0 (Linux; Android 13; Samsung SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.54 Mobile Safari/537.36"
    device_model = "Samsung SM-G998B"
    sdk_version= "SDK 33"
    android_version = "13"
    chrome_version="129.0.6668.54"
    webkit_version="537.36"
    safari_version="537.36"
    def __init__(self,device_data:dict) -> None:
        if device_data and isinstance(device_data,dict):
            self.__dict__.update(device_data)
    
    def to_dict(self):
            return dict(
                 user_agent=self.user_agent,
                device_model=self.device_model,
                sdk_version=self.sdk_version,
                android_version=self.android_version,
                chrome_version=self.chrome_version,
                webkit_version=self.webkit_version,
                safari_version=self.safari_version
                
                )
        
    def __str__(self) -> str:
            
        return json.dumps(self.to_dict(),indent=4)

class Generator:

        def __init__(self,chrome_version:str="129.0.6668.54",webkit_version:str="537.36",safari_version:str="537.36") -> None:
            
            self.chrome_version=chrome_version
            self.webkit_version=webkit_version
            self.safari_version=safari_version

        
       
        def Generate(self ,unique_id: str = None,webview:bool=False) :
            """
            Generate random device model and system version

            ### Arguments:
            
                unique_id (`str`, default=`None`):
                    The unique ID to generate - can be anything.\\
                    This will be used to ensure that it will generate the same data everytime.\\
                    If not set then the data will be randomized each time we runs it.
            
            """
            
            device = Device.RandomDevice(unique_id)
            self.device_model=device.device_model
            self.sdk_version=device.sdk_version
            self.android_version=device.android_version
            
            wv="; wv" if webview else ""
            self.user_agent=f"Mozilla/5.0 (Linux; Android {device.android_version}; {device.device_model}{wv}) AppleWebKit/{self.webkit_version} (KHTML, like Gecko) Chrome/{self.chrome_version} Mobile Safari/{self.safari_version}"
            
            
            data=dict(
                user_agent=self.user_agent,
                device_model=self.device_model,
                sdk_version=self.sdk_version,
                android_version=self.android_version,
                chrome_version=self.chrome_version,
                webkit_version=self.webkit_version,
                safari_version=self.safari_version
                
                )
            
            return DviceData(data)
        
        