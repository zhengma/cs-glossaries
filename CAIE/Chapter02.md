# 2 Communication 通讯

## 2.1 Networks Including the Internet 网络，包括互联网

### wide area network (WAN) 广域网

a network connecting computers on different sites, possibly thousands of
kilometres apart.

### local area network (LAN) 局域网

a network connecting computers in a small geographical area, usually privately
owned.

### Internet 互联网

the largest WAN in the world.  Massive network of networks made up of computers
and other devices.  Use TCP/IP communication protocols.

### World Wide Web (WWW) 万维网

the most important service running on the Internet.  A collection of multimedia
web pages, written in HTML, stored on websites, and specified by URLs.  Use a
client-server model and the HTTP/HTTPS protocol to access.

### Wi-Fi

also known as wireless LAN (WLAN) or wireless Ethernet.  

### client-server model 客户端-服务器模型

an architecture where specific client devices connect to and run applications on
dedicated servers on a network. Server receives and processes the requests from
the clients, and clients send requests to the server and output the response.

### server 服务器

a system providing a specific function/service to clients.  Examples of services
include: web, email, file access, print, etc.

### thin-client 瘦客户端

a client that only provides input and receives output from the application.  It
needs connection to a network to work.

### thick-client 胖客户端

a client that carries out at least some of the processing itself, so that it
can also work in offline mode.

### peer-to-peer network 对等网络

a model in which all computers are of equal status and data is distributed. Each
computer is responsible for its own security and they communicate to share
resources.

### topology 网络拓扑

the configuration of a network that defines how the various devices on the
network are connected.

### bus topology 总线拓扑

a network topology using a single central cable, to which all devices are
attached.

### end system 端系统

a computer or server connected to a network.

### star topology 星形拓扑

a network topology in which each end-system is linked to a central device.

### mesh topology 网状拓扑

a network topology containing direct links between devices.

### hybrid network

a collection of connected LANs where some of them have different topologies
or supporting technologies.

### cable 线缆

a transmission using copper wire or fibre-optic, such as twisted pair cable,
coaxial cable or fibre-optic cable.

### bandwidth 带宽

a measure of the amount of data that can be transmitted per second.

### wireless 无线

a transmission using radio, microwave or infrared.

### repeater 中继器

a device that connects two cables and provides a full-strength signal to
the second cable.

### gateway 网关

a device that connects two LANs using different protocols.

### bridge 网桥

a device that connects two segments of a LAN using the same protocols.

### Network Interface Card (NIC) 网卡

a component used to identify the end-system and provides an interface to
wireless network.

### Ethernet 以太网

a protocol for data transmission over wired network using CSMA/CD.  Data is
transmitted in frames. Each frame has a source and destination address and
error checking data.

### collision 冲突

two messages from different sources trying to transmit along the same channel.

### carrier-sense multiple access with collision detection (CSMA/CD) 载波监听多点接入 / 碰撞检测

a method used in Ethernet to detect and resolve collision.

### switch 交换机

a connecting device that connects two or more devices, and allow them to
communicate with each other by receiving transmissions and forwarding them to
their destination.

### Wireless Access Point (WAP) 无线热点

the connecting device in a Wi-Fi LAN that allows a central device connecting
to other devices by sending and receiving radio signals.  Also allow wireless
enabled devices to connect to a wired network.

### router 路由器

a device that enables data packets to be routed between different networks.

### public switched telephone network (PSTN) 公共交换电话网络

wired network for conventional telephone to make calls or send faxes.

### cloud 云

Accessing a service/files/software on a remote **server**.

### private cloud 私有云

owned by and only accessible to an organisation, being offered either over the
Internet or a private internal network.

### public cloud 公有云

owned by a cloud service provider over the public Internet, accessible to anyone
with the appropriate credentials.

### Bit streaming 比特流

Transfer sequence of bits over the Internet at high speed.  Bits arrive in the
same order as they were sent.  It requires fast broadband connection some form
of buffering.

### On-demand

when the bit stream content is transmitted at a time chosen by the user.

### Real-time

when the bit stream content is transmitted as it is produced.

### Bit rate 比特率

the number of bits transmitted per second.

### Internet Protocol (IP) 互联网协议

assign an address (IPv4 or IPv6) to each device connected to the internet.

### IPv4 address IPv4 地址

a 32-bit long, hierarchical address of a device on the Internet.  Commonly
written as four denary numbers (0~255 each) separated by three periods.
The first part is a netID and the second part is a hostID.

### IPv6 address IPv6 地址

128-bit long.  Commonly written as eight chunks of hexadecimal numbers
(four digits each) separated by seven colons.

### public IP address 公网IP地址

an IP address visible to any device on the Internet, allowing direct access
on the Internet.

### private IP address 私有IP地址

an IP address only visible to devices within the LAN and used for LAN
communication only.

### static IP address 静态IP地址

an IP address allocated to a device, and does not change each time the device
rejoins the network.

### dynamic IP address 动态IP地址

the IP address allocated to a device that may be different each time the device
rejoins the network.

### Subnetting 子网

divide network into two or more sub-networks.  It reduces the traffic in a
network, improves network security and allow for easier maintenance.

### Network Address Translation (NAT) 网络地址转换

a technique used by routers to allow multiple devices in a private LAN to share
a single public IP address.

### Domain name service (DNS) 域名服务

a hierarchical distributed database installed on domain name servers that is
responsible for mapping a domain name to an IP address. Also known as domain
name system.
