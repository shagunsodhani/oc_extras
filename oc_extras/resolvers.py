from omegaconf import OmegaConf

from oc_extras.utils import utils


def register_new_resolvers() -> None:
    OmegaConf.register_new_resolver("git_commit_id", utils.get_current_commit_id)
    OmegaConf.register_new_resolver(
        "git_has_uncommitted_changes", utils.has_uncommitted_changes
    )
    OmegaConf.register_new_resolver("date", utils.get_current_time)
    OmegaConf.register_new_resolver("slurm_id", utils.get_slurm_id)
    OmegaConf.register_new_resolver("generate_id", utils.generate_id)
