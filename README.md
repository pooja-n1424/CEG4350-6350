## CEG4350-6350

### **Create a producer process and a consumer process sharing data.**
	
- [x] The producer generates total 100 integer data randomly, and the consumer process reads all those data. 
- [x] The data generated by the producer could be stored in a file by the producer; and the data consumed (i.e., read) by the
	consumer could be stored in another file by the consumer.
- [x] The file of produced data and the file of consumed data could be printed to verify that the two processes have cooperated correctly; that means, each data item is not lost and not consumed more than once.
	
### **Interprocess communication (IPC) between producer and consumer (to share data) can be implemented using any two of the following four methods:**

1. **Use a Pipe to transfer 100 data from the producer to the consumer**. 
  Note: a Pipe (anonymous pipe, named pipe, or an equivalent) should be created using a system call, 
  instead of piping the (standard) output of one process to the (standard) input   of another.

2. **Use either the direct message passing or indirect message passing** (using a mailbox, a
message queue, or a similar one) to transfer 100 data from the producer to the consumer.

3. **Use the sockets to transfer 100 data from the producer to the consumer.**
  Note: The producer and consumer processes can be executed on the same machine
  or on different machines.

4. **Use the shared memory and semaphores for the implementation of the logical ring-buffer
(that can store up to 10 data items) and the synchronization.**

### **Programming Languages and Operating Systems:**

- [x] For each implementation of IPC method, any programming language can be used on any
machine running any OS. 
- [x] In other others, different programming languages and OSs can
be used for different IPC methods.
- [x] Instead of creating and using two processes — one for producer and one for consumer —
you can create two threads in a process, except for the socket-based communication
method.
