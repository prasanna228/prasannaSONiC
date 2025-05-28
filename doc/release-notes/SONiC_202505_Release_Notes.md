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
| SAI   version             | SAI v1.16.1    |
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
| ***Add Srv6 static config HLD*** | This feature implements the change in SONiC to support static configuration of Segment-routing over IPv6. Besides, a YANG model specification for the new table in CONFIG_DB is also defined.   | [1860](https://github.com/sonic-net/SONiC/pull/1860) |   |
| ***Authentication Support for 802.1X and MAB*** | This feature supports the authentication for 802.1X and for MAB support |  [1977](https://github.com/sonic-net/SONiC/issues/1977) |   |
| ***CVL Enhancements*** | This feature enhances the cvl custom validation to demonstrate its capability to allow/deny configuration based on other db data. 	|  [1969](https://github.com/sonic-net/SONiC/issues/1969) |   |
| [testbed_doc] ***Design doc for deploying a single testbed with multiple servers*** | This implementation recommends to leverage the servers to deploy single testbed with multiple servers instead of a single server for a single testbed. | [15395](https://github.com/sonic-net/sonic-mgmt/pull/15395) |   |
| ***Enhance bulk counter poll HLD and implementation for better accuracy and performance***  | This feature implements counter-polling interval more accurate by setting bulk chunk size for a counter or per counter and collect timestamp in sairedis instead of in the Lua plugin  | [1864](https://github.com/sonic-net/SONiC/pull/1864) |   |
| ***Event/alarm framework HLD update. Integrate with event producer framework.*** | This implements the availability of event producer framework, and this design is updated to provide DB/persistent support for event history. Also gnmi/rest openconfig interface for get operations and gnmi subscription.  | [1409](https://github.com/sonic-net/SONiC/pull/1409) |   |
| ***HLD for diagnostic monitoring of CMIS based transceivers*** | This feature provides an overview of how SONiC reads and stores the various diagnostic parameters read from a CMIS based transceiver.  | [1828](https://github.com/sonic-net/SONiC/pull/1828) |   |
| ***Link flap count and last flap time*** | This feature introduces a new CLI command, show interfaces flap, to display interface flap information. The command fetches details about flap counts, admin and operational status, and timestamps of link down/up events for specified or all interfaces. | [3724](https://github.com/sonic-net/sonic-utilities/pull/3724) |  |
| ***Local fault and remote fault*** | The feature adds a new debug.py module to handle SFP diagnostics and debugging and replaced existing utility methods with functions from utilities_common.platform_sfputil_helper. And also have, registered debug as a subcommand in sfputil/main.py.  | [3811](https://github.com/sonic-net/sonic-utilities/pull/3811) |  |
| ***Migrate from ntpd to Chrony*** | This feature is to describe the migration from ntpd to Chrony, along with the need and the changes that has been implemented.	|  [1852](https://github.com/sonic-net/SONiC/pull/1852) |   |
| ***MSTP configuration tool and utilities*** | This implements the MSTP configuration tool and its utilities for API packages.	|  [1971](https://github.com/sonic-net/SONiC/issues/1971) |   |
| ***MSTP State Machines*** | This implements the MSTP state machine packages and its utilities.	|  [1970](https://github.com/sonic-net/SONiC/issues/1970) |   |
| ***PAC Phase 2*** | This feature implements the Port Access Control (PAC) by means of preventing unauthorized access by users to the services offered by a Network. |  [1978](https://github.com/sonic-net/SONiC/issues/1978) |   |
| ***PVST*** | 	|  [1968](https://github.com/sonic-net/SONiC/issues/1968) |   |
| ***Per-Lane DOM data*** | This feature implements the CMIS diagnostic monitoring for SONiC | [1885](https://github.com/sonic-net/SONiC/issues/1885) |  |
| ***Port level Pre-FEC / Post-FEC BER (TP1, TP3, TP5)*** |	This feature adds design proposal for Port FEC BER and enhances the collect and compute of the FEC BER on each port. Also, modified the port_rates.lua , portstat.py and netstat.py | [1829](https://github.com/sonic-net/SONiC/pull/1829) |
| ***Support for Fine-Grained ECMP (consistent hashing) with dynamic nexthops*** | This implements the addition of prefix-based match mode that allows list of nexthops IP to be discovered from route updates instead of requiring users to configure them statically. The new mode will add support for consistent hashing as traditionally implemented in other commercial NOSes.	| [1823](https://github.com/sonic-net/SONiC/pull/1823) |  |
| ***Transformer enhancement to support YANG model based config replace and delete*** | This feature enhances the transformer component in management framework will support PUT/REPLACE and DELETE operations using OpenConfig YANG models, enabling configuration data replacement and deletion through YANG data tree traversal.    | [1950](https://github.com/sonic-net/SONiC/pull/1950) |  |
| ***[test plan] Test plan for BGP scale test*** | This test plan is to test if control/data plane can handle the initialization/flapping of numerous BGP session holding a lot routes, and estimate the impact on it.  |  [15702](https://github.com/sonic-net/sonic-mgmt/pull/15702) |  | 
| ***Translib bulk API support*** |	This implements the test cases part of sonic-gnmi and mgmt-framework.| [1972]( https://github.com/sonic-net/SONiC/issues/1972) |   |
| ***UMF infra enhancement*** | This fixes the pipeline tests which were failing after recent openconfig-interface related changes in sonic-mgmt-common repo.	|  [1974](https://github.com/sonic-net/SONiC/issues/1974) |   |
| ***YANG RPC support via gNOI*** | This feature implements the The YANG RPC support using gNOI.The protobufs are auto-generated as part of build from YANG files. |  [1973](https://github.com/sonic-net/SONiC/issues/1973) |   |




Note : The HLD PR's have been updated in ""HLD PR / PR tracking"" coloumn. The code PR's part of the features are mentioned within the HLD PRs. The code PRs not mentioned in HLD PRs are updated in "HLD PR / PR tracking" coloumn along with HLD PRs.

# SAI APIs

Please find the list of API's classified along the newly added SAI features. For further details on SAI API please refer [SAI_1.16.1 Release Notes](https://github.com/opencomputeproject/SAI/blob/master/doc/SAI_1.16.1_ReleaseNotes.md)


# Contributors 

SONiC community would like to thank all the contributors from various companies and the individuals who has contributed for the release. 

<br> 



