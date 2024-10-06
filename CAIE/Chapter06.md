# 6 Security, Privacy and Data Integrity 安全，隐私与数据完整性

## 6.1 Data Security 数据安全

### data integrity 数据完整性

a requirement for data to be accurate, complete, consistent and up to date.

### data privacy 数据隐私

a requirement for data to be available only to authorised users.

### data security 数据安全

a requirement for data to be available for use when needed, can be recovered if
lost or corrupted, and only accessible by the authorised.  It emphasize on the
prevention against data **loss**.

### data protection law 数据保护法

a law that governs how data should be kept private and secure.

### malware 恶意软件

malicious software that has the intention of causing harm to a computer system
or its contents.

### virus 电脑病毒

malware that **replicates itself** and can corrupt data.

### hacking 黑客攻击

illegal access to a computer system without the owner’s permission.

### ethical hacking 道德黑客攻击

hacking used to test the security and vulnerability of a computer system.

### phishing 网络钓鱼

use email to trick the recipient into giving personal data to the malicious
sender.

### pharming 网域嫁接

redirect the user to fake website in order to illegally obtain personal data.

### authentication 身份验证

verification that someone or something is who or what they claim to be.

### firewall 防火墙

hardware or software that monitors and controls incoming and outgoing traffic
between a computer and external network.

### eEncryption 加密

encode data (plaintext) using encryption key to form ciphertext.  Ciphertext
can’t be understood if intercepted.

### decryption 解密

use algorithm with the correct decryption key to covert ciphertext back to
plaintext.

### anti-spyware software 反间谍软件

software that detects and removes spyware programs on a computer system.

### authorisation 授权

definition of a user’s access rights to system components.

## 6.2 Data Integrity 数据完整性

### validation 数据校验

a check that data entered is of the correct type and format; it does not
guarantee that data is accurate.

### verification 数据验证

confirmation that the data received by a system is correct. It does not check
if the **original** data is accurate.

### check digit 校验数位

verification method that calculates an additional digit from the number to
be sent and append it to the number.

### parity byte 奇偶校验字节

verification method used in data transmission. An additional bit is added to
make the number of 1s in the byte odd or even to match the parity. If a byte
with an odd number of 1 bits is received when even parity is used, there is
an error.

### parity block 奇偶校验块

Parity is calculated horizontally and vertically. A parity byte is created
from the bits produced by the vertical parity check and sent with the data.
The receiver re-checks the parity and identify the position of the incorrect
bit if there is one.

### checksum 校验和

verification method used in data transmission by calculating a number from the
data and transmit it with the data. The receiver repeats the calculation and
compares the result with the value received. If the two are different, there is
an error.
