# SONiC 202405 Release Notes

This document captures the new features added and enhancements done on existing features/sub-features for the SONiC [202405](https://github.com/orgs/sonic-net/projects/17/) release.



# Table of Contents

 * [Branch and Image Location](#branch-and-image-location)
 * [Dependency Version](#dependency-version)
 * [Security Updates](#security-updates)
 * [Feature List](#feature-list)
 * [SAI APIs](#sai-apis)
 * [Contributors](#contributors)


# Branch and Image Location  

Branch : https://github.com/Azure/sonic-buildimage/tree/202405 <br> 
Image  : https://sonic-build.azurewebsites.net/ui/sonic/pipelines  (Example - Image for Broadcom based platforms is [here](https://sonic-build.azurewebsites.net/ui/sonic/pipelines/138/builds/51255/artifacts/98637?branchName=master&artifactName=sonic-buildimage.broadcom))

# Dependency Version

|Feature                    | Version  |
| ------------------------- | --------------- |
| Linux kernel version      | linux_5.10.0-23-2-$(5.10.179)  |
| SAI   version             | SAI v1.13.3    |
| FRR                       | 8.5.1   |
| LLDPD                     | 1.0.16-1+deb12u1 |
| TeamD                     | 1.30-1    |
| SNMPD                     | 5.9+dfsg-4+deb11u1    |
| Python                    | 3.9.2-1    |
| syncd                     | 1.0.0    |
| swss                      | 1.0.0    |
| radvd                     | 2.18-3    |
| isc-dhcp                  | 4.4.1-2.3+deb11u2  |
| sonic-telemetry           | 1.1    |
| redis-server/ redis-tools | 5.0.3-3~bpo9+2    |
| Debian version			| Continuous to use Bullseye (Debian version 11)	|

Note : The kernel version is migrated to the version that is mentioned in the first row in the above 'Dependency Version' table.


# Security Updates

1. Kernel upgraded from 5.10.103-1 to 5.10.136-1 for SONiC release.<br>
   Change log: https://cdn.kernel.org/pub/linux/kernel/v5.x/ChangeLog-5.10.136

2. Docker upgraded from  24.0.2-debian-stretch to 24.0.7-debian-stretch <br>
   Change log: https://docs.docker.com/engine/release-notes/24.0/#2407


# Feature List

| Feature| Feature Description | HLD PR / PR tracking |	Quality |
| ------ | ------- | -----|-----|
| ***Add SRv6 SID L3Adj*** | This feature describes the extensions of SRv6Orch required to support the programming of the L3Adj associated with SRv6 uA, End.X, uDX4, uDX6, End.DX4, and End.DX6 behaviors.     |  [1472](https://github.com/sonic-net/SONiC/pull/1472)     | Alpha |
| ***Bookworm Upgrade LLDP, SNMP subagent, ICCPD, PDE*** | This feature impliments the bookworm upgrade for LLDP, SNMP subagent, ICCPD, PDE |  [1677](https://github.com/sonic-net/SONiC/issues/1677)     | Alpha |
| ***CVL dynamic table field support*** |      | [1682](https://github.com/sonic-net/SONiC/issues/1682) | Alpha |
| ***CVL Infra Enhancement*** |      |  [1680](https://github.com/sonic-net/SONiC/issues/1680) | Alpha |
| ***CVL singleton table and multi-list table support*** |      | [1681](https://github.com/sonic-net/SONiC/issues/1681)      | Alpha |
| ***Extend CMIS host management to support warmboot and fastboot*** |      | [1663](https://github.com/sonic-net/SONiC/pull/1663) | Alpha |
| ***Go Code format checker and formatter*** |      | [1678](https://github.com/sonic-net/SONiC/issues/1678) | Alpha |
| ***RESTCONF infra enhancement*** |      | [1679](https://github.com/sonic-net/SONiC/issues/1679) | Alpha |
| ***SONiC Debian Upgrade Cadence process improvement*** |      | [1632](https://github.com/sonic-net/SONiC/issues/1632) | Alpha |
| ***TLS1.3 Support*** |      | [1531](https://github.com/sonic-net/SONiC/issues/1531) | Alpha |
| ***Upgrade SWSS/SyncD to debian 12*** |      | [1670](https://github.com/sonic-net/SONiC/pull/1670) | Alpha |


Note : The HLD PR's have been updated in ""HLD PR / PR tracki
ng"" coloumn. The code PR's part of the features are mentioned within the HLD PRs. The code PRs not mentioned in HLD PRs are updated in "HLD PR / PR tracking" coloumn along with HLD PRs.

# SAI APIs

Please find the list of API's classified along the newly added SAI features. For further details on SAI API please refer [SAI_1.13.3 Release Notes](https://github.com/opencomputeproject/SAI/blob/master/doc/SAI_1.13.3_ReleaseNotes.md)


# Contributors 

SONiC community would like to thank all the contributors from various companies and the individuals who has contributed for the release. Special thanks to the major contributors - AMD, Aviz Networks, Broadcom, Capgemini, Centec, Cisco,  Dell, eBay, Edge core, Google, InMon, Inspur, Marvell, Micas Networks, Microsoft, NTT, Nvidia, Orange, Ufispace, xFlow Research Inc.    

<br> 



