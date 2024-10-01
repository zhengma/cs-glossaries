# 1 Information Representation 信息的表示

## 1.1 Data Representation 数据的表示

### denary numbers 十进制数

also known as decimal numbers, are written using one of the symbols 0~9 for
each denary digit.

### bit 位

a digit in the binary number system written using either of the symbols 0 and 1.

### byte 字节

a group of eight bits treated as a single unit.

### nibble 半字节

a group of four bits.

### decimal prefix 十进制前缀

a prefix to define the magnitude of a value. Examples are *kilo-*, *mega-*,
*giga-* and *tera-* representing factors of $10^3$, $10^6$, $10^9$ and
$10^{12}$ respectively.

### binary prefix 二进制前缀

a prefix to define the magnitude of a value. Examples are *kibi*, *mebi*,
*gibi* and *tebi* representing factors of $2^{10}$, $2^{20}$, $2^{30}$ and
$2^{40}$ respectively.

### one’s complement 反码表示法

a form of signed integer, in which the binary representation of $-n$ is the
bitwise `NOT` of that of $n$.

### two’s complement 补码表示法

a form of signed integer, in which the binary representation of $-n$ is the
bitwise `NOT` of that of $n$ **plus 1**.

### overflow 溢出

a condition when the result of a calculation is too large to fit into the
number of bits defined for storage.

### binary coded decimal (BCD)

the storage of a binary value representing one denary digit in a nibble.

### packed BCD

store two BCD nibbles in one byte.

## 1.2 Multimedia 多媒体

### vector graphic 矢量图

a graphic consisting of drawing objects defined in a drawing list.

### drawing object

a component defined by geometric formulae and associated properties (fill
colour, line width, etc.).

### drawing list

a list contains one set of values for each drawing object.

### property 性质

defines one aspect of the appearance of the drawing object.

### bitmap image 位图

an image made up of pixels stored in sequence.

### picture element (pixel) 像素

the smallest identifiable component of a bitmap image, defined by just two
properties: its position in the bitmap matrix and its colour.

### colour depth 色深

the number of bits used to represent one pixel.

### bit depth 位深

the number of bits used to represent each of the red, green and blue colours.

### image resolution 图像分辨率

the number of pixels in the bitmap file defined as the product of the width and
the height values.

### screen resolution 屏幕分辨率

the product of width and height values for the number of pixels that the screen
can display.

### file header 文件的标头

a set of bytes at the beginning of a bitmap file which identifies the file and
contains information about the coding used.

### analogue data 模拟信号数据

data obtained by measurement of a physical property which can have any value
from a continuous range of values.

### digital data 数字信号数据

data that has been stored as a binary value which can have one of a discrete
range of values.

### sampling 采样

taking measurements at regular intervals and storing the value.

### sampling resolution 采样分辨率

the number of bits used to store each sample.

### sampling rate 采样频率

the number of samples taken per second.

## 1.3 Compression 压缩

### compression 压缩

represent the original content of a file with another file of smaller
size. Compressed file takes less storage space and can be transmitted in less
time using less bandwidth.

### lossless compression 无损压缩

compression methods that allow subsequent decoding to recreate exactly the
original file.

### lossy compression 有损压缩

compression methods that cause some information to be lost so that the exact
original file cannot be recovered in subsequent decoding.

### Running-Length Encoding (RLE) 游程编码

a lossless compression algorithm that identifies consecutive repeating data
and stores the data and the number of times it repeats.
