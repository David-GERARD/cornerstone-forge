"""PhotonForge implementation of Cornerstone's silicon photonics PDKs.

Each technology is implemented as a subpackage, e.g.::

    from cornerstone_forge import si_220nm_passive as cs
"""

from importlib.metadata import version

__version__ = version("cornerstone-forge")
