### Denary numbers
also known as decimal numbers are written using one of the symbols 0~9 for 
each denary digit.

### Bit
a digit in the binary number system written using either of the symbols 0 and 1.

### Byte
a group of eight bits treated as a single unit.

### Nibble
a group of four bits.

### Decimal prefix
a prefix to define the magnitude of a value. Examples are *kilo-*, *mega-*, 
*giga-* and *tera-* representing factors of $10^3$, $10^6$, $10^9$ and 
$10^{12}$ respectively.

### Binary prefix
a prefix to define the magnitude of a value. Examples are *kibi*, *mebi*, 
*gibi* and *tebi* representing factors of $2^{10}$, $2^{20}$, $2^{30}$ and 
$2^{40}$ respectively.

### One’s complement
a form of signed integer, in which $-n$ is represented by taking a bitwise 
`NOT` of the binary representation of $n$. 

### Two’s complement
a form of signed integer, in which $-n$ is represented by taking a bitwise 
`NOT` of the binary representation of $n$ and then add $1$ to it.

### Overflow
a condition when the result of a calculation is too large to fit into the 
number of bits defined for storage.

### Binary coded decimal (BCD)
the storage of a binary value representing one denary digit in a nibble.

### Packed BCD
store two BCD nibbles in one byte.

### Vector graphic
a graphic consisting of drawing objects defined in a drawing list.

### Drawing object
a component defined by geometric formulae and associated properties (fill 
colour, line width, etc.).

### Drawing list
a list contains one set of values for each drawing object.

### Property
defines one aspect of the appearance of the drawing object.

### Bitmap image
an image made up of pixels stored in sequence.

### Picture element (pixel)
the smallest identifiable component of a bitmap image, defined by just two 
properties: its position in the bitmap matrix and its colour.

### Colour depth
the number of bits used to represent one pixel.

### Bit depth
the number of bits used to represent each of the red, green and blue colours.

### Image resolution
the number of pixels in the bitmap file defined as the product of the width and 
the height values.

### Screen resolution
the product of width and height values for the number of pixels that the screen 
can display.

### File header
a set of bytes at the beginning of a bitmap file which identifies the file and 
contains information about the coding used.

### Analogue data
data obtained by measurement of a physical property which can have any value 
from a continuous range of values.

### Digital data
data that has been stored as a binary value which can have one of a discrete 
range of values.

### Sampling
taking measurements at regular intervals and storing the value.

### Sampling resolution
the number of bits used to store each sample.

### Sampling rate
the number of samples taken per second.

### Compression
represent the original content of a file with a file of smaller size.  
Compressed file takes less storage space and can be transmitted in less time 
using less bandwidth.

### Lossless compression
compression methods that allow subsequent decoding to recreate exactly the 
original file.

### Lossy compression
compression methods that cause some information to be lost so that the exact 
original file cannot be recovered in subsequent decoding.

### Running-Length Encoding (RLE)
a lossless compression algorithm that identifies consecutive repeating data 
and stores the data and the number of times it repeats.