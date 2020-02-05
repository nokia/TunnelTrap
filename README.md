# TunnelTrap
Work-in-progress telco honeypot for GPRS Tunneling Protocol (GTP) traffic.

## What will be inside?
This repository will contain scripts that are required to do the following tasks:
- **Generating GTP traffic**: GTP request traffic to immitate the roaming partners.
- **Answering machine**: GTP response traffic based on a "lookup table" model, where handshaking + some specified communication messages are saved, and sent to recipients so that the communication looks like real. More information about the proposed plan can be found in the [Roadmap](https://github.com/thehoneypotter/TunnelTrap/tree/master/Roadmap) folder.
- **Testbed creation**: The answering machine part is actually the honeypot part. However, the testbed needs the traffic genertor as well. This set of scripts will implement creation and tearing down of the testbed. Some samples can be found [here](https://github.com/sidtechnical/core-in-a-box). 

###  Copyright notice
© 2020 Nokia
Licensed under the BSD 3-Clause Clear License
SPDX-License-Identifier: BSD-3-Clause-Clear
