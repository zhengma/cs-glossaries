# 14 Communication and internet technologies 通讯与互联网技术

## 14.1 Protocol 协议

a set of rules governing data transmission across a network, which are agreed
by sender and receiver.

### protocol suite 协议群

The protocols in a **stack** determine the interconnectivity rules for a
**layered** network model such as the TCP/IP model.

### the four layers of TCP/IP protocol suite TCP/IP 协议群的四个层次

the protocol suite underpinning Internet usage.  It consists of four layers,
from lowest to highest: Link, Internet, Transport and Application.

### Link Layer 链路层

responsible for handling how data is physically transported within the network.
It enables the upper layers to access the **physical medium** and ensure the
correct network protocols are followed.

### Internet Layer 网络层

also known as *Network Layer*.  It identifies the intended network and host,
addresses packets with their source and destination addresses by adding a
further header, and transmit the packet to the Link Layer. It is also
responsible for routing the packets independently through the optimum route.

### Transport Layer 传输层

responsible for delivery of data from the source host to the destination host.
It receives data from the application layer, breaks it into packets, add a
header to each packet, and send to the Internet layer, and establish end to end
contact.  It also automatically retransmit lost packets. Protocols in this layer
include: TCP, UDP.

### Transmission Control Protocol (TCP) 传输控制协议

a transport layer protocol that is host-to-host (establish end-to-end
connections between the two devices before transmitting).

### Application Layer 应用层

responsible for allowing applications to access the services used in other
layers, and also defines the protocols that any app uses to allow the exchange
of data. Examples include: HTTP/HTTPS, FTP, POP3, SMTP, IMAP, BitTorrent,
etc.

### HyperText Transfer Protocol (HTTP) 超文本传输协议

the most important application layer protocol used to transmit HTML documents
(web pages). It underpins the WWW.

### HTTP Secure (HTTPS) 安全超文本传输协议

the encrypted version of HTTP.

### File Transport Protocol (FTP) 文件传输协议

an application layer protocol for sending and receiving files over a network.

### Simple Mail Transfer Protocol (SMTP) 简单邮件传输协议

an application layer protocol used to send (push) email messages toward the
intended destination, usually a mail server.

### Post Office Protocol 3 (POP3) 邮局协议3

an application layer protocol used to retreive (pull) email messages by
downloading and then deleting messages from the mail server.

### Internet Message Access Protocol (IMAP) 互联网消息访问协议

an application layer protocol used by email clients that keeps it in sync with
a mail server via retrieving a copy of email messages from the server over a
TCP/IP connection.

### BitTorrent

an application layer protocol that provides peer-to-peer file sharing.

## 14.2 Circuit switching, packet switching  线路交换，分组交换

### circuit switching 线路交换

method of transmission, in which a dedicated circuit/path/channel/connection is
established before transmission starts, and lasts throughout the duration of
transmission. All data is transferred over this same route, using its whole
bandwidth. Typical applications include: standard voice communications (PSTN),
video streaming and private data networks.

### Packet switching 分组交换

method of transmission, where data to be transmitted is split into packets, and
each packet can be sent along route independently from each other. The routing
depends on the congestion, so the packets may not arrive in the order sent.
Most computer data networks, including the Internet, uses packet switching.

### routing table 路由表

a data table that contains the information necessary to forward a package along
the shortest or best route to allow it to reach its destination.
