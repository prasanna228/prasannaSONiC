# SONiC 202505 Release Notes

This document captures the new features added and enhancements done on existing features/sub-features for the SONiC [202505](https://github.com/orgs/sonic-net/projects/25/) release.



# Table of Contents

 * [Branch and Image Location](#branch-and-image-location)
 * [Dependency Version](#dependency-version)
 * [Security Updates](#security-updates)
 * [Feature List](#feature-list)
 * [SAI APIs](#sai-apis)
 * [Contributors](#contributors)


# Branch and Image Location  

Branch : https://github.com/Azure/sonic-buildimage/tree/202505 <br> 
Image  : https://sonic-build.azurewebsites.net/ui/sonic/pipelines  (Example - Image for Broadcom based platforms is [here](https://sonic-build.azurewebsites.net/ui/sonic/pipelines/138/builds/51255/artifacts/98637?branchName=master&artifactName=sonic-buildimage.broadcom))

# Dependency Version

|Feature                    | Version  |
| ------------------------- | --------------- |
| Linux kernel version      | linux_6.1.94-1  |
| SAI   version             | SAI v1.15.1    |
| FRR                       | 10.0.1   |
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
| Debian version			| Continuous to use Bookworm (Debian version 12)	|

Note : The kernel version is migrated to the version that is mentioned in the first row in the above 'Dependency Version' table.


# Security Updates

1. Kernel upgraded from 6.1.38-4 to 6.1.94-1 for SONiC release.<br>
   Change log: https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.1.94

2. Docker is with 27.4.0-debian-stretch  <br>
   Change log: https://docs.docker.com/engine/release-notes/27.0/#2740


# Feature List

| Feature| Feature Description | HLD PR / PR tracking |	Quality |
| ------ | ------- | -----|-----|
| Add Srv6 static config HLD |    | https://github.com/sonic-net/SONiC/pull/1860 |   |
| [testbed_doc] Design doc for deploying a single testbed with multiple servers |   | https://github.com/sonic-net/sonic-mgmt/pull/15395 |   |
| HLD for diagnostic monitoring of CMIS based transceivers |   |https://github.com/sonic-net/SONiC/pull/1828 |   |
| Event/alarm framework HLD update. Integrate with event producer framework.  | https://github.com/sonic-net/SONiC/pull/1409 |   |
| Enhance bulk counter poll HLD and implementation for better accuracy and performance   | https://github.com/sonic-net/SONiC/pull/1864 |   |


Note : The HLD PR's have been updated in ""HLD PR / PR tracking"" coloumn. The code PR's part of the features are mentioned within the HLD PRs. The code PRs not mentioned in HLD PRs are updated in "HLD PR / PR tracking" coloumn along with HLD PRs.

# SAI APIs

Please find the list of API's classified along the newly added SAI features. For further details on SAI API please refer [SAI_1.15.1 Release Notes](https://github.com/opencomputeproject/SAI/blob/master/doc/SAI_1.15.1_ReleaseNotes.md)


# Contributors 

SONiC community would like to thank all the contributors from various companies and the individuals who has contributed for the release. 

<br> 



