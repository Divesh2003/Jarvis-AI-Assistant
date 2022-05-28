from logging import config

from jarvis import settings
from jarvis.settings import ROOT_LOG_CONF
from jarvis.utils.mongoDB import db
from jarvis.utils.startup import configure_MongoDB
from jarvis.enumerations import InputMode
import jarvis.engines as engines

# ----------------------------------------------------------------------------------------------------------------------
# Create a Console & Rotating file logger
# ----------------------------------------------------------------------------------------------------------------------
config.dictConfig(ROOT_LOG_CONF)

# ----------------------------------------------------------------------------------------------------------------------
# Clear log file in each assistant fresh start
# ----------------------------------------------------------------------------------------------------------------------
with open(ROOT_LOG_CONF['handlers']['file']['filename'], 'w') as f:
    f.close()

# ----------------------------------------------------------------------------------------------------------------------
# Configuare MongoDB, load skills and settings
# ----------------------------------------------------------------------------------------------------------------------
configure_MongoDB(db, settings)

# ----------------------------------------------------------------------------------------------------------------------
# Get assistant settings
# ----------------------------------------------------------------------------------------------------------------------
input_mode = db.get_documents(collection='general_settings')[0]['input_mode']
response_in_speech = db.get_documents(collection='general_settings')[0]['response_in_speech']
assistant_name = db.get_documents(collection='general_settings')[0]['assistant_name']

# ----------------------------------------------------------------------------------------------------------------------
# Create assistant input and output engine instances
# ----------------------------------------------------------------------------------------------------------------------
input_engine = engines.STTEngine() if input_mode == InputMode.VOICE.value else engines.TTTEngine()
output_engine = engines.TTSEngine() if response_in_speech else engines.TTTEngine()
