#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

#define ip_addr = argv[1];
#define system(const char *command);

int get_forth(char* ip_addr){
    //need to split after '.', not just return the last 3 in the array
    string fourth = int(ip_addr[:3]); // same as python3?
    return forth;
}
string ping(string ip_addr){
    string cmd = "ping -c 2" + ip_addr
    //string result = check_output(CMD); //sames as python3?
    system(cmd);
    return result;
}
string ping_sweep(string ip_addr){
    int limit = 255;
    // 192.168.0.21
    // need to split after 
    for(int i = get_fourth(ip_addr); i >= limit; i++;){
        string_inc_ip = ip_addr.split(3,'.')
    }
    
}
int main
