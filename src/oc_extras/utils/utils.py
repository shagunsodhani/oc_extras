import datetime
import hashlib
import os
import subprocess  # noqa: S404


def generate_id(description: str, git_issue_id: str, seed: int) -> str:
    return f"{hashlib.sha224(description.encode()).hexdigest()}_issue_{git_issue_id}_seed_{seed}"


def get_current_commit_id() -> str:
    """Get current commit id.

    Returns:
        str: current commit id.
    """
    command = "git rev-parse HEAD"
    commit_id = (
        subprocess.check_output(command.split()).strip().decode("utf-8")  # noqa: S603
    )
    return commit_id


def has_uncommitted_changes() -> bool:
    """Check if there are uncommited changes.

    Returns:
        bool: wether there are uncommiteed changes.
    """
    command = "git status --porcelain"
    output = subprocess.check_output(command.split()).strip().decode("utf-8")
    return len(output) > 0


def get_current_time() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_slurm_id() -> str:
    slurm_id = []
    env_var_names = ["SLURM_JOB_ID", "SLURM_STEP_ID"]
    for var_name in env_var_names:
        if var_name in os.environ:
            slurm_id.append(str(os.environ[var_name]))
    if slurm_id:
        return "-".join(slurm_id)
    return "-1"
