There will be periodic SONiC Roadmap planning sessions.  These will define the new capabilities to be delivered by the SONiC project in its next release.  It's expected that new feature contributions will be aligned with the roadmap.  

Pull requests for features that are not in the roadmap may not be accepted into the project.  This is to help ensure the project can produce a stable, reliable release and make progress.  

| Release    | Release Date | SAI version   | Features Included                  |
|------------|--------------|---------------|------------------------------------|
|SONiC.202411| 11/30/2024   |  SAI1.15.1    | [Progress Tracking](https://github.com/orgs/sonic-net/projects/18) |
|		     |				|				|[[HLD] bmp for monitoring SONiC BGP info](https://github.com/sonic-net/SONiC/pull/1621) |
|		     |				|				|[Add HLD for FRR-SONiC Communication Channel Enhancements](https://github.com/sonic-net/SONiC/pull/1620) |
|			 |				|				|[Authentication Manager for PAC](https://github.com/sonic-net/SONiC/issues/1853)
|  			 |				|				|[Banner HLD](https://github.com/sonic-net/SONiC/blob/master/doc/banner/banner_hld.md) |
|		     |				|				|[BBR and Overlay ECMP coexistence with dual ToR](https://github.com/sonic-net/SONiC/issues/1735) |
|		     |				|				|[Broadcom syncd bookworm upgrade](https://github.com/sonic-net/SONiC/issues/1815) |
|			 |				|				|[Everflow DSCP marking using Metadata](https://github.com/sonic-net/SONiC/pull/1743)
|		     |				|				|[HLD for cli sessions feature](https://github.com/sonic-net/SONiC/pull/1367) |
|			 |				|				|[Mac Authentication Bypass](https://github.com/sonic-net/SONiC/issues/1854)
|		     |				|				|[Port Access Control Phase 1](https://github.com/sonic-net/SONiC/issues/1724) |
|		     |				|				|[Silicon config support for Broadcom yml file and property overwrite](https://github.com/sonic-net/SONiC/issues/1814) |
|		     |				|				|[upgrade FRR to version 10.0.1, upgrade libyang2 to 2.1.148.](https://github.com/sonic-net/sonic-buildimage/pull/20269) |
|		     |				|				|[Upgrade to FRR 10.0.1](https://github.com/sonic-net/SONiC/issues/1565) |
|SONiC.202405| 05/31/2024   |  SAI1.14.0    | [Progress Tracking](https://github.com/orgs/sonic-net/projects/17) |
|		     |				|				|[[LLDP][T2] Advertise Chassis Hostname when present.](https://github.com/sonic-net/sonic-buildimage/pull/19076)  |
|		     |				|				|[[NTP] Fix config template to init default parameters](https://github.com/sonic-net/sonic-buildimage/pull/18736) | 
|		     |				|				|[[SubnetDecap] Add subnet decap HLD](https://github.com/sonic-net/SONiC/pull/1657)   |
|		     |				|				|[Add details of sff_mgr regarding deterministic bringup for SFF compliant modules](https://github.com/sonic-net/SONiC/pull/1334)  |
|		     |				|				|[Add HLD for IPv4 port based DHCP server in SONiC](https://github.com/sonic-net/SONiC/pull/1282)  |
|		     |				|				|[[Add LDAP HLD](https://github.com/sonic-net/SONiC/pull/1487)  |
|		     |				|				|[Add SRv6 SID L3Adj](https://github.com/sonic-net/SONiC/pull/1472)      |
|		     |				|				|[Base OS upgrade to Bookworm](https://github.com/sonic-net/sonic-buildimage/pull/17234)   |
|		     |				|				|[Bookworm Upgrade LLDP, SNMP subagent, ICCPD, PDE, FRR](https://github.com/sonic-net/SONiC/issues/1677)      |
|		     |				|				|[[CVL dynamic table field support]](https://github.com/sonic-net/SONiC/issues/1682)  |
|		     |				|				|[CVL Infra Enhancement](https://github.com/sonic-net/SONiC/issues/1680)  |
|		     |				|				|[CVL singleton table and multi-list table support](https://github.com/sonic-net/SONiC/issues/1681)       |
|		     |				|				|[Decrease number of false positive triggers while using  PFC watchdog](https://github.com/sonic-net/SONiC/pull/1660) 
|		     |				|				|[Extend CMIS host management debug capability](https://github.com/sonic-net/SONiC/pull/1476)  |
|		     |				|				|[Extend CMIS host management to support warmboot and fastboot](https://github.com/sonic-net/SONiC/pull/1663)  |
|		     |				|				|[Go Code format checker and formatter](https://github.com/sonic-net/SONiC/issues/1678)  |
|		     |				|				|[High-level Design of Storage Monitoring Daemon](https://github.com/sonic-net/SONiC/pull/1481)    |
|		     |				|				|[HLD: DHCPv4 - Specify dhcp relay's Gateway explicitly with Primary address.](https://github.com/sonic-net/SONiC/pull/1470)  |
|		     |				|				|[NetScan over VLAN support](https://github.com/sonic-net/SONiC/pull/1657)   |
|		     |				|				|[NextHop Group Table Enhancement](https://github.com/sonic-net/SONiC/pull/1636)  |
|		     |				|				|[RESTCONF infra enhancement](https://github.com/sonic-net/SONiC/issues/1679)  |
|		     |				|				|[SAI health monitor and dump generation](https://github.com/sonic-net/SONiC/pull/1533)  |
|		     |				|				|[SONiC container upgrade to Bookworm (Debian 12)](https://github.com/sonic-net/SONiC/issues/1541)   |
|		     |				|				|[SONiC Debian Upgrade Cadence process improvement](https://github.com/sonic-net/SONiC/issues/1632)  |
|		     |				|				|[Support OpenSSL 3.0 SymCrypt provider and engine for bookworm](https://github.com/sonic-net/sonic-buildimage/pull/18088)  |
|		     |				|				|[Test Plan for OSPF and BFD](https://github.com/sonic-net/SONiC/issues/1576)   |
|		     |				|				|[Third party container management using the Sonic Application Framework](https://github.com/sonic-net/SONiC/pull/1286)  |
|		     |				|				|[TLS1.3 Support](https://github.com/sonic-net/SONiC/issues/1531)  |
|		     |				|				|[UMF Config Session Support](https://github.com/sonic-net/SONiC/pull/1518)  |
|		     |				|				|[UMF infra enhancement](https://github.com/sonic-net/SONiC/pull/1287)  |
|		     |				|				|[UMF: OpenConfig YANG support for Physical Interfaces](https://github.com/sonic-net/SONiC/pull/1628)  |
|		     |				|				|[UMF subscription enhancement](https://github.com/sonic-net/SONiC/issues/1705)  |
|		     |				|				|[UMF: Transformer Infrastructure](https://github.com/sonic-net/SONiC/pull/1287)	 |
|		     |				|				|[Upgrade FRR to 8.5.4](https://github.com/sonic-net/sonic-buildimage/pull/18669)	 |
|		     |				|				|[Upgrade SWSS/SyncD to debian 12](https://github.com/sonic-net/SONiC/pull/1670)  |
|		     |				|				|[Weighted-Cost Multi-Path](https://github.com/sonic-net/SONiC/pull/1629)   |
|SONiC.202311| 11/30/2023   |  SAI1.13.3    | [Progress Tracking](https://github.com/orgs/sonic-net/projects/14) |
|		     |				|				| [[DASH] ACL tags HLD](https://github.com/sonic-net/SONiC/blob/master/doc/dash/dash-acl-tags/dash-acl-tags.md)  |
|		  	 |				|				| AMD-Pensando ELBA SOC support |
|			 |				|				| [Auto FEC](https://github.com/sonic-net/SONiC/blob/master/doc/port_auto_neg/auto-fec.md) | 
|			 |				|				| FRR version 8.5.1 Upgrade | 
|			 |				|				| Build improvements changes |
|			 |				|				| [CMIS host management - Port signal integrity per speed](https://github.com/sonic-net/SONiC/blob/master/doc/port-si/Port_SI_Per_Speed.md) | 
|			 |				|				| [CMIS Module Management Enhancement HLD](https://github.com/sonic-net/SONiC/blob/master/doc/cmis-module-enhancement/cmis-module-enhancement.md) | 
|			 |				|				| [Container Hardening](https://github.com/sonic-net/SONiC/blob/master/doc/Container%20Hardening/SONiC_container_hardening_HLD.md) | 
|			 |				|				| [Create CMIS-custom-SI-settings.md](https://github.com/sonic-net/SONiC/blob/master/doc/sfp-cmis/CMIS-custom-SI-settings.md) | 
|			 |				|				| [Egress Sflow Enhancement](https://github.com/sonic-net/SONiC/blob/master/doc/sflow/sflow_hld.md) | 
|			 |				|				| [Factory reset](https://github.com/sonic-net/SONiC/blob/master/doc/reset_factory/ResetFactoryHLD.md) | 
|			 |				|				| [Fix containers deployments dependencies on boot/config_reload affecting user experience](https://github.com/sonic-net/SONiC/blob/master/doc/config_reload/config_reload_enhancement.md) | 
|			 |				|				| [gNMI Master Arbitration](https://github.com/sonic-net/SONiC/blob/master/doc/mgmt/gnmi/master_arbitration.md) | 
|	         |				|				| [High-level design for Wake-on-LAN feature in SONiC](https://github.com/sonic-net/SONiC/blob/master/doc/wol/Wake-on-LAN-HLD.md) | 
|			 |				|				| Libvs Port Counter Support | 
|			 |				|				| NAT Bookworm Upgrade | 
|			 |				|				| [NTP: Additional NTP configuration knobs + NTP server provisioning](https://github.com/sonic-net/SONiC/blob/master/doc/ntp/ntp-design.md) | 
|			 |				|				| PDDF System Fan Enhancement | 
|			 |				|				| PDDF support for Ufispace platforms and GPIO extension | 
|			 |				|				| Persistent DNS address across reboots | 
|			 |				|				| RADIUS NSS Vulnerability | 
|			 |				|				| [[SNMP]: SONiC SNMP Changes to support IPv6](https://github.com/sonic-net/SONiC/blob/master/doc/snmp/snmp-changes-to-support-ipv6.md) | 
|			 |				|				| [SSH global config](https://github.com/sonic-net/SONiC/blob/master/doc/ssh_config/ssh_config.md) | 
|			 |				|				| Sflow 800G Support | 
|			 |				|				| TACACS NSS Vulnerability | 
|			 |				|				| UMF: Additional Optimizations for Transformer Infrastructure | 
|			 |				|				| UMF Infra Enhancement for SONIC-YANG | 
|		     |				|				| [UMF Subscription Infra Phase 2](https://github.com/sonic-net/SONiC/blob/master/doc/mgmt/gnmi/gNMI_Subscription_for_YangData.md) | 
|			 |				|				| Upgrade hsflowd and remove dropmon build flags |
|			 |				|				| [Virtual SONiC Network Helper](https://github.com/ramakristipati/sonic-mgmt/blob/master/spytest/Doc/vsnet.md) | 			
|SONiC.202305| 05/31/2023   |  SAI1.12.0    | [Progress Tracking](https://github.com/orgs/sonic-net/projects/8) |
|			 |				|				|  ACL keys for matching BTH_opcode and AETH_syndrome |
|			 |				|				| [Auto tech support w/orchagent abort case](https://github.com/vivekrnv/SONiC/blob/cabbac08f54246dd61a1f65dec320f9a08deb721/doc/auto_techsupport/auto_techsupport_and_coredump_mgmt.md) | 
|			 |				|				| [Build Time Improvement Version Caching Support](https://github.com/sonic-net/SONiC/blob/master/doc/sonic-build-system/build-enhancements.md) | 
|			 |				|				| Chassis - execute Line card cmds from Sup remotely |
|			 |				|				| [Collecting dump during SAI failure](https://github.com/sonic-net/SONiC/blob/master/doc/SAI_failure_handling/dump_on_sai_failure.md) |
|			 |				|				| [Config Reload Enhancement](https://github.com/sonic-net/SONiC/blob/master/doc/config_reload/config_reload_enhancement.md) |
|			 |				|				| Docker migration to Bullseye |
|			 |				|				| [FIB Suppress Announcements of Routes Not Installed in HW](https://github.com/sonic-net/SONiC/blob/3ae161c4efa4ccab8443d90de3adfd4e7bfc9701/doc/BGP/BGP-supress-fib-pending.md) | 
|			 |				|				| MDIO IPC Client Library |
|			 |				|				| [PDDF FPGA Device Support](https://github.com/sonic-net/SONiC/blob/master/doc/platform/brcm_pdk_pddf.md) |
|			 |				|				| [PDDF S3IP Compliant SysFS Path Support](https://github.com/sonic-net/SONiC/blob/master/doc/platform/brcm_pdk_pddf.md) |
|			 |				|				| [PINS Generic SAI Extensions resource monitoring support](https://github.com/sonic-net/SONiC/blob/master/doc/crm/Generic_SAI_Extensions_CRM.md) |
|			 |				|				| [Port breakout feature with CMIS enabled](https://github.com/sonic-net/SONiC/blob/master/doc/dynamic-port-breakout/sonic-dynamic-port-breakout-HLD.md) |
|			 |				|				| [Preserve CoPP table during fastboot](https://github.com/sonic-net/SONiC/blob/master/doc/copp/Preserve_COPP_tables_to_improve_fast-reboot.md) | 
|			 |				|				| [Reproducible SONiC web server population script](https://github.com/sonic-net/SONiC/blob/master/doc/sonic-build-system/web_file_server_population_script.md) | 
|			 |				|				| REST Server DoS Attack Security Fix |
|			 |				|				| [rsyslog enhancements](https://github.com/iavraham/SONiC/blob/master/doc/syslog/syslog-design.md) |
|			 |				|				| [SONiC YANG RADIUS Server and RADIUS table](https://github.com/sonic-net/sonic-buildimage/blob/master/src/sonic-yang-models/doc/Configuration.md) | 
|			 |				|				| SONiC YANG Support for IPv6 Link Local |
|			 |				|				| [Standalone local clock setting](https://github.com/sonic-net/SONiC/blob/0ab39a3eaece239bbcfc23e73525c954a075096c/doc/Clock%20commands/clock_managment_hld.md) | 
|			 |				|				| [Static Route BFD HLD document](https://github.com/sonic-net/SONiC/blob/master/doc/static-route/SONiC_static_route_bfd_hld.md) |
|			 |				|				| [Switch Port Modes and VLAN CLI Enhancement](https://github.com/sonic-net/SONiC/blob/master/doc/vlan/switchport-mode-support/Switchport%20Mode%20and%20VLAN%20CLI%20Enhancement.md) |
|			 |				|				| [UMF Subscription Infra Phase 1](https://github.com/sonic-net/SONiC/blob/master/doc/mgmt/gnmi/gNMI_Subscription_for_YangData.md) |
|			 |				|				| UMF Transformer Enhancements and Optimization |
|			 |				|				| [V4/V6 L3 ACL optimization](https://github.com/sonic-net/SONiC/blob/master/doc/acl/Extend-L3V6ACLs.md) |
|			 |				|				|				  |
|SONiC.202211| 11/30/2022   |  SAI1.11.0    | [Progress Tracking](https://github.com/Azure/SONiC/wiki/Release-Progress-Tracking-202211) |
|			 |				|				| [Add syslog message rate limit configuration per container](https://github.com/sonic-net/SONiC/blob/master/doc/syslog/syslog-rate-limit-design.md) |
|			 |				|				|[Auto Neg Enhancement](https://github.com/ds952811/SONiC/blob/1cfa5041db5326c816725c487e73bfb77118c527/doc/port_auto_neg/port-auto-negotiation-design.md) |  
|			 |				|				| BRCM KNET sflow psample API compliance upgrade |
|			 |				|				|[Bulk counters](https://github.com/sonic-net/SONiC/blob/master/doc/bulk_counter/bulk_counter.md) | 
|			 |				|				| Bullseye Docker Migration - FRR, PDE, BRCM Platform, ICCPD |
|			 |				|				|[Build Time Improvement](https://github.com/sonic-net/SONiC/blob/master/doc/sonic-build-system/build-enhancements.md) | 
|			 |				|				| [General config CLI validation by YANG model](https://github.com/sonic-net/SONiC/blob/master/doc/config_yang_validation/config_db_yang_validation.md) |  
|			 |				|				| [gNMI interface for config](https://github.com/sonic-net/SONiC/blob/master/doc/mgmt/gnmi/SONiC_GNMI_Server_Interface_Design.md)  | 
|			 |				|				|[Incremental port configuration update](https://github.com/sonic-net/SONiC/blob/master/doc/port_auto_neg/port-auto-negotiation-design.md) | 
|			 |				|				|[Link Training](https://github.com/ds952811/SONiC/blob/5b8291a3c2770b84ebb1827f037c123201cb4745/doc/port_link_training/port-link-training-design.md) | 
|			 |				|				|[Make syslog log level configuration persistent](https://github.com/sonic-net/SONiC/blob/master/doc/logging/persistent_logger/persistent_loglevel.md) | 
|			 |				|				|[NPU MDIO Access Support and gbsyncd Enhancement](https://github.com/sonic-net/SONiC/blob/master/doc/gearbox/gearbox_mdio-HLD.md) | 
|			 |				|				| OSFP Transceiver monitoring |
|			 |				|				| PDDF QSFPs Low Power Mode Support | 
|			 |				|				|[PINS Generic SAI Extensions](https://github.com/sonic-net/SONiC/blob/master/doc/pins/PINS_SONiC_Design_for_SaiGenericExt.md) |
|			 |				|				|[PINS Runtime Configuration](https://github.com/sonic-net/SONiC/blob/master/doc/pins/p4rt_app_hld.md) | 
|			 |				|				| RJ-45 | 
|			 |				|				|[S3IP sysfs](https://github.com/sonic-net/SONiC/blob/f352ebfcacbaa7073c7496367d64a4b8caf1fb90/doc/s3ip_sysfs/s3ip_sysfs_hld.md) | 
|			 |				|				|[Security Secure boot](https://github.com/sonic-net/SONiC/blob/master/doc/secure_boot/hld_secure_boot.md) |
| 			 |              |               |[Security California Law](https://github.com/sonic-net/SONiC/blob/master/doc/California-SB237/California-SB237.md) |
|			 |				|				|[Setting RIF loopback action to drop](https://github.com/sonic-net/SONiC/blob/master/doc/ip-interface/loopback-action/ip-interface-loopback-action-design.md) | 
|			 |				|				|[SONiC ECMP calculator](https://github.com/sonic-net/SONiC/pull/1163) |
|			 |				|				|[SONIC YANG - VxLAN, SNMP](https://github.com/sonic-net/sonic-buildimage/blob/master/src/sonic-yang-models/doc/Configuration.md) | 
|			 |				|				|[SRv6 uSID support in SONiC dataplane - uN, uA](https://github.com/sonic-net/SONiC/blob/master/doc/srv6/SRv6_uSID.md) | 
|			 |				|				|[Structured message by streaming telemetry](https://github.com/sonic-net/SONiC/blob/9decb8c43b131fc9aeb1e28d8b55a548ae92248c/doc/event-alarm-framework/events-producer.md) | 
|			 |				|				|[Systemd bootchart integration](https://github.com/sonic-net/SONiC/blob/master/doc/profiling/sonic_bootchart.md) | 
|			 |				|				|[Syslog Source IP configuration](https://github.com/sonic-net/SONiC/blob/master/doc/syslog/syslog-design.md) |   
|			 |				|				|				  |
|SONiC.202205| 05/31/2022   | SAI1.10.2     | [Progress Tracking](https://github.com/Azure/SONiC/wiki/Release-Progress-Tracking-202205) |
|			 |				|               |[Active Active ToRs](https://github.com/sonic-net/SONiC/blob/master/doc/dualtor/active_active_hld.md) |
|			 |				|               |[Add SAI version check to SONiC build system](https://github.com/sonic-net/SONiC/blob/master/doc/sonic-build-system/saiversioncheck.md) |
|			 |				|               |[Add system date row to ‘show version’](https://github.com/sonic-net/sonic-utilities/blob/master/doc/Command-Reference.md) |
|			 |				|               |Added fan_drawer class support in PDDF |
|			 |				|               |Align crmorch with sai_object_type_get_availability  |
|			 |				|               |[CMIS Diagnostics](https://github.com/sonic-net/SONiC/blob/d1633130fa192d99eaa9cc32d9eb6087f45e64e1/doc/sfp-cmis/cmis.md)  |
|			 |				|               |Command for showing specific MAC from DB  |
|			 |				|               |[counter delay via config_db and not via systemd](https://github.com/Azure/SONiC/blob/1e5a5cdc2cd16142801b80d8cbb02eec38440fb6/doc/counters_enabling_redesign.md)  |
|			 |				|               |[Deterministic interface Link bring-up](https://github.com/sonic-net/SONiC/blob/323b161349a0c0d6d2319d66026f38536c266990/doc/sfp-cmis/Interface-Link-bring-up-sequence.md) |
|			 |				|               |[DSCP/TC remapping for tunnel traffic](https://github.com/sonic-net/SONiC/blob/master/doc/qos/tunnel_dscp_remapping.md)  |
|			 |				|               |[Dynamic Policy Based Hashing (edit flow)](https://github.com/sonic-net/SONiC/blob/master/doc/pbh/pbh-design.md)  |
|			 |				|               |[Extend auto tech support for memory threshold](https://github.com/sonic-net/SONiC/blob/master/doc/auto_techsupport_and_coredump_mgmt.md) |
|			 |				|               |FRR version update from 7.5 to 8.2  |
|			 |				|               |[Klish CLI for show-tech support](https://github.com/sonic-net/SONiC/blob/d0986fb74c0210bb4661ede3674ca2a7eb367432/doc/mgmt/SONiC%20Management%20Framework%20Show%20Techsupport%20HLD.md)  |
|			 |				|               |Migrated PDDF to Bullseye |
|			 |				|               |Move Nvidia syncd and pmon to Debian11- "Bullseye"  |
|			 |				|               |[NVGRE/GRE](https://github.com/sonic-net/SONiC/blob/master/doc/nvgre_tunnel/nvgre_tunnel.md)  |
|			 |				|               |[Password Hardening](https://github.com/sonic-net/SONiC/blob/master/doc/passw_hardening/hld_password_hardening.md) |
|			 |				|               |[PINS - Batched programming requests for higher throughput](https://github.com/sonic-net/SONiC/blob/5a5922499b388acafa85dd3c9a64520514e01946/doc/pins/batch_requests_api_hld.md)  |
|			 |				|               |Queue statistics based on queue configurations and not max  |
|			 |				|               |[Route Flow counters (based on generic counters)](https://github.com/sonic-net/SONiC/blob/master/doc/flow_counters/routes_flow_counters.md)  |
|			 |				|               |[SONiC Generic Configuration Update and Rollback](https://github.com/ghooo/SONiC/blob/c1f3f3b5427d0cafb3defd93df8b906a26fcee8a/doc/config-generic-update-rollback/SONiC_Generic_Config_Update_and_Rollback_Design.md) - Full Support |
|			 |				|               |SONIC YANG Support for KDUMP, ACL, MCLAG, BUM Storm Control  |
|			 |				|               |[Sorted next hop ECMP](https://github.com/sonic-net/SONiC/blob/master/doc/bum_storm_control/bum_storm_control_hld.md)  |
|			 |				|               |[Storm Control (BUM)](https://github.com/sonic-net/SONiC/blob/453ca2acb11ef551cd7b859705f7bf6234ad9b5f/doc/bum_storm_control/bum_storm_control_hld.md) |
|			 |				|               |[Symcrypt integration with OpenSSL](https://github.com/sonic-net/SONiC/blob/master/doc/fips/SONiC-OpenSSL-FIPS-140-3.md) |
|			 |				|               |[System Ready Enhancements](https://github.com/sonic-net/SONiC/blob/master/doc/system_health_monitoring/system-ready-HLD.md)  |
|			 |				|               |Updated PDDF kernel modules in compliance with kernel 5.10 APIs  |
|			 |				|               |Updated PDDF SFP Class with refactored SFP framework |
|			 |				|				|				  |
|SONiC.202111| 11/30/2021   |   SAI1.9.1    | [Progress Tracking](https://github.com/Azure/SONiC/wiki/Release-Progress-Tracking-202111) |
| 			 |              |               |[ACL orch redesign](https://github.com/Azure/SONiC/pull/857) |
| 			 |              |               |[App extension CLI generation tool](https://github.com/Azure/SONiC/pull/780) |
| 			 |              |               |[Automatic tech support and core dump creation](https://github.com/Azure/SONiC/pull/818) |
| 			 |              |               |[Better route scalability with multiple next-hops](https://github.com/Azure/SONiC/pull/712) | 
| 			 |              |               |[Class-Based Forwarding](https://github.com/Azure/SONiC/pull/796) |
| 			 |              |               |[CLI level authorization](https://github.com/Azure/SONiC/pull/813) |
| 			 |              |               |[DHCP support IPv6](https://github.com/Azure/SONiC/pull/787) |
| 			 |              |               |[Dynamic Policy Based Hashing](https://github.com/Azure/SONiC/pull/773) |
| 			 |              |               |[Dynamic port breakout](https://github.com/Azure/SONiC/blob/master/doc/dynamic-port-breakout/sonic-dynamic-port-breakout-HLD.md) |
| 			 |              |               |[EXP to TC QoS maps](https://github.com/Azure/SONiC/pull/844) |
| 			 |              |               |[EVPN VXLAN  for platforms using P2MP tunnel based L2 forwarding](https://github.com/Azure/SONiC/pull/806) |
| 			 |              |               |[Handle port config change on fly in xcvrd](https://github.com/Azure/SONiC/pull/839) |
| 			 |              |               |[Host interface trap counter](https://github.com/Azure/SONiC/pull/858) |
| 			 |              |               |[L2 functional and performance enhancements](https://github.com/Azure/SONiC/pull/379) | 
| 			 |              |               |[New branch creation for Debian11](https://github.com/Azure/sonic-buildimage/pull/8191) |
| 			 |              |               |[One line command to extract multiple DBs info of a SONiC component - Debug dump utility](https://github.com/Azure/SONiC/pull/789) |
| 			 |              |               |[Overlay ECMP](https://github.com/Azure/SONiC/pull/861) |
| 			 |              |               |[Overlay ECMP - BFD offload](https://github.com/Azure/SONiC/pull/880) |
| 			 |              |               |[PDK - Platform Development Environment](https://github.com/Azure/SONiC/blob/master/doc/platform/pde.md) | 
| 			 |              |               |[PINS (P4 Integrated Network Stack)](https://github.com/Azure/SONiC/issues/841) | 
| 			 |              |               |[Reclaim reserved buffer for unused ports](https://github.com/Azure/SONiC/pull/831) |
| 			 |              |               |[Routed sub-interface naming convention](https://github.com/Azure/SONiC/pull/833) |
| 			 |              |               |[SONiC for MPLS Dataplane](https://github.com/Azure/SONiC/pull/706) | 
|			 |				|               |[SONiC Generic Configuration Update and Rollback](https://github.com/ghooo/SONiC/blob/c1f3f3b5427d0cafb3defd93df8b906a26fcee8a/doc/config-generic-update-rollback/SONiC_Generic_Config_Update_and_Rollback_Design.md) - Preliminary Support |
| 			 |              |               |[SRv6 support (Cntd)](https://github.com/Azure/SONiC/pull/795) |
| 			 |              |               |Support for passing IS-IS, LDP and MicroBFD packets to CPU |
| 			 |              |               |[Upgrade  SONiC init flow](https://github.com/Azure/SONiC/pull/871) |
| 			 |              |               |VXLAN src port configuration |
|			 |				|				|				  |
|SONiC.202106| 06/30/2021   |    SAI1.8.1   | [Progress Tracking](https://github.com/Azure/SONiC/wiki/Release-Progress-Tracking-202106), [Release Note](https://github.com/Azure/SONiC/blob/master/doc/SONiC_202106_Release_Notes.md) |  |
| 			 |              |               |  Add FRR running configuration to tech support |
| 			 |              |               | [Broadcom silicon common config](https://github.com/Azure/SONiC/pull/699) |
| 			 |              |               | [Dynamic policy based hashing](https://github.com/Azure/SONiC/blob/6af2959ee5829f801409fc833389e78802d5258a/doc/pbh/pbh-design.md) | 
| 			 |              |               | [Enable/Disable auto negotiation and speed setting with number of lanes](https://github.com/Azure/SONiC/blob/9b58ef06ab49b489e3aed287659100ce7be8c76a/doc/port_auto_neg/port-auto-negotiation-design.md#cli-enhancements)| 
| 			 |              |               |  Error handling (swss) | 
| 			 |              |               | [Inband mgmt VRF](https://github.com/venkatmahalingam/SONiC/blob/7781c097a92d9fbac3fc2fe2f8c6ce175839f473/doc/vrf/SONiC_in_band_mgmt_via_mgmt_Vrf_HLD.md) |
| 			 |              |               | [IPv6 Link Local and BGP Unnumbered](https://github.com/Azure/SONiC/pull/625) |
| 			 |              |               | [MC-LAG (L2)](https://github.com/Azure/SONiC/pull/596) |
| 			 |              |               | [PCIe Monitoring](https://github.com/Azure/SONiC/pull/634) |
| 			 |              |               | [PDK - Platform Development Environment](https://github.com/Azure/SONiC/blob/master/doc/platform/pde.md) | 
| 			 |              |               | [RADIUS AAA](https://github.com/Azure/SONiC/pull/500) | 
| 			 |              |               | [SONiC for MPLS Dataplane](https://github.com/Azure/SONiC/blob/364fcae0438ed583270b56319dcfcb91e20b918a/doc/mpls/MPLS_hld.md) |
| 			 |              |               | Telemetry for Multi-ASIC |
| 			 |              |               | [TPID config support](https://github.com/Azure/SONiC/pull/681) |
| 			 |              |               | [Enhanced xcrvd SFP error flow HLD](https://github.com/Azure/SONiC/pull/586) |
| 			 |              |               | [Entity sensor MIB extension](https://github.com/Azure/SONiC/pull/766)  |
|			 |				|				|				  |
|SONiC.202012| 12/31/2020   |    SAI1.7.1   | [Progress Tracking](https://github.com/Azure/SONiC/wiki/Release-Progress-Tracking-202012), [Release Note](https://github.com/Azure/SONiC/blob/master/doc/SONiC_202012_Release_Notes.md) |
|            |              |               | [Consistent ECMP support (fine grain ECMP)](https://github.com/anish-n/SONiC/blob/e5cdb3d9337026a98d6be5d558126926a4e959e4/doc/ecmp/fine_grained_next_hop_hld.md) |
|            |              |               | Console Support for SONiC (Hardware)|
|            |              |               | Console Support for SONiC (SSH forwarding)|
|            |              |               | Container warm restart (BGP/TeamD/SWSS/SyncD) |
|            |              |               | [CoPP Config/Management](https://github.com/Azure/SONiC/blob/262e2581c3360e971c370e347c608d081d7e1c49/doc/copp/CoPP%20Config%20and%20Management.md) |
|            |              |               | [Distributed forwarding in a VOQ architecture HLD](https://github.com/Azure/SONiC/blob/e607a9f3e8e0cc77687acf7913b559210804cc65/doc/chassis/system-ports.md) |
|            |              |               | [Dynamic headroom calculation](https://github.com/Azure/SONiC/blob/415f19931bccd900ac528b100aafffa6000e82e9/doc/qos/dynamically-headroom-calculation.md)               |
|            |              |               | [Enable synchornous SAI APIs (error handling)](https://github.com/shi-su/SONiC/blob/61762c8e709ead5f8ee7df83facea6ceee9de6f5/doc/synchronous-mode/synchronous-mode-cfg.md)|
|            |              |               | [EVPN/VXLAN](https://github.com/Azure/SONiC/blob/7fbda34ee3315960c164a0c202f39c2ec515cfc3/doc/vxlan/EVPN/EVPN_VXLAN_HLD.md) |
|            |              |               | [FRR BGP NBI](https://github.com/Azure/SONiC/blob/48e9012c548528b6528745bda9d75b4164e785eb/doc/mgmt/SONiC_Design_Doc_Unified_FRR_Mgmt_Interface.md) |
|            |              |               | [Gearbox](https://github.com/Azure/SONiC/blob/master/doc/gearbox/gearbox_mgr_design.md) |
|            |              |               | [Kubernetes (docker to be controlled by Kubernetes)](https://github.com/renukamanavalan/SONiC/blob/kube_systemd/doc/kubernetes/Kubernetes-support.md) |
|            |              |               | Management Framework (Phase 2) |
|            |              |               | Merge common lib for C++ and python (SWSS common lib)  |
|            |              |               | Move from Python2->python3 |
|            |              |               | [Multi-ASIC](https://github.com/Azure/SONiC/blob/ebe4f4b695af5d2dbd23756d3cff03aef0a0c880/doc/multi_asic/SONiC_multi_asic_hld.md) |
|            |              |               | Multi-DB enhancement-Part 2 |
|            |              |               | ONIE FW tools CPLD, BIOS, SSD, Firmware upgrade [Uniform Tool] |
|            |              |               | [PDDF advance to SONiC Platform 2.0, BMC](https://github.com/Azure/SONiC/blob/master/doc/platform/brcm_pdk_pddf.md) |
|            |              |               | [SONiC entity MIB extensions](https://github.com/Azure/SONiC/blob/0e53548a8f1023d1be2a1dffd62737c7a1b18a2e/doc/snmp/extension-to-physical-entity-mib.md) |
|            |              |               | [Support hardware reboot/reload reason (Streaming Telemetry)](https://github.com/sujinmkang/SONiC/blob/6ed19e88c6f7aac74640d3d343210d840af70a23/doc/system-telemetry/reboot-cause.md)|
|            |              |               | [System health and system LED](https://github.com/Azure/SONiC/blob/master/doc/system_health_monitoring/system-health-HLD.md) |
|			 |				|				|				  |
|SONiC.202006| 06/30/2020   |    SAI1.6.3   | [Progress Tracking](https://github.com/Azure/SONiC/wiki/Release-Progress-Tracking-202006), [Release Note](https://github.com/Azure/SONiC/blob/master/doc/SONiC_202006_Release_Notes.md) |
|            |              |               | Build Improvements |
|            |              |               | Bulk API for route |
|            |              |               | [D-Bus to Host Communications](https://github.com/Azure/SONiC/pull/541/files#diff-0fe927c97d0445fd919a2316bd0c5aa7) |
|            |              |               | Debian 10 upgrade, base image,driver |
|            |              |               | [Dynamic port break](https://github.com/Azure/SONiC/blob/master/doc/dynamic-port-breakout/sonic-dynamic-port-breakout-HLD.md) |
|            |              |               | [Egress shaping (port, queue)](https://github.com/Azure/SONiC/pull/535) |
|            |              |               | [FW utils extension: SSD upgrade](https://github.com/Azure/SONiC/blob/master/doc/fwutil/fwutil.md) |
|            |              |               | Getting docker ready for Debian 10 |
|            |              |               | Platform APIs move to new APIs * - Continuation |
|            |              |               | [Port Mirroring](https://github.com/Azure/SONiC/pull/580) |
|            |              |               | Porting mVRF support to Debian 10  |
|            |              |               | [Proxy ARP](https://github.com/Azure/SONiC/pull/579/files#diff-27f0a7d1396a80ae9bb361e779f14e8c) |
|            |              |               | Pytest 100% moved from ansible to Pytest |
|            |              |               | SPytest |
|            |              |               | [Thermal control](https://github.com/Azure/SONiC/blob/master/thermal-control-design.md) |
|			 |				|				|				  |
|SONiC.201911| 10/30/2019   |   1.5         |  [Progress Tracking](https://github.com/Azure/SONiC/wiki/Release-Progress-Tracking-201911) &nbsp;&nbsp; &nbsp;&nbsp; [Release Notes](https://github.com/Azure/SONiC/blob/master/doc/SONiC_201911_Release_Notes.md)  |
|            |              |               | [ZTP - design review in progress](https://github.com/Azure/SONiC/blob/master/doc/ztp/ztp.md)      |
|            |              |               | [Mgmt VRF](https://github.com/Azure/sonic-utilities/pull/463/commits/d6d14929ef1f1d27f92e4bb5db30fba8b39dcfd4)      |
|            |              |               | [sFlow](https://github.com/Azure/SONiC/pull/389)      |
|            |              |               | [L3 perf enhancement](https://github.com/Azure/SONiC/pull/399) |
|            |              |               | [VRF](https://github.com/Azure/SONiC/blob/master/doc/vrf/sonic-vrf-hld.md) |
|            |              |               | Platform test                                                |
|            |              |               | [SSD diagnostic<br/>tolling](https://github.com/Azure/SONiC/pull/378) |
|            |              |               | [Management<br/>Framework](https://github.com/Azure/SONiC/pull/436) |
|            |              |               | [Multi-DB optimization-Part 1](https://github.com/Azure/SONiC/blob/master/doc/database/multi_database_instances.md) |
|            |              |               | [Sub-port support](https://github.com/Azure/SONiC/pull/420)  |
|            |              |               | [Build time<br/>improvements](https://github.com/Azure/SONiC/pull/419) |
|            |              |               | [Egress mirroring and<br/>ACL action support check via SAI](https://github.com/Azure/SONiC/pull/411) |
|            |              |               | [Configurable<br/>drop counters](https://github.com/Azure/SONiC/pull/434) |
|            |              |               | [Log analyzer to pytest](https://github.com/Azure/SONiC/pull/421) |
|            |              |               | [HW resource monitor](https://github.com/Azure/SONiC/pull/439) |
|            |              |               | [NAT](https://github.com/Azure/SONiC/pull/390) |
|            |              |               | ONIE FW tools - bios & cpld|
|			 |		        |			    |				  |
|SONiC.201904| 04/30/2019   |   1.4         | [Release Note](https://github.com/Azure/SONiC/blob/master/doc/SONiC%20201904%20Release%20Notes.md )                                  |
|            |              |               | FRR as default routing stack      |
|            |              |               | Upgrade each docker to stretch version   |
|            |              |               | Upgrade docker engine to 18.09    |
|            |              |               | [Everflow V2 - IPV4/IPv6 Portion 2.0](https://github.com/Azure/SONiC/blob/bb4f4a3a85935a38ec7f9625ef62cbe58c0998b4/doc/SONiC_EVERFLOW_IPv6.pdf)              |
|            |              |               | [Egress ACL bug fix and ACL CLI enhancement](https://github.com/Azure/SONiC/blob/dfa7e58292deb4d7b10d1e0ca73f296cd206e9d2/doc/acl/egress-acl-bug-fix-description.md)|
|            |              |               | [L3 RIF counter support](https://github.com/Azure/SONiC/pull/310 ) |
|            |              |               | [PMon Refactoring](https://github.com/Azure/SONiC/tree/master/doc/pmon)|
|            |              |               | BGP-EVPN support(type 5), (related HLD [Fpmsyncd](https://github.com/Azure/SONiC/pull/375),[Vxlanmgr](https://github.com/Azure/SONiC/pull/369),[template](https://github.com/Azure/sonic-buildimage/pull/2838/files))  |
|            |              |               | [Transceiver parameter tuning](https://github.com/Azure/SONiC/pull/328/files) PR pending on CR sign off|
| 			 |              |               |                 |
|SONiC.201811| 11/30/18     | 1.3           | [Release Note](https://github.com/Azure/SONiC/blob/master/doc/SONiC%20201811%20Release%20Note.pdf)                                   |
|            |              |               | [Debian Kernel Upgrade to 4.9](https://github.com/Azure/SONiC/wiki/Upgrading-SONiC-kernel-to-3.16.0‐5-or-later-versions)       |
|            |              |               | [Warm Reboot](https://github.com/Azure/SONiC/pull/187) |
|            |              |               | [Incremental Config (IP, LAG, Port shut/unshut)](https://github.com/Azure/SONiC/blob/7ae7106fd3106cfc9a6a60a81d3b8f5ebd9ebab5/doc/Incremental%20IP%20LAG%20Update.md)|
|            |              |               | [Asymmetric PFC](https://github.com/Azure/SONiC/wiki/Asymmetric-PFC-High-Level-Design)|
|            |              |               | [PFC Watermark](https://github.com/Azure/SONiC/blob/master/doc/watermarks_HLD.md) |
|            |              |               | [Routing Stack Graceful Restart](https://github.com/Azure/SONiC/blob/dcac72377f23521a394694214678ea4450f6f70a/doc/routing-warm-reboot/Routing_Warm_Reboot.md)|
|            |              |               | [Basic VRF and L3 VXLAN](https://github.com/Azure/SONiC/blob/master/doc/vxlan/Vxlan_hld.md)             |
| 			 |              |               |                 |
|SONiC.201807| 07/30/18     | 1.3           |                 |
|            |              |               | [gRPC](https://github.com/Azure/SONiC/pull/207)|
|            |              |               | [Dtel support](https://github.com/Azure/SONiC/pull/182)|
|            |              |               | SONiC Architecture and User Manual (Documentation)| 
|            |              |               | [Sensor transceiver monitoring](https://github.com/Azure/SONiC/pull/202)|
|            |              |               |LLDP extended MIB: lldpremtable, lldplocporttable, lldpremmanaddrtable, lldplocmanaddrtable, lldplocporttable, lldpLocalSystemData|
| 			 |              |               |                 |
|SONiC.20180 | 03/15/18     | 1.2           |                                    |
|            |              |               | [Critical Resource Monitoring](https://github.com/Azure/SONiC/wiki/Critical-Resource-Monitoring-High-Level-Design)       |
|            |              |               | MAC Aging                          |
|            |              |               | [IPv6 ACL](https://github.com/Azure/SONiC/blob/gh-pages/doc/ACL-enhancements-on-SONIC.docx) |
|            |              |               | [BGP/Neighbor-down fib-accelerate](https://github.com/Azure/SONiC/blob/gh-pages/doc/sonic-ecmp-acceleration.docx)   |
|            |              |               | [PFC WD](https://github.com/Azure/SONiC/wiki/PFC-Watchdog-Design)                             |
| 			 |              |               |                 |
|SONiC.201712| 12/15/2017   | 1.0           | Fast Reload                        |
|            |              |               | SONiC Support SAI 1.0              |
|            |              |               | TACACS+                            |
|            |              |               | LACP Fallback                      |
|            |              |               | MTU Setting                        |
|            |              |               | Vlan Trunk                         |
|            |              |               | Static Port breakout<sup>1<sup>    |
|            |              |               | Dynamic ACL Upgrade                |
|            |              |               | SWSS Unit Test Framework           |
|            |              |               | CobfigDB framework                 |
| 			 |              |               |                 |
|SONiC.201709| 9/15/2017    | 0.9.4         | VLAN                               |
|            |              |               | ACL permit/deny                    |
|            |              |               | IPv6                               |
|            |              |               | Tunnel Decap                       |
|            |              |               | Mirroring                          |
|            |              |               | Post Speed Setting                 |
|            |              |               | BGP Graceful restart helper        |
|            |              |               | BGP MP                             |
| 			 |              |               |                 |
|SONiC.201705| 5/15/2017    | 0.9.4         | BGP                                |
|            |              |               | ECMP                               |
|            |              |               | LAG                                |
|            |              |               | LLDP                               |
|            |              |               | QoS - ECN                          |
|            |              |               | QoS - RDMA                         |
|            |              |               | Priority Flow Control              |
|            |              |               | WRED                               |
|            |              |               | COS                                |
|            |              |               | SNMP                               |
|            |              |               | Syslog                             |
|            |              |               | Sysdump                            |
|            |              |               | NTP                                |
|            |              |               | COPP                               |
|            |              |               | DHCP Relay Agent                   |
|            |              |               | SONiC to SONiC upgrade             |
|            |              |               | Multiple Images support            |
|            |              |               | One Image                          |
| 			 |              |               |                 |
| Backlog    |              |               |                 |
| 			 |              |				| 400G DR support - Deferred from 202205 release |
| 			 |              |				| 400G ZR optics performance monitoring  - Deferred from 202305 release | 
|          	 |              |               | [AAA improvement ](https://github.com/Azure/SONiC/blob/a46aa68b3a3ca57fea28c3d139fcef437e0cf0e6/doc/aaa/AAA20Improvements/AAA%20Improvements.md) |
| 			 |              |               | ACL enhancements: Policing, DHCP/PCP remark, L2 |
| 			 |              |               | ACL UDF |
| 			 |              |				| ACMS and Restful API for Arista 7060 - Deferred from 202205 release |
|		     |				|				|[[Logrotate] Add logrotate feature HLD](https://github.com/sonic-net/SONiC/pull/1683) |
|		     |				|				|[Adding the HLD for SONiC reset local users' passwords](https://github.com/sonic-net/SONiC/pull/1577) |
|			 |				|				| Add SNMP view to filter MIB browsing - Deferred from 202305 release | 
| 			 |              |				| Add new YANG models for IS-IS/SR/MPLS configs and telemetry - Deferred from 202305 release | 
| 			 |              |				| Add PIT HLD document , this PR replace previous [PR#1014](https://github.com/sonic-net/SONiC/pull/1014) - Deferred from 202305 release | 
| 			 |              |				| Adding IS-IS and SR/MPLS from FRR - Deferred from 202305 release |
| 			 |              |               | Align crmorch with sai_object_type_get_availability |
| 			 |              |               | ARP Refresh |
| 			 |              |               | App extension with warmboot awareness |
| 			 |              |               | App extension with Orchagent/SWSS |
|			 |				|				| ASIC Firmware update mechanism - Deferred from 202305 release | 
|		     |			    | 				| [BGP Add Path](https://tools.ietf.org/rfc/rfc7911.txt) |
|			 |				|				| BGP config incremental update - Deferred from 202205 release	| 
|		     |			    | 				| [BGP ExtComm](https://tools.ietf.org/rfc/rfc4360.txt) |
|		     |			    | 				| [BGP Link bandwidth ExtComm](https://tools.ietf.org/pdf/draft-ietf-idr-link-bandwidth-07.pdf) |
|		     |				|				|[BGP Loading Optimization HLD](https://github.com/sonic-net/SONiC/pull/1521) |
|		     |				|				|[BGP PIC HLD](https://github.com/sonic-net/SONiC/pull/1493) |
|		     |				|				|[BGP route aggregation with BBR awareness](https://github.com/sonic-net/SONiC/issues/1731) |
|			 |				|				| BGP Unnumbered config_db knobs - Deferred from 202211 release |
|            |              |               | [BFD SW 100ms interval from FRR](https://github.com/Azure/SONiC/blob/master/doc/bfd/BFD_Enhancement_HLD.md)| 
|			 |				|				| [Chassis infrastructure, T2 topologies and sample Testcases converted](https://github.com/Azure/sonic-mgmt/blob/master/ansible/library/multi-asic_aware_module_requirements.md) |
| 			 |              |               | [CMIS Diagnostics](https://github.com/Azure/SONiC/blob/d1633130fa192d99eaa9cc32d9eb6087f45e64e1/doc/sfp-cmis/cmis.md) |
| 			 |              |				| Config Reload Enhancement: Introduce the Transaction Mechanism - Deferred from 202205 release | 
|			 |				|				| ConfigDB 100% YANG model - Deferred from 202305 release | 
| 			 |              |               | [CPU Queues](https://github.com/Azure/SONiC/pull/743) |
| 			 |              |				| DASH Infra - Deferred from 202305 release | 
|            |              |             	| DASH – SAI PTF extension for SmartNIC - Deferred from 202205 release |
| 			 |              |               | [Distributed VOQ architecture HLD](https://github.com/Azure/SONiC/blob/a9b221e3252e5ef3a45d18f615c23d3794f39a5b/doc/voq/voq_hld.md)
| 			 |              |				| Debug Port Data - Deferred from 202305 release | 
| 			 |              |               | Deprecating Python2 platform daemons - Deferred from 202205 release |
|			 |				|				| Default value from SONiC YANG for configuration - Deferred from 202211 release |  
| 			 |              |               | DHCP relay IPv6 support |
|			 |				|				| DHCPv4 refactoring - Deferred from 202211 release |
| 			 |              |				| Docker image on Bulleyes - Deferred from 202205 release |
| 			 |              |               | DPB Reconcile |
|		     |				|				|[DSCP inner marking with IP-in-IP](https://github.com/sonic-net/SONiC/issues/1734) |
| 			 |              |               | Dynamic CoPP reconcile | 
|			 |				|				| Dynamic Load Balancing (DLB) - Deferred from 202211 release | 
|			 |				|				| ECMP and LAG hashing and IP fields - Deferred from 202211 release |
| 			 |              |				| ECN and WRED statistics - Deferred from 202305 release | 
| 			 |              |               | Enabling IS-IS in the dataplane |
|            |              |               | Extending Entphysicaltable MIB table |
|            |              |               | Extend FW debug info in sysdump |
|		     |				|				|[Expand docker manifest capabilities to include network and ports configuration](https://github.com/sonic-net/SONiC/pull/1601) |
|		     |				|				|[Extend sysmonitor functionality to wait for host daemons](https://github.com/sonic-net/SONiC/issues/1756) |
|			 |				|				| Extended TeamD expire timer - Deferred from 202211 release | 
| 			 |              |               | [Event-mgmt Infra](https://github.com/Azure/SONiC/pull/761) - Deferred from 202205 release |
| 			 |              |               | [Everflow Support on VOQ Chassis](https://github.com/Azure/SONiC/blob/9c08b2f3f77230017c7035ceaf880746cb590d49/doc/voq/everflow.md) |
| 			 |              |				| EVPN-MH Phase #1 - Deferred from 202205 release | 
| 			 |              |               | [Fabric Port support for SONiC](https://github.com/Azure/SONiC/blob/2e1f699a3ba1dbf88abeecb192f6bb5e390b8b8a/doc/chassis/fabric.md) |
|		     |				|				|[FEC Histogram](https://github.com/sonic-net/SONiC/issues/1736) |
|            |              |               | Flow-based Services (incl. packet DSCP remark) |
|			 |				|				| Firmware upgrade infra - Deferred from 202211 release | 
|		     |				|				|[Fpmsyncd Next Hop Table Enhancement HLD](https://github.com/sonic-net/SONiC/pull/1425) |
| 			 |              |				| Further extensions and uses of application extension framework | 
| 			 |              |               | Gearbox part 2 |
| 			 |              |               | Generic counters (Flow counters) |
| 			 |              |				| Generic Hash - ECMP and LAG hashing and IP fields - Deferred from 202305 release |
| 			 |              |				| Global setting to allow IPv6 link-local neighbours to always be programmed | 
| 			 |              |				| gNMI: Save-On-Set - Deferred from 202305 release | 
|		     |				|				|[Graceful SAI failure handling w/o orchagent crash](https://github.com/sonic-net/SONiC/issues/1733) |
| 			 |              |				| HLD for changing teamd expiry timer - Deferred from 202305 release | 
|		     |				|				|[HLD for ECN and WRED statistics support in SONiC](https://github.com/sonic-net/SONiC/pull/1273) |
|		     |				|				|[HLD for Memory_Statistics](https://github.com/sonic-net/SONiC/pull/1760) |
| 			 |              |				| IEEE 802.1s – Multiple Spanning Tree Support - Deferred from 202305 release |
| 			 |              |               | [Inband port support for Chassis](https://github.com/Azure/SONiC/pull/639) |
|		     |				|				|[IPM: IP Measurements](https://github.com/sonic-net/SONiC/issues/1715) |
|		     |				|				|[IPMC dataplane](https://github.com/sonic-net/SONiC/issues/1728) |
|			 |				|				| IPSec on vSwitch - Deferred from 202211 release |
|			 |				|				| IS-IS and OSPF routing support - Deferred from 202305 release |
|		     |				|				|[Kdump Remote SSH Config Enhancements](https://github.com/sonic-net/SONiC/issues/1711) |
| 			 |              |               | [Kernel programming performance enhancement](https://github.com/Azure/SONiC/pull/493) |
| 			 |              |               | [Klish CLI for show-tech support](https://github.com/Azure/SONiC/blob/d0986fb74c0210bb4661ede3674ca2a7eb367432/doc/mgmt/SONiC%20Management%20Framework%20Show%20Techsupport%20HLD.md)  |
| 			 |              |               | Kubernetes enhancements |
| 			 |              |               | [LAG Support for Chassis](https://github.com/Azure/SONiC/blob/332ca53d938e0df24c78d76bcf1117d896ed2683/doc/voq/lag_hld.md)
|            |              |               | L2 Dot1Q tunneling support |
| 			 |              |               | libebpf support and usage |
|			 |				|				| Link and node path protection - Deferred from 202305 release |
| 			 |              |				| Link Event Damping - Deferred from 202305 release | 
| 			 |              |               | [MACSec support in Chassis](https://github.com/Pterosaur/SONiC/blob/fdbaa116fdc4579c67974e70efcce3c882801fcf/doc/macsec/MACsec_hld.md) |
| 			 |              |               | MACSEC enhancement: primary & fallback case - Deferred from 202205 release |
| 			 |              |				| MacSec  fallback key  support - Deferred from 202305 release |
|            |              |               | [Management Framework RBAC](https://github.com/Azure/SONiC/blob/48fab9db4f090c5beaea5f7a8fdcb9474d23a4e9/doc/aaa/SONiC%20RBAC.md) | 
|            |              |               | [Media Enhancements<br>(Media Information & Settings)](https://github.com/Azure/SONiC/blob/a6e9636552149829e39a82705d1ad2b48a17b3f0/doc/media-info-enhancements/media-info.md) | 
|		     |				|				|[Merged EVPN VxLAN MH HLD from Cisco and BCM](https://github.com/sonic-net/SONiC/pull/1702) |
|		     |				|				|[Mitigating DHCP Starvation Attacks](https://github.com/sonic-net/SONiC/issues/1575) | 
| 			 |              |               | Mgmt FW Phase 3 |
| 			 |              |				| MPLS scalability enhancement in SAI and SWSS | 
| 			 |              |               | MultiDB reconcile |
|		     |				|				|[Multiple Spanning Tree Protocol (MSTP) Updated HLD](https://github.com/sonic-net/SONiC/issues/1775) |
|			 |				|				| MMU incremental config update - Deferred from 202211 release|
|			 |				|				| Neighbor Enhancement - Nbrmgrd ARP refresh for router port - Deferred from 202211 release |  
| 			 |              |				| Neigh refresh - Deferred from 202305 release |
|		     |				|				|[Notification to SAI that fast-reboot is done](https://github.com/sonic-net/SONiC/issues/1755) |
| 			 |              |               | [NVGRE/GRE](https://github.com/Azure/SONiC/pull/869) | 
|			 |				|				| Operator security profile - Deferred from 202305 release |
| 			 |              |				| P4 Runtime State Cache - Deferred from 202305 release | 
| 			 |              |				| P4-CLI - Deferred from 202305 release | 
| 			 |              |				| PINS Generic SAI Extensions - Cross Referencing of dynamic PINS Extensions objects with SAI objects - Deferred from 202305 release | 
| 			 |              |               | [Platform Monitoring for Chassis systems](https://github.com/Azure/SONiC/blob/4206c5420c4b63f1d2ec40b10d54adb27fc9d42a/doc/pmon/pmon-chassis-design.md)
|			 |				|				|[Platform Integration Test, aka. PIT](https://github.com/sonic-net/SONiC/blob/4c5192665dbb4a4a7c1a1d138db2f7772fbf38b4/doc/pit/Platform_Integration_Test_high_level_design.md)  - Deferred from 202211 release |  
| 			 |              |				| PINS enhancement | 
|			 |				|				|[PINS GE Netlink](https://github.com/sonic-net/SONiC/blob/d84acffa39f9481a4657bd08d08fb56812ad937b/doc/pins/Packet_io.md) - Deferred from 202211 release |
|            |              |      			| PINS SAI.P4 enhancements for Layer2 support and VxLAN - Deferred from 202205 release | 
| 			 |              |				| P-NAC (Port based Network Access Control) - Deferred from 202305 release |
|			 |				|				| Port auto-negotiation status - Deferred from 202305 release | 
| 			 |              |				| Port Init Profile (Port Bulk) - Deferred from 202305 release | 
|			 |				|				| Port-security - Deferred from 202211 release | 
|			 |				|				| [Port bulk support](https://github.com/sonic-net/SONiC/blob/master/doc/port-profile-init/port-profile-init-design.md) - Deferred from 202211 release | 
|		     |				|				|[Power over Ethernet (PoE)](https://github.com/sonic-net/SONiC/issues/1539) |
|			 |				|				| Python 3.0 upgrade for testbed - Deferred from 202305 release |  
|			 |				|				| Qumram-MX support - Deferred from 202305 release | 
|			 |				|				| Reproducible SONiC web server population script <br> [HLD](https://github.com/orenreiss/SONiC/blob/7ed5fe4ac08c70fc2dbfd770264f6601f4be9732/doc/sonic-build-system/web_file_server_population_script.md) - Deferred from 202211 release | 
|		     |				|				|[Reset user password upon long press on reset button](https://github.com/sonic-net/SONiC/issues/1545) | 
| 			 |              |               | [Routing/BGP for Chassis](https://github.com/Azure/SONiC/blob/35d6f8d1a88a8f8b08237d6ec9f719e9c06a6758/doc/voq/bgp_voq_chassis.md)
| 			 |              |               | Routed sub-interface reconcile | 
| 			 |              |               | [RPVST+](https://github.com/Azure/SONiC/pull/499) |
| 			 |              |               | Sample Rate on mirror	|
| 			 |              |               | Segment Routing support in SONiC | 
|			 |				|				| [Security Secure upgrade](https://github.com/sonic-net/SONiC/blob/master/doc/secure_upgrade/secure_upgrade.md) - Deferred from 202211 release |
| 			 |              |               | Sflow with remote collector |
| 			 |              |               | [Show running enhancement](https://github.com/Azure/SONiC/pull/838) |  
| 			 |              |               | SNMPd Enhancements - Deferred from 202205 release |
| 			 |              |				| Secure upgrade v2 - Deferred from 202305 release | 
|            |              |               | SONiC shared headroom - enhanced configuration | 
| 			 |              |				| SONiC management repo  Python3 compliance | 
|            |              |               | SONiC new polling counters for counters which has extend CPU req.|
|          	 |              |               | SONiC app extension (w/o orchagent)|
| 			 |              |               | SONiC fanout support - Deferred from 202205 release |
| 			 |              |               | SONiC IPSEC support |
| 			 |              |               | SONiC NAT Scaling |
| 			 |              |				| SONiC Port Access Control - Deferred from 202305 release | 
|		     |				|				|[SONiC Security Auditing HLD](https://github.com/sonic-net/SONiC/pull/1713) |
| 			 |              |				| SONiC Static Port Channel Support - Deferred from 202305 release | 
|            |              |             	| SONiC with P4 DPDK (PNA architecture) – Basic SoftSwitch with DPDK - Deferred from 202205 release | 
| 			 |              |               | 100% SONiC YANG model | 
|			 |				|				| StateDB on YANG model - Deferred from 202211 release	|  
| 			 |              |               | Static Anycast Gateway |
| 			 |				|				| [Static LAG Support](https://github.com/sonic-net/SONiC/blob/6e36529f92ad54ee950a14a5d0fc391086771f5d/doc/lag/Static%20Port%20Channel%20Design%20Document.md) - Deferred from 202211 release |
| 			 |              |               | [Storm Control (BUM)](https://github.com/Azure/SONiC/blob/453ca2acb11ef551cd7b859705f7bf6234ad9b5f/doc/bum_storm_control/bum_storm_control_hld.md) |
| 			 |              |               | STP/PVST |
| 			 |              |				| Streaming Telemetry support for Syslog - Deferred from 202205 release | 
|			 |				|				| SR-MPLS support - Deferred from 202305 release |
| 			 |              |				| SRv6 Orchagent support for FRR integration in SONiC - Deferred from 202305 release | 
|            |              |             	| SRv6 policy steering w/ FRR protocols integration - Deferred from 202205 release |
|            |              |             	| SRv6 sBFD, DT46 - Deferred from 202205 release |
| 			 |              |				| SRv6 VPN - Deferred from 202305 release | 
|		     |				|				|[SRv6 VPN HLD for 202305 release](https://github.com/sonic-net/SONiC/pull/1252) |
| 			 |              |				| Static Anycast Gateway HLD - Deferred from 202305 release | 
|			 |				|				| [Support PCEP](pathd daemon from FRR) and BFD protocols - Deferred from 202305 release | 
|		     |				|				|[Support SSD cleanup](https://github.com/sonic-net/SONiC/issues/1529) |
|			 |				|				|[Switch Port Modes and VLAN CLI Enhancement](https://github.com/sonic-net/SONiC/blob/ab74bb25dc6afe6d39581c609bdbd0ce6f09f732/doc/L2_802.1q_Tunneling_Support_HLD/L2%20dot1q%20HLD.markdown) - Deferred from 202211 release |  
| 			 |              |				| SWSS App State DB and Redis performance - Deferred from 202305 release | 
| 			 |              |               | [System Ready Enhancements](https://github.com/Azure/SONiC/pull/875/files) |
| 			 |              |               | [System with zero port support](https://github.com/Azure/SONiC/pull/900) - Deferred from 202205 release |
| 			 |              |               | TDR support for 1G Cu SFP |
|			 |				|				| Teamd warm-restart - Deferred from 202211 release |  
|			 |				|				| Testbed v2 scale out - Deferred from 202211 release | 
| 			 |              |               | Testcase/Testbed Infrastructure |
| 			 |              |               | Telemetry for Chassis |
| 			 |              |               | Telemetry for BGP | 
| 			 |              |               | (Test) Testbed v2 |
| 			 |              |               | (Test) Upgrade to Python3 compliance |
| 			 |              |               | (Test) Ansible 2.10 upgrade | 
| 			 |              |				| Third Party Container Management - Deferred from 202305 release | 
| 			 |              |               | [Thresholds (statistics)](https://github.com/Azure/SONiC/blob/master/doc/threshold/SONiC%20Threshold%20feature%20spec.md) |
|			 |				|				| Traffic Management - Deferred from 202305 release | 
|		     |				|				|[UEFI key management in SONiC to perform secure boot key rotation, update, remove revoke etc](https://github.com/sonic-net/SONiC/issues/1401) |
| 			 |              |               | UI Content (UMF client) | 
| 			 |              |				| UMF DB Access Layer Enhancement - Deferred from 202305 release | 
| 			 |              |				| UMF Translib API Enhancement - Deferred from 202305 release | 
| 			 |              |				| Uploading logs to remote syslog server - Deferred from 202305 release | 
| 			 |              |				| User Management (RBAC) - Deferred from 202305 release | 
|			 |				|				| UMF Management Infra Enhancement - Deferred from 202305 release | 
|			 |				|				| vlan management improvement - Deferred from 202305 release | 
| 			 |              |				| VLAN Stacking - Deferred from 202205 release | 
|            |              |               | VoQ Chassis Support in SONiC |
| 			 |              |               | VNET ping tool to debug VNET configuration |
| 			 |              |				| Vxlan enhancement - Deferred from 202205 release | 
|		     |				|				|[VRRP](https://github.com/sonic-net/SONiC/issues/1726) |
|			 |				|				| YANG model enhancement - Deferred from 202305 release | 

**NOTE**
* Platform APIs will be backwards compatible in 201908, will be cut over to new APIs in the next release
