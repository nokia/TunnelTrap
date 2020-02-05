## Proposed functionalities              

- **Functionality 1**: *Intrusion detection* ---trigging alert of an intruder as early as possible, for example for the incedence response team.

- **Functionality 2**: *Covertness (undetectability)* --- an attacker should not be able to detect the presence of a honeypot, at least at first glance.

- **Functionality 3**: *Filtering*  --- Honeypot should have some kind of firewall (within itself or with a dedicated firewall) or filtering mechanism (network-based or machine learning-based) to route/divert only suspicious traffic into honeypot.

- **Functionality 4**: *Reproducablity* --- mimicking the actual network nodes by processing and responding everything as if it the actual network

- **Functionality 5**: Interactibility --- starting from low-interaction to begin with, and then to high-interaction honeypot, the honeypot has to keep the intruder busy by interactng with it. 

- **Functionaltiy 6**: Logging/reporting --- irrespecive of the end result, the honeypot should always log (record) everything and  produce a rreport for further analysis. This is as important as any other functionality because honeypots are often isoloated environments, and a skilled attacker would always want to  destroy his traces in case the presence of a honeypot is detected.

## Proposed modes of operatipon
- **Filter mode**: Filter the GTP traffic as per [GSMA FS.20 firewall rules](https://www.gsma.com/security/resources/fs-20-gprs-tunnelling-protocol-gtp-security-v3-0/) --- respond to traffic that has already been filtered, and log everything.
- **Offensive mode**: No filtering and answer everything --- respond to everything and log everything.
- **Silent mode**: No filtering, no answering, but observe everything --- silently log everything, and selectively respond, to create a dataset for future studies. 
