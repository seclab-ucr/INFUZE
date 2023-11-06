
import unittest
from syzgen.parser.generate import reduce_lenType

from syzgen.parser.syscalls import Syscall


class TestGenerate(unittest.TestCase):
    TestCases = [
        {
            "syscall": {'CallName': 'syz_IOConnectCallMethod', 'SubName': 'IOBluetoothHCIUserClient_Group0_1', 'status': 3, 'args': [{'type': 'resource', 'offset': 0, 'size': 8, 'typename': 'connection', 'data': [0, 0, 0, 0, 0, 0, 0, 0], 'access': True, 'name': 'IOBluetoothHCIUserClient_port', 'parent': 'io_connect_t'}, {'type': 'const', 'offset': 0, 'size': 4, 'typename': 'selector', 'data': [0, 0, 0, 0], 'access': True}, {'type': 'ptr', 'offset': 0, 'size': 8, 'typename': 'input', 'optional': False, 'dir': 1, 'ref': {'type': 'buffer', 'offset': 0, 'size': 128, 'access': True}}, {'type': 'range', 'offset': 0, 'size': 4, 'typename': 'inputCnt', 'data': [15, 0, 0, 0], 'access': True, 'path': [2], 'bitSize': 64, 'min': 0, 'max': 16, 'stride': 1}, {'type': 'ptr', 'offset': 0, 'size': 8, 'typename': 'inputStruct', 'optional': False, 'dir': 1, 'ref': {'type': 'struct', 'offset': 0, 'size': 116, 'fields': [{'type': 'ptr', 'offset': 0, 'size': 8, 'optional': False, 'dir': 1, 'ref': {'type': 'struct', 'offset': 0, 'size': 4096, 'fields': [{'type': 'buffer', 'offset': 0, 'size': 4, 'data': [0, 253, 255, 255], 'access': True}, {'type': 'buffer', 'offset': 4, 'size': 4092, 'access': True}], 'isArray': False}}, {'type': 'ptr', 'offset': 8, 'size': 8, 'optional': False, 'dir': 1, 'ref': {'type': 'struct', 'offset': 0, 'size': 4096, 'fields': [{'type': 'const', 'offset': 0, 'size': 1, 'data': [0], 'access': True}, {'type': 'buffer', 'offset': 1, 'size': 1, 'data': [192], 'access': True}, {'type': 'buffer', 'offset': 2, 'size': 1, 'data': [0], 'access': True}, {'type': 'buffer', 'offset': 2, 'size': 1, 'data': [255], 'access': True}, {'type': 'buffer', 'offset': 4, 'size': 4092, 'access': True}], 'isArray': False}}, {'type': 'const', 'offset': 16, 'size': 8, 'data': [0, 0, 0, 0, 0, 0, 0, 0], 'access': True}, {'type': 'const', 'offset': 24, 'size': 8, 'data': [0, 0, 0, 0, 0, 0, 0, 0], 'access': True}, {'type': 'buffer', 'offset': 32, 'size': 24, 'data': [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, {'type': 'range', 'offset': 56, 'size': 8, 'data': [1, 0, 0, 0, 0, 0, 0, 0], 'access': True, 'path': [4, 0, 0], 'bitSize': 8, 'min': 1, 'max': 8, 'stride': 1}, {'type': 'range', 'offset': 64, 'size': 8, 'data': [4, 0, 0, 0, 0, 0, 0, 0], 'access': True, 'path': [4, 0, 8], 'bitSize': 8, 'min': 1, 'max': 8, 'stride': 1}, {'type': 'range', 'offset': 72, 'size': 8, 'data': [1, 248, 0, 0, 0, 0, 0, 0], 'access': True, 'min': 1, 'max': 65535, 'stride': 1}, {'type': 'range', 'offset': 80, 'size': 8, 'data': [1, 128, 0, 0, 0, 0, 0, 0], 'access': True, 'min': 1, 'max': 65535, 'stride': 1}, {'type': 'buffer', 'offset': 88, 'size': 24, 'data': [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, {'type': 'const', 'offset': 112, 'size': 4, 'data': [0, 0, 0, 0], 'access': True}], 'isArray': False}}, {'type': 'const', 'offset': 0, 'size': 4, 'typename': 'inputStructCnt', 'data': [116, 0, 0, 0], 'access': True, 'path': [4], 'bitSize': 8}, {'type': 'ptr', 'offset': 0, 'size': 8, 'typename': 'output', 'optional': False, 'dir': 2, 'ref': {'type': 'struct', 'offset': 0, 'size': 128, 'fields': [{'type': 'buffer', 'offset': 0, 'size': 8, 'data': [255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, {'type': 'buffer', 'offset': 8, 'size': 8, 'data': [255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, {'type': 'buffer', 'offset': 16, 'size': 8, 'data': [255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, {'type': 'buffer', 'offset': 24, 'size': 8, 'data': [255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, {'type': 'buffer', 'offset': 32, 'size': 8, 'data': [255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, {'type': 'buffer', 'offset': 40, 'size': 8, 'data': [255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, {'type': 'buffer', 'offset': 48, 'size': 8, 'data': [255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, {'type': 'buffer', 'offset': 56, 'size': 8, 'data': [255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, {'type': 'buffer', 'offset': 64, 'size': 8, 'data': [255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, {'type': 'buffer', 'offset': 72, 'size': 8, 'data': [255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, {'type': 'buffer', 'offset': 80, 'size': 8, 'data': [255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, {'type': 'buffer', 'offset': 88, 'size': 8, 'data': [255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, {'type': 'buffer', 'offset': 96, 'size': 8, 'data': [255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, {'type': 'buffer', 'offset': 104, 'size': 8, 'data': [255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, {'type': 'buffer', 'offset': 112, 'size': 8, 'data': [255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, {'type': 'buffer', 'offset': 120, 'size': 8, 'data': [255, 255, 255, 255, 255, 255, 255, 255], 'access': True}], 'isArray': True}}, {'type': 'ptr', 'offset': 0, 'size': 8, 'typename': 'outputCnt', 'optional': False, 'dir': 1, 'ref': {'type': 'range', 'offset': 0, 'size': 4, 'data': [0, 0, 0, 0], 'access': True, 'path': [6], 'bitSize': 64, 'min': 0, 'max': 16, 'stride': 1}}, {'type': 'ptr', 'offset': 0, 'size': 8, 'typename': 'outputStruct', 'optional': False, 'dir': 2, 'ref': {'type': 'buffer', 'offset': 0, 'size': 4, 'data': [0, 0, 0, 0], 'access': True}}, {'type': 'ptr', 'offset': 0, 'size': 8, 'typename': 'outputStructCnt', 'optional': False, 'dir': 1, 'ref': {'type': 'const', 'offset': 0, 'size': 4, 'data': [4, 0, 0, 0], 'access': True, 'path': [8], 'bitSize': 8}}]},
            "finalize": False,
            "resize": True,
            "res": {'CallName': 'syz_IOConnectCallMethod', 'SubName': 'IOBluetoothHCIUserClient_Group0_1', 'status': 3, 'args': [{'type': 'resource', 'offset': 0, 'size': 8, 'typename': 'connection', 'data': [0, 0, 0, 0, 0, 0, 0, 0], 'access': True, 'name': 'IOBluetoothHCIUserClient_port', 'parent': 'io_connect_t'}, {'type': 'const', 'offset': 0, 'size': 4, 'typename': 'selector', 'data': [0, 0, 0, 0], 'access': True}, {'type': 'ptr', 'offset': 0, 'size': 8, 'typename': 'input', 'optional': False, 'dir': 1, 'ref': {'type': 'buffer', 'offset': 0, 'size': 128, 'access': True}}, {'type': 'len', 'offset': 0, 'size': 4, 'typename': 'inputCnt', 'lenField': 'input', 'bitSize': 64, 'max': 16, 'min': 0}, {'type': 'ptr', 'offset': 0, 'size': 8, 'typename': 'inputStruct', 'optional': False, 'dir': 1, 'ref': {'type': 'struct', 'offset': 0, 'size': 116, 'fields': [{'type': 'ptr', 'offset': 0, 'size': 8, 'optional': False, 'dir': 1, 'ref': {'type': 'struct', 'offset': 0, 'size': 8, 'fields': [{'type': 'buffer', 'offset': 0, 'size': 4, 'data': [0, 253, 255, 255], 'access': True}, {'type': 'array', 'offset': 4, 'size': 4, 'field': {'type': 'buffer', 'offset': 0, 'size': 1, 'data': [255], 'access': True}, 'minLen': 4, 'maxLen': 4}], 'isArray': False}}, {'type': 'ptr', 'offset': 8, 'size': 8, 'optional': False, 'dir': 1, 'ref': {'type': 'struct', 'offset': 0, 'size': 8, 'fields': [{'type': 'const', 'offset': 0, 'size': 1, 'data': [0], 'access': True}, {'type': 'buffer', 'offset': 1, 'size': 1, 'data': [192], 'access': True}, {'type': 'buffer', 'offset': 2, 'size': 1, 'data': [0], 'access': True}, {'type': 'buffer', 'offset': 3, 'size': 1, 'data': [255], 'access': True}, {'type': 'array', 'offset': 4, 'size': 4, 'field': {'type': 'buffer', 'offset': 0, 'size': 1, 'data': [255], 'access': True}, 'minLen': 4, 'maxLen': 4}], 'isArray': False}}, {'type': 'const', 'offset': 16, 'size': 8, 'data': [0, 0, 0, 0, 0, 0, 0, 0], 'access': True}, {'type': 'const', 'offset': 24, 'size': 8, 'data': [0, 0, 0, 0, 0, 0, 0, 0], 'access': True}, {'type': 'buffer', 'offset': 32, 'size': 24, 'data': [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, {'type': 'range', 'offset': 56, 'size': 8, 'data': [1, 0, 0, 0, 0, 0, 0, 0], 'access': True, 'path': [4, 0, 0], 'bitSize': 8, 'min': 1, 'max': 8, 'stride': 1}, {'type': 'range', 'offset': 64, 'size': 8, 'data': [4, 0, 0, 0, 0, 0, 0, 0], 'access': True, 'path': [4, 0, 8], 'bitSize': 8, 'min': 1, 'max': 8, 'stride': 1}, {'type': 'range', 'offset': 72, 'size': 8, 'data': [1, 248, 0, 0, 0, 0, 0, 0], 'access': True, 'min': 1, 'max': 65535, 'stride': 1}, {'type': 'range', 'offset': 80, 'size': 8, 'data': [1, 128, 0, 0, 0, 0, 0, 0], 'access': True, 'min': 1, 'max': 65535, 'stride': 1}, {'type': 'buffer', 'offset': 88, 'size': 24, 'data': [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, {'type': 'const', 'offset': 112, 'size': 4, 'data': [0, 0, 0, 0], 'access': True}, {'type': 'array', 'offset': 116, 'size': 0, 'field': {'type': 'buffer', 'offset': 0, 'size': 1, 'data': [255], 'access': True}, 'minLen': 0, 'maxLen': 0}], 'isArray': False}}, {'type': 'const', 'offset': 0, 'size': 4, 'typename': 'inputStructCnt', 'data': [116, 0, 0, 0], 'access': True, 'path': [4], 'bitSize': 8}, {'type': 'ptr', 'offset': 0, 'size': 8, 'typename': 'output', 'optional': False, 'dir': 2, 'ref': {'type': 'array', 'offset': 0, 'size': 16, 'field': {'type': 'buffer', 'offset': 0, 'size': 8, 'data': [255, 255, 255, 255, 255, 255, 255, 255], 'access': True}, 'minLen': 16, 'maxLen': 16}}, {'type': 'ptr', 'offset': 0, 'size': 8, 'typename': 'outputCnt', 'optional': False, 'dir': 1, 'ref': {'type': 'len', 'offset': 0, 'size': 4, 'lenField': 'output', 'bitSize': 64, 'max': 16, 'min': 0}}, {'type': 'ptr', 'offset': 0, 'size': 8, 'typename': 'outputStruct', 'optional': False, 'dir': 2, 'ref': {'type': 'buffer', 'offset': 0, 'size': 4, 'data': [0, 0, 0, 0], 'access': True}}, {'type': 'ptr', 'offset': 0, 'size': 8, 'typename': 'outputStructCnt', 'optional': False, 'dir': 1, 'ref': {'type': 'const', 'offset': 0, 'size': 4, 'data': [4, 0, 0, 0], 'access': True, 'path': [8], 'bitSize': 8}}]}
        }
    ]

    def test_reduce_lenType(self):
        for testcase in self.TestCases:
            syscall = Syscall.load(testcase["syscall"])
            print(syscall.repr())
            reduce_lenType(syscall, testcase["finalize"], resize=testcase["resize"])
            print(syscall.repr())
            self.assertTrue(syscall.toJson() == testcase["res"])
