// SIPClientDemo.cpp : 定义控制台应用程序的入口点。
//

#include <eXosip2/eXosip.h>
#include <WinSock2.h>
#include <iostream>

/*
Dnsapi.lib
Iphlpapi.lib
Ws2_32.lib
osip2.lib
osipparser2.lib
exosip.lib
*/
#pragma comment(lib,"Ws2_32.lib")
#pragma comment(lib,"Dnsapi.lib")
#pragma comment(lib,"Iphlpapi.lib")
#pragma comment(lib,"delayimp.lib")
#pragma comment(lib,"Qwave.lib")

eXosip_t *g_eXosip_t;

void initExosip()
{
    eXosip_init(g_eXosip_t);
}

void uninitExosip()
{
    eXosip_quit(g_eXosip_t);
}

void startListen()
{
    eXosip_listen_addr(g_eXosip_t, IPPROTO_UDP, NULL, 708, AF_INET, 0);
}

int main()
{
    g_eXosip_t = eXosip_malloc();

    initExosip();
    startListen();

    char *source_call = "sip:140@127.0.0.1:708";
    char *dest_call = "sip:133@127.0.0.1:707";

    while (true)
    {
    
    osip_message_t *message = NULL;

    int i = eXosip_message_build_request(g_eXosip_t,&message, "MESSAGE", dest_call, source_call, NULL);;
    if (i != 0)
    {
        printf("Intial INVITE failed!/n");
        return 0;
    }
    //符合SDP格式,其中属性a是自定义格式,也就是说可以存放自己的信息,但是只能是两列,比如帐户信息
    //但是经测试,格式:v o t必不可少,原因未知,估计是协议栈在传输时需要检查的
    char tmp[MAX_PATH] = { 0 };
    sprintf_s(tmp, 
        "v=0/r/n"
        "o=anonymous 0 0 IN IP4 0.0.0.0/r/n"
        "t=1 10/r/n"
        "a=username:rainfish/r/n"
        "a=password:123/r/n");
    osip_message_set_body(message, tmp, strlen(tmp));
    osip_message_set_content_type(message, "application/sdp");

    eXosip_lock(g_eXosip_t);
    i = eXosip_message_send_request(g_eXosip_t, message);
    eXosip_unlock(g_eXosip_t);

    Sleep(6000);
    }
    return 0;
}// SIPClientDemo.cpp : 定义控制台应用程序的入口点。
//

