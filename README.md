[![AndroidDeviceGenerator](https://img.shields.io/badge/AndroidDeviceGenerator%20-Version%201.0.0-green?style=plastic&logo=codemagic)](https://python.org)




# Android Device Generator





## Installation guide

Install from source:
``` bash
pip install git+https://github.com/abbas-bachari/AndroidDeviceGenerator.git
```



<!-- ## user manual -->

##  Generate a device

```python
from AndroidDeviceGenerator import Generator

generator=Generator(chrome_version = "129.0.6668.54", webkit_version = "537.36", safari_version= "537.36")

device=generator.Generate()

print(device)


# >>> {
#       "device_model": "HTC HTC 2Q4R400",
#       "sdk_version": "SDK 28",
#       "android_version": "9",
#       "user_agent": "Mozilla/5.0 (Linux; Android 9; HTC HTC 2Q4R400) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.54 Mobile Safari/537.36"
#     }

```

Powered by [Abbas Bachari](https://github.com/abbas-bachari).
