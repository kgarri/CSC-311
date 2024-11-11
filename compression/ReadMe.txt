    So the algorithim that our group decided on to use is the Hoffman encoding algorthim this is because
it is realtively simple to deploy since in the end it is transversing and building a tree. The only super 
diffcult part was deciding whether the compression should be in plan text or in binary encoding and due
to problems with the text file actually getting longer through plan text encoding our group decided to 
go with the binary encoding approach. As there is only 256 unique compination of an 8 bit integer and
by encoding our text in a binary format compatiable with utf-8 formating we where able to substantially
reduce the file size and increase the transfer time of the compressed version of the file. 

Now to actually run the program there is two commands to know:

python or python3 compress.py <filename>
this command compresses the file and 
python or python3 decompress.py <filename.huff> 
decompresses the file 

    Other than that there is the server arcitecture which was a filetransferserver.py and the filetransferclient.py.
Both of these can just be run by doing python or python3 <filename.py> and then you input the file you want to transfer 
from one computer to another.


Overall this was a really fun program to make and helped us better understand how file compression works. 

Effort:
100% Katherine Garri
100% Nathan Cobb
100% Duyen Tran
