#include <osip2/osip_mt.h>  
#include <eXosip2/eXosip.h>
#include <WinSock2.h>
  
#include <iostream>  
#include <string>  
  
using namespace std;  

class sipclient
{
public:
    sipclient()
    {
        g_eXosip_t = NULL;
        string strSrcCall =  "sip:140@10.142.62.193:708";  
        string strDestCall = "sip:133@10.142.62.193:707"; 

    }
    bool InitialSip()
    {

    }
    void printHelp()
    {
        string strHelp = string("\n\t--> function describe<--\n\n")  
                        + "\t\tr register\n"  
                        + "\t\tc cancel register \n"  
                        + "\t\ti invite \n"  
                        + "\t\th hang\n"  
                        + "\t\tq quit\n"  
                        + "\t\ts execute method INFO\n"  
                        + "\t\tm execute method MESSAGE\n"  
                        + "\t\te help\n\n";  
        cout << strHelp;  
    }

private:
    eXosip_t *g_eXosip_t;
    string strSrcCall;
    string strDestCall;

};
  
int main(int argc, char* argv[])  
{  
    eXosip_event_t *je;  
    osip_message_t *reg = NULL;  
    osip_message_t *invite = NULL;  
    osip_message_t *ack = NULL;  
    osip_message_t *info = NULL;  
    osip_message_t *message = NULL;  
    eXosip_t *g_eXosip_t = NULL;

    int call_id, dialog_id;  
    int i,flag;  
    int flag1 = 1;  
    int id;  
      
    string strIdentity = "sip:136@127.0.0.1";  
    string strRegisterer = "sip:10.142.62.193:708"; // server ip  
  
    string strSrcCall =  "sip:140@10.142.62.193:708";  
    string strDestCall = "sip:133@10.142.62.193:707"; 

  string strHelp = string("\n\t--> function describe<--\n\n")  
                        + "\t\tr register\n"  
                        + "\t\tc cancel register \n"  
                        + "\t\ti invite \n"  
                        + "\t\th hang\n"  
                        + "\t\tq quit\n"  
                        + "\t\ts execute method INFO\n"  
                        + "\t\tm execute method MESSAGE\n"  
                        + "\t\te help\n\n";  
        cout << strHelp; 
      
    char command;  
    char tmp[4096];  
    char localip[128];  
  
    
  
    string strMsg;  
	g_eXosip_t = eXosip_malloc();
  
    i = eXosip_init(g_eXosip_t);
    if (i != 0)  
    {  
        cout << "\t--> Couldn't initialize eXosip! <--\n";  
        return -1;  
    }  
    else  
    {  
        cout << "\t--> eXosip_init successfully! <-- \n\n";  
    }  
  
    i = eXosip_listen_addr (g_eXosip_t,IPPROTO_UDP, NULL, 708, AF_INET, 0);  
    if (i != 0)  
    {  
        eXosip_quit (g_eXosip_t);  
        cerr << "\n\t--> Couldn't initialize transport layer! <-- \n\n";  
        return -1;  
    }  
    flag = 1;  
    while (flag)  
    {  
        cout << "please input:\t";  
        cin >> command;  
        
        switch (command)  
        {  
        case 'r':  
            cout << "\n\t--> This modal isn't commpleted! \n" << endl;  
            break;  
  
        case 'i': // 初始化的 INVITE 请求  
            i = eXosip_call_build_initial_invite (g_eXosip_t,&invite,  
                                                  strDestCall.c_str(),  
                                                  strSrcCall.c_str(),  
                                                  NULL,  
                                                  "This is a call for a conversation");  
            if (i != 0)  
            {  
                cout << "\n --> Intial INVITE failed! <-- \n";  
                break;  
            }  
  
            // 符合 SDP 格式, 其中属性 a 是自定义格式,也就是说可以存放自己的信息,   
            // 但是只能是两列,比如帐户信息  
            // 但是经测试,格式: v o t必不可少,原因未知,估计是协议栈在传输时需要检查的  
  
            strMsg = string("v=0\r\n")  
                   + "o=anonymous 0 0 IN IP4 0.0.0.0\r\n"  
                   + "t=1 10\r\n"  
                   + "a=username:bluesea\r\n"  
                   + "a=password:123456\r\n";  
  
            osip_message_set_body (invite, strMsg.c_str(), strMsg.length());  
            osip_message_set_content_type (invite, "application/sdp");  
        
            // 这里使用了锁机制以保证同步  
            eXosip_lock (g_eXosip_t);  
            i = eXosip_call_send_initial_invite (g_eXosip_t,invite);  
            eXosip_unlock (g_eXosip_t);  
            flag1 = 1;  
            while (flag1)  
            {  
                je = eXosip_event_wait (g_eXosip_t,0, 200);  
                if (je == NULL)  
                {  
                    cout << "\n\t--> No response or the time is over! <--\n" << endl;  
                    break;  
                }  
            
                switch (je->type)  
                {  
                case EXOSIP_CALL_INVITE:  
                    cout << "\n\t--> a new invite reveived! <--\n" << endl;  
                    break;  
  
                // announce processing by a remote app  
                case EXOSIP_CALL_PROCEEDING:  
                    cout << "\n\t--> proceeding! <--\n" << endl;  
                    break;  
  
                // announce ringback  
                case EXOSIP_CALL_RINGING:  
                    cout << "\n\t--> ringing! <--\n"  
                         << "\n\tcall_id is " << je->cid  
                         << ", dialog_id is " << je->did << endl;  
                    break;  
  
                // 收到请求，表示连接成功，下面发送回复确认  
                case EXOSIP_CALL_ANSWERED:  
                    cout << "\n\t--> ok! connected! <--\n" << endl;  
                    call_id = je->cid;  
                    dialog_id = je->did;  
                    cout << "\n\tcall_id is " << je->cid  
                         << ", dialog_id is " << je->did << endl;  
                    eXosip_call_build_ack (g_eXosip_t,je->did, &ack);  
                    eXosip_call_send_ack (g_eXosip_t,je->did, ack);  
                    flag1 = 0;  
                    break;  
  
                case EXOSIP_CALL_CLOSED:  
                    cout << "\n\t--> the other sid closed! <--\n" << endl;  
                    break;  
  
                case EXOSIP_CALL_ACK:  
                    cout << "\n\t--> ACK received! <--\n" << endl;  
                    break;  
  
                default:  
                    cout << "\n\t--> other response!\n" <<endl;  
                    break;  
                }  
            
                eXosip_event_free (je);  
            }  
  
            break;  
  
        case 'h':  
            cout << "\n\t--> Holded ! \n" << endl;  
        
            eXosip_lock (g_eXosip_t);  
            eXosip_call_terminate (g_eXosip_t,call_id, dialog_id);  
            eXosip_unlock (g_eXosip_t);  
            break;  
  
        case 'c':  
            cout << "\n\t--> This modal isn't commpleted! \n" << endl;  
            break;  
  
        case 's':  
            // 传输 INFO 方法  
            eXosip_call_build_info (g_eXosip_t,dialog_id, &info);  
              
            snprintf (tmp , 4096, "hello,bluesea");  
            osip_message_set_body (info, tmp, strlen(tmp));  
  
            // 格式可以任意设定, text/plain 代表文本信息  
            osip_message_set_content_type (info, "text/plain");  
            eXosip_call_send_request (g_eXosip_t,dialog_id, info);  
            break;  
  
        case 'm':  
            // 传输 MESSAGE方法,也就是即时消息，  
            // 和 INFO 方法相比，主要区别，是 MESSAGE 不用建立连接，直接传输信息，  
            // 而 INFO 必须在建立 INVITE 的基础上传输。  
            cout << "\n\t--> the mothed :MESSAGE \n" << endl;  
            eXosip_message_build_request (g_eXosip_t,&message,  
                                          "MESSAGE",  
                                          strDestCall.c_str(),  
                                          strSrcCall.c_str(),  
                                          NULL);  
            strMsg = "message: hello bluesea!";  
            osip_message_set_body (message, strMsg.c_str(), strMsg.length());  
        
            // 假设格式是xml  
            osip_message_set_content_type (message, "text/xml");  
            eXosip_message_send_request (g_eXosip_t,message);
            break;  
  
        case 'q':  
            eXosip_quit (g_eXosip_t);  
            cout << "\n\t--> Exit the setup! \n" << endl;;  
            flag = 0;  
            break;  
  
        case 'e':  
            cout << strHelp << endl;  
            break;  
  
        default:  
            cout << "\n\t--> 不支持的命令 <--\n" << endl;  
            break;  
        }  
    }  
  
    return 0;  
}  