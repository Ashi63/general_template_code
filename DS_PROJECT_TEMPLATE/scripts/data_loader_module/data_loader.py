import sys 
from pathlib import Path
print(sys.path[-1])
print()
print(Path())
print(Path().resolve())
print(Path().resolve().parent)

sys.path.append(Path().resolve().parent)
print('path appended successfully')
#print(Path().resolve().parent.parent)



'''

['C:\\Users\\Alkashi\\Desktop\\ML_Project\\Automation_python\\DS_PROJECT_TEMPLATE\\scripts\\data_loader_module', 
'C:\\ProgramData\\Anaconda3\\python39.zip',
'C:\\ProgramData\\Anaconda3\\DLLs', 
'C:\\ProgramData\\Anaconda3\\lib', 
'C:\\ProgramData\\Anaconda3', 
'C:\\Users\\Alkashi\\Desktop\\ML_Project\\Automation_python\\.venv',
'C:\\Users\\Alkashi\\Desktop\\ML_Project\\Automation_python\\.venv\\lib\\site-packages']
'''
from scripts.logging_module import logger


exception_handler = logger.ExceptionHandler()
log_logger = logger.ProjectLogger()


log_logger._create_logger()
print('logger created successfully.')
