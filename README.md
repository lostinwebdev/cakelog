# cakelog
a lightweight logging library for python applications


This is a very small logging library to make logging in python easy and simple.


## config

open the file:

     cakeconf.json

the file has the attribute:

    logger: [
        {
            ...
        }
    ]

in this attribute you can add different logger-types
the syntax of a logger is:

    "<name>": "<path>"

It is possible to add infinite loggers into the "logger"-section
"path"-value works with all types of text-like-files (.txt, .log, ...)

Example of cakeconf.json:

    logger: [
        {
            "common": "examplefolder/examplelog.txt",
            "second": "anotherfolder/2_examplelog.txt",
            "random": "randomfolder/log_rand.txt",
        }
    ]

## functions

    look_at_config()

- show the raw "logger"-section of the config file 
<hr />

    create_logger(<name>)

- instantiate a logger by the "name"-value set in the "logger"-section of the cakeconf.json
- "name"-value has to be set before calling this function
<hr />

    get_logger(<name>)

- gives the "path"-value for a logger by the "name"-value set in the "logger"-section of the cakeconf.json
- both values need to be set in the cakeconf.json file
<hr />

    log(<name>, <msg>)

- logs the "msg"-value in the specified logger
- "name"-value needs to be set in the "logger"-section of the cakeconf.json
