#_author: liuz
#date: 2017/12/22
import os
'''IO多路复用  是同步的
/O多路复用是用于提升效率，单个进程可以同时监听多个网络连接IO
I/O是指Input/Output
I/O多路复用，通过一种机制，可以监视多个文件描述符，
一旦描述符就绪（读就绪和写就绪），能通知程序进行相应的读写操作。
I/O多路复用避免阻塞在io上，
原本为多进程或多线程来接收多个连接的消息变为单进程
或单线程保存多个socket的状态后轮询处理.
下面3个方法就是执行这个效果
1.select是通过系统调用来监视一组由多个文件描述符组成的数组，通过调用select()返回结果 数组中就绪的文件描述符会被内核标记出来，然后进程就可以获得这些文件描述符，然后进行相应的读写操作
2.pll poll本质上与select基本相同，只不过监控的最大连接数上相较于select没有了限制，因为poll使用的数据结构是链表，而select使用的是数组，数组是要初始化长度大小的，且不能改变
3.epoll相当于是linux内核支持的方法，而epoll主要是解决select，poll的一些缺点
'''