# Random Port Scan Generator

### Dependencies

-   Python 3.x and 2.x
-   Scapy

### Usage

`python gen_scan.py`

or

`import gen_scan`

I needed a util to generate random portscan data, so, here is a util that generates random port scan data. Maybe someone'll make use of it.

    import gen_scan
    print({"scan":[generate_box() for x in range(random.randint(1,4))]})

    {'scan': [{'sensenet_qihut': {'ports': [(22, 'ssh'),
         (22, 'ssh'),
         (25, 'smtp'),
         (25, 'smtp'),
         (23, 'telnet'),
         (2792, 'f5_globalsite'),
         (7, 'echo'),
         (174, 'mailq'),
         (25, 'smtp'),
         (77, 'rje'),
         (5680, 'canna'),
         (1959, 'remoteping'),
         (2603, 'ripngd'),
         (346, 'zserv'),
         (2431, 'venus_se'),
         (7003, 'afs3_vlserver'),
         (2947, 'gpsd'),
         (117, 'uucp_path')]}},
      {'sensenet_kuqiza': {'ports': [(53, 'domain'),
         (21, 'ftp'),
         (53, 'domain'),
         (22, 'ssh'),
         (67, 'bootps'),
         (23, 'telnet'),
         (67, 'bootps'),
         (37, 'time'),
         (9, 'discard'),
         (7008, 'afs3_update'),
         (21, 'ftp'),
         (2628, 'dict'),
         (18, 'msp'),
         (17500, 'db_lsp'),
         (6007, 'x11_7'),
         (37, 'time'),
         (111, 'sunrpc')]}},
      {'sensenet_z': {'ports': [(138, 'netbios_dgm'),
         (137, 'netbios_ns'),
         (138, 'netbios_dgm'),
         (67, 'bootps'),
         (23, 'telnet'),
         (67, 'bootps'),
         (6444, 'sge_qmaster'),
         (9, 'discard'),
         (3689, 'daap'),
         (543, 'klogin'),
         (161, 'snmp'),
         (3306, 'mysql')]}}]}
         ```
