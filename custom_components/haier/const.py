from homeassistant.const import Platform

DOMAIN = 'haier'

SUPPORTED_PLATFORMS = [
    Platform.SELECT,
    Platform.NUMBER,
    Platform.SENSOR,
    Platform.BINARY_SENSOR,
    Platform.SWITCH,
    Platform.CLIMATE
]

FILTER_TYPE_INCLUDE = 'include'
FILTER_TYPE_EXCLUDE = 'exclude'
