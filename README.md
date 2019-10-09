# Wdang

Wdang is a Wifi.id Automation Login using Python and selenium library.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all requirements.

```bash
pip install -r requirements
```

## Usage

```python
import wifiidscript

auto = wifiidscript.wdang()

if auto.checkPing() == 0:
    print("Network Active")
else:
    auto.login()
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
