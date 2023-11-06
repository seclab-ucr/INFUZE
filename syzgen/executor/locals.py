
from angr.sim_state import SimState
import logging
import copy

from angr import SimStatePlugin

import sys
sys.setrecursionlimit(10000)

l = logging.getLogger(name=__name__)

# CwT: As oppposed to globals, locals allow deep copy so that stored information is private.


class SimStateLocals(SimStatePlugin):
    def __init__(self, backer=None):
        super(SimStateLocals, self).__init__()
        self._backer = backer if backer is not None else {}

    def set_state(self, state):
        pass

    def merge(self, others, merge_conditions, common_ancestor=None):  # pylint: disable=unused-argument
        # FIXME: merge according its type?
        for other in others:
            for k in other.keys():
                if k not in self:
                    self[k] = other[k]

        return True

    def widen(self, others):  # pylint: disable=unused-argument
        l.warning("Widening is unimplemented for locals")
        return False

    def __getitem__(self, k):
        return self._backer[k]

    def __setitem__(self, k, v):
        self._backer[k] = v

    def __delitem__(self, k):
        del self._backer[k]

    def __contains__(self, k):
        return k in self._backer

    def keys(self):
        return self._backer.keys()

    def values(self):
        return self._backer.values()

    def items(self):
        return self._backer.items()

    def get(self, k, alt=None):
        return self._backer.get(k, alt)

    def pop(self, k, alt=None):
        return self._backer.pop(k, alt)

    @SimStatePlugin.memo
    def copy(self, memo):   # pylint: disable=unused-argument
        return SimStateLocals(copy.deepcopy(self._backer))


SimState.register_default('locals', SimStateLocals)
