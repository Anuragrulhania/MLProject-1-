import sys
import  logging
## we will try to create our own custom error message
def error_message_detail(error,error_detail:sys): ## error details are present in sys
   
    ## sys will provide us 3 output but we are intersted in the last one
   
    _,_,exc_tb=error_detail.exc_info()   ## execution info will give us three info but we are intersted in the last one
     ## exc_info will give us the info that on which the error line ,in which file the exception has occured
    
    # returning the filename
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error Occured in python script name[{0}] line number [{1}] error message [{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

## Creating a custom class to call the error_message_detail    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
       # use super as we have to inherit from the init function i.e. inheriting the error message
        super().__init__(error_message)
        #Calling the error message detail
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
  