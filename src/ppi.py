import click
from itertools import compress
from utils import for_each
from terminal import sh, touch, cd, mv, curl, mkdir


# region Standard prints

def log_start(
        category: str,
        msg: str) -> None:
    click.echo(f"[{category.upper()}] > {msg}...")


def log_end() -> None:
    click.echo()

# endregion


# region Default initializers

def standard_init(
        name: str,
        desc: str,
        dry_run: bool) -> None:
    """Standard project initialization"""
    def make_poetry(msg: str):
        log_start(category, msg)
        if not dry_run:
            sh(command=["poetry", "new", name])
            cd(name)
        log_end()

    def make_readme(msg: str):
        log_start(category, msg)
        if not dry_run:
            mv("README.rst", "README.md")
            with open("README.md", "w") as readme:
                readme.write(f"# {name}\n")
                readme.write(f"{desc}  \n")
        log_end()

    def make_gitignore(msg: str):
        log_start(category, msg)
        if not dry_run:
            url = "https://www.toptal.com/developers/gitignore/api/visualstudiocode,python,pycharm,jupyternotebooks,pycharm+all,pycharm+iml"
            curl(url=url, path=".gitignore")
            # gitignore_cmd = ["curl", "-fsSL", url, "-o", ".gitignore"]
            # sh(command=gitignore_cmd, dry_run=dry_run)
        log_end()

    def make_license(msg: str):
        log_start(category, msg)
        if not dry_run:
            url = "https://raw.githubusercontent.com/gabrielecorni/python-project-initializer/master/LICENSE"
            curl(url=url, path="LICENSE")
            # license_cmd = ["curl", "-fsSL", url, "-o", "LICENSE"]
            # sh(command=license_cmd, dry_run=dry_run)
        log_end()

    # ---

    category = "Creation"
    make_poetry(f"Creating {name}")
    make_readme("Setting README")
    make_gitignore("Getting .gitignore")
    make_license("Getting LICENSE")


def closure() -> None:
    """Closure"""

    def make_closure(msg: str):
        log_start(category, msg)
        sh(command=["tree", "-R", "."])
        log_end()

    # ---

    category = "Creation"
    make_closure("Completing setup")

# endregion


# region Docker

def docker_init(
        name: str,
        dry_run: bool) -> None:
    """Docker init"""
    def make_docker(msg: str):
        log_start(category, msg)
        if not dry_run:
            touch("docker/Dockerfile", makedirs=True)
        log_end()

    def make_scripts(msg: str):
        log_start(category, msg)
        if not dry_run:
            curl(
                url="https://raw.githubusercontent.com/gabrielecorni/python-project-initializer/master/data/scripts/.gitignore",
                path="scripts/.gitignore",
                makedirs=True)
            curl(
                url="https://raw.githubusercontent.com/gabrielecorni/python-project-initializer/master/data/scripts/_conf.sh",
                path="scripts/_conf.sh",
                makedirs=True)
            curl(
                url="https://raw.githubusercontent.com/gabrielecorni/python-project-initializer/master/data/scripts/docker-build.sh",
                path="scripts/docker-build.sh",
                makedirs=True)
            curl(
                url="https://raw.githubusercontent.com/gabrielecorni/python-project-initializer/master/data/scripts/docker-clean.sh",
                path="scripts/docker-clean.sh",
                makedirs=True)
            curl(
                url="https://raw.githubusercontent.com/gabrielecorni/python-project-initializer/master/data/scripts/docker-push.sh",
                path="scripts/docker-push.sh",
                makedirs=True)
            curl(
                url="https://raw.githubusercontent.com/gabrielecorni/python-project-initializer/master/data/scripts/docker-run.sh",
                path="scripts/docker-run.sh",
                makedirs=True)
        log_end()

    # ---

    category = "Docker"
    make_docker(f"Creating Dockerfile for {name}")
    make_scripts("Copying utility scripts")

# endregion


# region Jenkins

def jenkins_init(
        name: str,
        dry_run: bool) -> None:
    """Jenkins init"""
    def make_jenkins(msg: str):
        log_start(category, msg)
        if not dry_run:
            touch("jenkins/Jenkinsfile", makedirs=True)
        log_end()

    # ---

    category = "Jenkins"
    make_jenkins(f"Creating Jenkinsfile for {name}")

# endregion


# region Helm

def helm_init(
        name: str,
        dry_run: bool) -> None:
    """Helm init"""
    def make_helm(msg: str):
        log_start(category, msg)
        if not dry_run:
            mkdir("scripts/deployments")
            sh(command=["helm", "create", f"scripts/deployments/{name}"])
        log_end()

    # ---

    category = "Helm"
    make_helm(f"Generating {name}'s helm chart template")

# endregion


# region Git

def git_init(
        name: str,
        dry_run: bool) -> None:
    """Git init"""
    def make_git(msg: str):
        log_start(category, msg)
        if not dry_run:
            sh(command=["git", "init"])
        log_end()

    # ---

    category = "Git"
    make_git(f"Putting {name} repository under version control")

# endregion


# region Package

def package_init(
        name: str,
        dry_run: bool) -> None:
    """Package init"""
    def make_package(msg: str):
        log_start(category, msg)
        if not dry_run:
            curl(
                url="https://raw.githubusercontent.com/gabrielecorni/python-project-initializer/master/data/src/setup.py",
                path="setup.py"
            )
        log_end()

    # ---

    category = "Package"
    make_package(f"Setting {name} build files")

# endregion


@click.command()
@click.argument('project_name')
@click.option('-d', '--description', help='Project description.', prompt='Insert project description', default='')
@click.option('--dry-run',  is_flag=True, default=False, help='Trigger a dry run execution.')
@click.option('--docker',   is_flag=True, default=False, help='Set to create a Dockerfile.')
@click.option('--jenkins',  is_flag=True, default=False, help='Set to create a Jenkinsfile.')
@click.option('--git',      is_flag=True, default=False, help='Set to initialize a new Git repository.')
@click.option('--helm',     is_flag=True, default=False, help='Set to create a Helm chart.')
@click.option('--package',  is_flag=True, default=False, help='Set to create a Jenkinsfile.')
def ppi(
        project_name: str,
        description: str,
        dry_run: bool,
        docker: bool,
        jenkins: bool,
        git: bool,
        helm: bool,
        package: bool) -> None:
    """
    Python Project Initializer (ppi): CLI to initialize a new, structured Python project in the current directory.

    Arguments:\n
        PROJECT_NAME: name of the project to create.
    """
    mask = [docker, jenkins, git, helm, package]
    fns = [docker_init, jenkins_init, git_init, helm_init, package_init]
    optional_executors = list(compress(fns, mask))

    # opening
    standard_init(
        name=project_name,
        desc=description,
        dry_run=dry_run
    )

    # optional
    for_each(
        lambda fn: fn(
            name=project_name,
            dry_run=dry_run
        ),
        optional_executors
    )

    # closing
    closure()


if __name__ == '__main__':
    ppi()
