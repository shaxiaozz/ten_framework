#
# Copyright © 2024 Agora
# This file is part of TEN Framework, an open source project.
# Licensed under the Apache License, Version 2.0, with certain conditions.
# Refer to the "LICENSE" file in the root directory for more information.
#
import sys
import utils


def setup():
    # Upgrade pip.
    utils.run_cmd_with_retry(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--upgrade",
            "pip",
        ]
    )

    # Install some python packages which are necessary during the building.
    utils.run_cmd_with_retry(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "jinja2",
        ]
    )

    # Install some python packages which are necessary during the testing.
    utils.run_cmd_with_retry(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "pytest",
        ]
    )
    utils.run_cmd_with_retry(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "requests",
        ]
    )
    utils.run_cmd_with_retry(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "numpy",
        ]
    )
    utils.run_cmd_with_retry(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "opencv-python",
        ]
    )
    utils.run_cmd_with_retry(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "oss2",
        ]
    )
    utils.run_cmd_with_retry(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "psutil",
        ]
    )

    # Using dotenv to load the environment file generated by toolchain on
    # Windows.
    utils.run_cmd_with_retry(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "python-dotenv",
        ]
    )


if __name__ == "__main__":
    setup()