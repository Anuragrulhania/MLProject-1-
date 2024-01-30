# logger is the purpose for if any execution happens we should we able log all those information, execution into
## into some file so that if any some errors or custom exception errors we will be able to  track or log into some text 
## file this is the reason to implement logger

import logging
import os
from datetime import datetime

## Creating our LOG_FILE with the name convention
LOG_FILE =f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)   ##"logs" are created w.r.t. cwd  and every file will be 
## created with logs along with whatever filename is coming


## keep on appending the file
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

## how you wanna save it

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)




### whenever we got an exception then i will take the exception then
#  log with the logging file and use log .logging.INfo to put inside the logging file