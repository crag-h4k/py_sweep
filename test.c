#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
//#include <string.h>

//#define ip_addr = argv[1];
//#define system(char command);

int get_forth(char* ip_addr){
    //need to split after '.', not just return the last 3 in the array
    char* fourth = int(ip_addr[:3]); // same as python3?
    return forth;
}
stri ping(char* ip_addr){
    char* cmd = "ping -c 2" + ip_addr;
    //string result = check_output(CMD); //sames as python3?
    system(cmd);
    return result;
}
char* ping_sweep(char* ip_addr){
    int limit = 255;
    // 192.168.0.21;
    // need to split after 
    for(int i = get_fourth(ip_addr); i >= limit; i++;){
        char*_inc_ip = ip_addr.split(3,'.');
    }
    
}
void main(){
    system("ping 192.168.174.1");
}
