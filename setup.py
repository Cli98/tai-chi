import setuptools
from configparser import ConfigParser
from pathlib import Path
from pkg_resources import parse_version

assert parse_version(setuptools.__version__) >= parse_version("36.2")

# note: all settings are in settings.ini; edit there, not here
config = ConfigParser(delimiters=["="])
config.read("settings.ini")
cfg = config["TAICHI"]

cfg_keys = "version description keywords author author_email".split()
expected = (
    cfg_keys
    + "lib_name user branch license status min_python audience language".split()
)

statuses = [
    "1 - Planning",
    "2 - Pre-Alpha",
    "3 - Alpha",
    "4 - Beta",
    "5 - Production/Stable",
    "6 - Mature",
    "7 - Inactive",
]

py_versions = (
    "2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.7 3.0 3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8 3.9 3.10".split()
)

for exp in expected:
    assert exp in cfg, f"missing expected setting: {exp}"
setup_cfg = {k: cfg[k] for k in cfg_keys}

requirements = cfg.get("requirements", "").split()
min_python = cfg["min_python"]
comp_version = py_versions[py_versions.index(min_python):]


setuptools.setup(
    name=cfg["lib_name"],
    license='GPLv3+',
    version=cfg["version"],
    classifiers=[
        "Development Status :: " + statuses[int(cfg["status"])],
        "Intended Audience :: " + cfg["audience"].title(),
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: " + cfg["language"].title(),
    ]
    + [f"Programming Language :: Python :: {v}" for v in comp_version],
    url=f"https://github.com/{cfg['user']}/tai-chi",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=" + cfg["min_python"],
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    project_urls={
        "Documentation": "https://tai-chi-engine.readthedocs.io/",
        "Tracker": "https://github.com/tcengine/tai-chi/issues",
    },
)