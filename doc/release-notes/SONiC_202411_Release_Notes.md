# SONiC 202411 Release Notes

This document captures the new features added and enhancements done on existing features/sub-features for the SONiC [202411](https://github.com/orgs/sonic-net/projects/18/) release.



# Table of Contents

 * [Branch and Image Location](#branch-and-image-location)
 * [Dependency Version](#dependency-version)
 * [Security Updates](#security-updates)
 * [Feature List](#feature-list)
 * [SAI APIs](#sai-apis)
 * [Contributors](#contributors)


# Branch and Image Location  

Branch : https://github.com/Azure/sonic-buildimage/tree/202411 <br> 
Image  : https://sonic-build.azurewebsites.net/ui/sonic/pipelines  (Example - Image for Broadcom based platforms is [here](https://sonic-build.azurewebsites.net/ui/sonic/pipelines/138/builds/51255/artifacts/98637?branchName=master&artifactName=sonic-buildimage.broadcom))

# Dependency Version

|Feature                    | Version  |
| ------------------------- | --------------- |
| Linux kernel version      | linux_6.1.38-4  |
| SAI   version             | SAI v1.15.0    |
| FRR                       | 8.5.4   |
| LLDPD                     | 1.0.16-1+deb12u1 |
| TeamD                     | 1.31-1    |
| SNMPD                     | 5.9.3+dfsg-2 |
| Python                    | 3.11.2-6    |
| syncd                     | 1.0.0    |
| swss                      | 1.0.0    |
| radvd                     | 2.19-1+b1 |
| isc-dhcp                  | 4.4.3-P1-2  |
| sonic-telemetry           | 1.1    |
| redis-server/ redis-tools | 7.0.15-1~deb12u1   |
| Debian version			| Migrated to Bookworm (Debian version 12)	|

Note : The kernel version is migrated to the version that is mentioned in the first row in the above 'Dependency Version' table.


# Security Updates

1. Kernel upgraded from 5.10.179-3 to 6.1.38-4 for SONiC release.<br>
   Change log: https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.1.38

2. Docker is with 24.0.2-debian-stretch  <br>
   Change log: https://docs.docker.com/engine/release-notes/24.0/#2402


# Feature List

| Feature| Feature Description | HLD PR / PR tracking |	Quality |
| ------ | ------- | -----|-----|
| ***Authentication Manager for PAC*** | This feature implements the authentication manager for PAC like API interface, generic header and makefile and common header files.   | [1853](https://github.com/sonic-net/SONiC/issues/1853)   | [Alpha](https://github.com/sonic-net/SONiC/blob/master/doc/SONiC%20feature%20quality%20definition.md) | 
| ***Banner HLD*** | This feature covers the definition, design and implementation of SONiC Banner feature and Banner CLI. |[1361](https://github.com/sonic-net/SONiC/pull/1361)| [Alpha](https://github.com/sonic-net/SONiC/blob/master/doc/SONiC%20feature%20quality%20definition.md) |
| ***Broadcom syncd bookworm upgrade*** | This feature implements the migration of platform broadcom docker syncd from bullseye to bookworm | 
| ***HLD for cli sessions feature*** | This feature describes the requirements, architecture and general flow details of serial connection config in SONIC OS based switches. | [1367](https://github.com/sonic-net/SONiC/pull/1367) | [Alpha](https://github.com/sonic-net/SONiC/blob/master/doc/SONiC%20feature%20quality%20definition.md) |
| ***Mac Authentication Bypass*** | This feature implements MAB protocol related common header files for generic files and its changes. | [1854](https://github.com/sonic-net/SONiC/issues/1854)   | [Alpha](https://github.com/sonic-net/SONiC/blob/master/doc/SONiC%20feature%20quality%20definition.md) | 
| ***Notification to SAI that fast-reboot is done*** | This feature enables the notification for SAI that fastboot is done by setting SAI_SWITCH_ATTR_FAST_API_ENABLE to false when fastboot is done | [1396](https://github.com/sonic-net/sonic-sairedis/pull/1396) | [Alpha](https://github.com/sonic-net/SONiC/blob/master/doc/SONiC%20feature%20quality%20definition.md) |
| ***Port Access Control Phase 1*** | This feature provides a means of preventing unauthorized access by users to the services offered by a Network. | [1315](https://github.com/sonic-net/SONiC/pull/1315) | [Alpha](https://github.com/sonic-net/SONiC/blob/master/doc/SONiC%20feature%20quality%20definition.md) |
| ***Update calculation for dynamic buffer management*** | This feature fixes a bug in lossless headroom calculation regarding the small packet percentage which should be calculated in a size-based approach instead of packet-based and also adjust the Mellanox-specific lossless headroom calculation algorithm.    | [3235](https://github.com/sonic-net/sonic-swss/pull/3235)   | [Alpha](https://github.com/sonic-net/SONiC/blob/master/doc/SONiC%20feature%20quality%20definition.md) | 

Note : The HLD PR's have been updated in ""HLD PR / PR tracking"" coloumn. The code PR's part of the features are mentioned within the HLD PRs. The code PRs not mentioned in HLD PRs are updated in "HLD PR / PR tracking" coloumn along with HLD PRs.

# SAI APIs

Please find the list of API's classified along the newly added SAI features. For further details on SAI API please refer [SAI_1.15.0 Release Notes](https://github.com/opencomputeproject/SAI/blob/master/doc/SAI_1.15.0_ReleaseNotes.md)


# Contributors 

SONiC community would like to thank all the contributors from various companies and the individuals who has contributed for the release. Special thanks to the major contributors - Alibaba, Arista, AvizNetworks, Broadcom, Capgemini, Centec, Cisco, Dell, eBay, Edge-Core, Google, InMon, Inspur, Intel, Marvell, Micas Networks, Microsoft, NTT, Nvidia, Orange, PLVision & xFlow Research Inc.   

<br> 



