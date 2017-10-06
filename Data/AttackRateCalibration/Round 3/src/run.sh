#!/bin/bash

#SBATCH --ntasks=34 --mem-per-cpu=2000
#SBATCH -J SimpleQueue
#SBATCH -p general
#SBATCH -t 240:00:00
#SBATCH -o SBATCH_SimpleQueue_out.txt
#SBATCH -e SBATCH_SimpleQueue_err.txt

module load NWS

SQDIR="/ysm-gpfs/project/dpd8/ZikaDengue/MC/SQ_Files_${SLURM_JOB_ID}"
mkdir "$SQDIR"
exec > "$SQDIR/PBS_script.log"
echo "$(date +'%F %T') Batch script starting in earnest (pid: $$)."
echo "$(date +'%F %T') About to execute /ysm-gpfs/apps/software/SimpleQueue/3.1/SQDedDriver.py using task file: scriptfile"

python "/ysm-gpfs/apps/software/SimpleQueue/3.1/SQDedDriver.py" \
  --logFile="$SQDIR/SQ.log" \
  --pnwss --wrapperVerbose \
  "scriptfile"
RETURNCODE=$?
echo "$(date +'%F %T') Writing exited file."
touch "$SQDIR/exited"
echo "$(date +'%F %T') Batch script exiting, $RETURNCODE."

