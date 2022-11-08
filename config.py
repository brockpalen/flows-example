from parsl.addresses import address_by_hostname
from parsl.launchers import SrunLauncher
from parsl.providers import SlurmProvider

from funcx_endpoint.endpoint.utils.config import Config
from funcx_endpoint.executors import HighThroughputExecutor

#config = Config(
#    executors=[
#        HighThroughputExecutor(
#            provider=LocalProvider(
#                init_blocks=1,
#                min_blocks=0,
#                max_blocks=1,
#            ),
#        )
#    ],
#    funcx_service_address="https://api2.funcx.org/v2",
#)

user_opts = {
    'greatlakes': {
        'worker_init': 'module load python',
        'scheduler_options': '',
    }
}

config = Config(
    executors=[
        HighThroughputExecutor(
            worker_port_range = (8888,8987),
            interchange_port_range = (8888,8987),
            max_workers_per_node=2,
            worker_debug=True,
            address=address_by_hostname(),
            provider=SlurmProvider(
                partition='standard',
                launcher=SrunLauncher(),
				account='support',

                # string to prepend to #SBATCH blocks in the submit
                # script to the scheduler eg: '#SBATCH --constraint=knl,quad,cache'
                scheduler_options=user_opts['greatlakes']['scheduler_options'],

                # Command to be run before starting a worker, such as:
                # 'module load Anaconda; source activate parsl_env'.
                worker_init=user_opts['greatlakes']['worker_init'],

                # Scale between 0-1 blocks with 2 nodes per block
                nodes_per_block=1,
                mem_per_node=180,
                init_blocks=0,
                min_blocks=0,
                max_blocks=1,

                # Hold blocks for 30 minutes
                walltime='00:30:00'
            ),
        )
    ],
    funcx_service_address="https://api2.funcx.org/v2",
)

# For now, visible_to must be a list of URNs for globus auth users or groups, e.g.:
# urn:globus:auth:identity:{user_uuid}
# urn:globus:groups:id:{group_uuid}
meta = {
    "name": "gl-login1",
    "description": "",
    "organization": "",
    "department": "",
    "public": False,
    "visible_to": [],
}
