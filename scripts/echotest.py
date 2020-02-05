# © 2020 Nokia
# Licensed under the BSD 3-Clause Clear License
# SPDX-License-Identifier: BSD-3-Clause-Clear

from scapy.all import *
from scapy.contrib import gtp_v2


load_contrib('gtp_v2')

#packet = Ether()/IP()/UDP(dport=2152)/GTPHeader(teid=0x12345678)/Raw('x'*20) 
packet = Ether()/IP()/UDP(dport=2152)/GTPV2EchoRequest()/Raw('x'*20)                                                                                                                                    
packet.show() 
answer = sr2(packet)
answer.show()
