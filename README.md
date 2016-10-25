Remote information Machine
==========

+ Usage: rim [ip] [Arguments] [Output Arguments]

Arguments:
-------------

+ -h --help                - Show this help
+ -u <username>            - Specifies optional user name for login to remote computer.
+ -p <password>            - Specifies optional password for user name.
+ -m <namemachine>         - Specifies the hostname Windows
+ -i <ip address>          - Specifies the IP Address

Output Arguments:
-------------------

+ -a --all                 - Show all Machine Information
+ -j --hardware            - Show Hardware Information
+ -s --software            - Show Software Information

Examples:
--------------------
+ rim 192.168.0.10 --all
+ rim 192.168.0.11 --hardware --software
+ rim 192.168.0.20
