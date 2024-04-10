## SONiC on GNS3 VM 

GNS3 is an environment that allows simulation of networking equipment in realistic scenarios. It can be used to emulate, configure, test, and troubleshoot networks in a simulated environment. GNS3 allows you to run a small network topology
consisting of only a few devices on your Windows 10 laptop, or larger network topologies using a GNS Server that is installed on an Ubuntu Linux server. You can use the GNS3 simulator to create a virtual environment to emulate various networks. See [GNS3 online documentation](https://docs.gns3.com/) and [Getting started](https://docs.gns3.com/docs/) with GNS3 for complete information.
Use GNS3 to run SONiC simulator VMs. GNS3 consists of the following components:
### For Windows Model
	- GNS3 user interface — Used to create and visualize network connections for the Windows enviorment.

### For Client Server Model
	- GNS3 client — Used to create and visualize complex network connections for the Windows enviorment. 
	- GNS3 server — Controls SONiC VM execution (natively supported on Ubuntu Linux running on a Dell server)
	
### GNS3 VM installation overview

1. Install GNS3 on a windows enviorment using [GNS3 VM installation guide](https://docs.gns3.com/docs/getting-started/installation/windows/#:~:text=The%20following%20are%20the%20optimal%20requirements%20for%20a,%2F%20RVI%20Series%20or%20Intel%20VT-X%20%2F%20EPT).
2. Download the SONiC image from the azure pipeline to the windows enviorment.
3. Import the SONiC image the GNS3 VM enviorment.
4. Build your SONiC topology virtual devices.
5. Log in and configure each device.

### GNS3 VM set up

Once the GNS3 VM is installed and application is opened. We see a window as shown below,

![](https://github.com/prasanna228/prasannaSONiC/blob/main/assets/img/GNS3VM/image1.jpg)


In the GNS3 window, create a project.

a. Select File->New blank project.
b. Name: Enter a new project name.
c. Location: The default projects folder name changes to the new project name.
d. Click OK.

![](https://github.com/prasanna228/prasannaSONiC/blob/main/assets/img/GNS3VM/image2.jpg)

The project window opens. The window title displays the name of the new project.

![](https://github.com/prasanna228/prasannaSONiC/blob/main/assets/img/GNS3VM/image3.jpg)

