# credential_stuffing_bot
a simulation of how a bot uses credential stuffing 

# How it works
+ you first have to run the flask app `python run.py`
+ then you have to run the run_controllers file `python run_controllers.py`
+ a db file will automatically be created because the `KeyboardController` class uses the `get_login` func as a class var
+ the `run_keyboard_controller` will return a `-1` signifying that all comprimised logins have been tried 
+ this will close the thread
