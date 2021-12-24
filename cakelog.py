import os
import pathlib
import json
import time


#look at the config file, and get all of its values

def look_at_config():

    if(os.path.isfile("cakeconf.json")):
        log_conf = open("cakeconf.json", "r")
        conf_values = log_conf.read()
        log_conf.close()

        conf_values = json.loads(conf_values)["logger"]
        return conf_values

the_logger_paths = look_at_config()


# get the path of the logger, by the name in the config

def get_logger(name):
    if(os.path.isfile("cakeconf.json")):
        log_conf = open("cakeconf.json", "r")
        conf_values = log_conf.read()
        log_conf.close()

        conf_values_json_read = json.loads(conf_values)["logger"]
        print(conf_values_json_read[0])
        print(len(str(conf_values_json_read).split(str('"' + str(name) + '":'))))
        if(len(str(conf_values_json_read).split(str("'" + str(name) + "':"))) > 1):
            pass
        else:
            return None

        conf_values_final = (conf_values_json_read[0])[str(name)]

        print("RESUBMIT")
        return conf_values_final

    
# create the log-file if it is not there

def create_logger(name):
    the_log_path = get_logger(name)
    if(os.path.isfile(the_log_path) == False):
        log_create = open(the_log_path, "w")
        log_create.close()
        return True
    else:
        return False


#log (write) the message in the log-file

def log(the_logger, msg):

    logger = get_logger(the_logger)

    if(logger != None):
        if(os.path.isfile((logger)) and len(str(logger)) > 0):

            the_year_time = [time.localtime().tm_mday, time.localtime().tm_mon, time.localtime().tm_year]
            the_day_time = [time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec]

            logfile = open(logger, "r")
            log_contents = logfile.read()
            print(log_contents)
            logfile.close()

            logfile = open(logger, "w+")
            logfile.write(str(log_contents) + "\n" + "[" + "(" + str(the_year_time[0]) + "." + str(the_year_time[1]) + ") " + str(the_day_time[0]) + ":" + str(the_day_time[1]) + ":" + str(the_day_time[2]) + "]-> " + str(msg))
            logfile.close()
            return True
        else:
            return False
    else:
        return False
