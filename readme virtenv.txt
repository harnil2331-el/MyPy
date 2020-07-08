*steps to create virtual environment
1. create folder
2. press shift + right click open windows powershell
3. type : pip install virtualenv
4. type : virtualenv env_name
5. to activate environment 
6. type: path\env_name\Script\activate
   if any error occure open powershell with admin permission
   type: path\set-executionpolicy remotesigned
   Press y then retry 
*exit from Virtual environment type: deactivate hit enter 
*for requirements.txt file
   activate virtenv 
   type: pip freeze > requirements.txt
*install requirements directly from requirements.txt file
   path\pip install -r requirement.txt
   you must be in virtenv folder and requirement.txt file must be there.  
*if you want to install all packages which is in system to virtual environment
 then 
   virtualenv --system-site-package env_name
 it will clone your system python config.

 