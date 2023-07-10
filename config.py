from globus_compute_endpoint.endpoint.utils.config import Config
from globus_compute_endpoint.executors import HighThroughputExecutor
from parsl.providers import SlurmProvider
from parsl.launchers import SrunLauncher
from parsl.addresses import address_by_interface

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
            address=address_by_interface('eth4'),  # Great Lakes eth4 armis/lh may use different values
            provider=SlurmProvider(
                partition='standard',  # update for slurm -p --partition value
                launcher=SrunLauncher(),
				account='support',  # update for slurm -A --account value
                exclusive=False,  # parsl defaults to --exclusive which is bad on ARC shared systems

                # string to prepend to #SBATCH blocks in the submit
                # script to the scheduler eg: '#SBATCH --constraint=knl,quad,cache'
                scheduler_options=user_opts['greatlakes']['scheduler_options'],

                # Command to be run before starting a worker, such as:
                # 'module load Anaconda; source activate parsl_env'.
                worker_init=user_opts['greatlakes']['worker_init'],

                # Scale between 0-1 blocks with 2 nodes per block
                nodes_per_block=1,
                mem_per_node=10,
                init_blocks=0,
                min_blocks=0,
                max_blocks=1,

                # Hold blocks for 30 minutes
                walltime='00:30:00'
            ),
        )
    ],
)

# For now, visible_to must be a list of URNs for globus auth users or groups, e.g.:
# urn:globus:auth:identity:{user_uuid}
# urn:globus:groups:id:{group_uuid}
meta = {
    "name": "gl-build-slurm",
    "description": "",
    "organization": "",
    "department": "",
    "public": False,
    "visible_to": [],
}
