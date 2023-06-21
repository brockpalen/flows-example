# Example Globus Flow

This flow example has two main components, 

 1. [Globus Flow](https://docs.globus.org/api/flows/) 
 1. [Globus Compute aka funcx](https://funcx.org/)

https://funcx.readthedocs.io/en/latest/quickstart.html


# Setup virtual env As of 6/2023

```
ssh gl-login1.arc-ts.umich.edu

module load python/3.10.4

virtualenv

source bin/activate
python3 -m pip install globus-compute-endpoint
python3 -m pip install globus-automate-client
```

# Startup funcx endpoint on gl-login1

Need to start this on same host always.
An endpoint per slurm configuration is required. 

```
globus-compute-endpoint configure gl-login1-standard

globus-compute-endpoint list


# copy in example parsl config to use slurm 
# this can be skipped and test will run on the login node to veryify

cp config.py ~/.globus_compute/gl-login1-standard/config.py

# edit config.py and update account, slurm settings
# example defaults to using a whole 36 core 180gb node

globus-compute-endpoint start gl-login1-standard 
globus-compute-endpoint list

#should list running
```


# Register function with funcx

```
# save UUID 
python3 reg_func.py
```

# globus automate/flow

## deploy flow

```
# save UUID 
globus-automate flow deploy --title "ARC Example Flow" \
    --definition flow-def.json --input-schema input-schema.json 
```

## run flow

Edit `input.json` for your own path and server.  Default values are for the
web UI only and must be provided when calling on the CLI.  The example
`input.json` has all the required variables. 

```
globus-automate flow run <uuid>  --flow-input
input.json  --label test-cli1
```
