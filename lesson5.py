
#MODULES - a python file with fxns and classes that can be used somewhere else
#PACKAGE - published collection of modules. modules created by someone and made available online. #pyhton package index.
#we install a package by using the syntax 'pip install (name of package)' bracket n ' not necessary.
#python will install package globally but we need it installed locally. therefore, we create a virtual env. for local install
#virtual environment is a folder that has all the codes u will need to run the application/package u are using
#python -m venv (folder name) : code for creatn/setting up our virtual env.(type it in the run section)
#now we activate the venv. before we can use. activate it by using the syntx: .\foldername\Scripts\activate.ps1
#or (watch video) for manually install
#now we install colorama(a module) by first creatin a requirement text file. use (pip freeze > requirement.txt) to create it or go manually by selectn new file n name it req.txt
#now we run the code 'pip install -r (path of the newly created req text file).
#pip list - reveals the packages/modules installed in your venv. to install a package, use code: pip install (name of package). this is another way

from helpers import display      #this imports display fxn from the helpers file.(u can use import display. then the next kine will be helpers.display)
display('sample message'is_warning=true)

display('sample message')

