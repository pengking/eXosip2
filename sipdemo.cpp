// SIPDemo.cpp : 定义控制台应用程序的入口点。
//

/*
Dnsapi.lib
Iphlpapi.lib
Ws2_32.lib
osip2.lib
osipparser2.lib
exosip.lib
*/

#include <eXosip.h>
#include <WinSock2.h>
#include <iostream>


#define time_out_s 5
#define time_out_ms 0

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
	eXosip_listen_addr(g_eXosip_t, IPPROTO_UDP, NULL, 707, AF_INET, 0);
}

void proMessage()
{
	while (true)
	{
		eXosip_event_t *ret = eXosip_event_wait(g_eXosip_t, time_out_s, time_out_ms);
		if (ret != NULL)
		{
			switch (ret->type)
			{
				
					///* REGISTER related events */
					//EXOSIP_REGISTRATION_SUCCESS,       /**< user is successfully registred.  */
					//EXOSIP_REGISTRATION_FAILURE,       /**< user is not registred.           */

					///* INVITE related events within calls */
					//EXOSIP_CALL_INVITE,            /**< announce a new call                   */
					//EXOSIP_CALL_REINVITE,          /**< announce a new INVITE within call     */

					//EXOSIP_CALL_NOANSWER,          /**< announce no answer within the timeout */
					//EXOSIP_CALL_PROCEEDING,        /**< announce processing by a remote app   */
					//EXOSIP_CALL_RINGING,           /**< announce ringback                     */
					//EXOSIP_CALL_ANSWERED,          /**< announce start of call                */
					//EXOSIP_CALL_REDIRECTED,        /**< announce a redirection                */
					//EXOSIP_CALL_REQUESTFAILURE,    /**< announce a request failure            */
					//EXOSIP_CALL_SERVERFAILURE,     /**< announce a server failure             */
					//EXOSIP_CALL_GLOBALFAILURE,     /**< announce a global failure             */
					//EXOSIP_CALL_ACK,               /**< ACK received for 200ok to INVITE      */

					//EXOSIP_CALL_CANCELLED,         /**< announce that call has been cancelled */

					///* request related events within calls (except INVITE) */
					//EXOSIP_CALL_MESSAGE_NEW,              /**< announce new incoming request. */
					//EXOSIP_CALL_MESSAGE_PROCEEDING,       /**< announce a 1xx for request. */
					//EXOSIP_CALL_MESSAGE_ANSWERED,         /**< announce a 200ok  */
					//EXOSIP_CALL_MESSAGE_REDIRECTED,       /**< announce a failure. */
					//EXOSIP_CALL_MESSAGE_REQUESTFAILURE,   /**< announce a failure. */
					//EXOSIP_CALL_MESSAGE_SERVERFAILURE,    /**< announce a failure. */
					//EXOSIP_CALL_MESSAGE_GLOBALFAILURE,    /**< announce a failure. */

					//EXOSIP_CALL_CLOSED,            /**< a BYE was received for this call      */

					///* for both UAS & UAC events */
					//EXOSIP_CALL_RELEASED,             /**< call context is cleared.            */

					///* response received for request outside calls */
					//EXOSIP_MESSAGE_NEW,              /**< announce new incoming request. */
					//EXOSIP_MESSAGE_PROCEEDING,       /**< announce a 1xx for request. */
					//EXOSIP_MESSAGE_ANSWERED,         /**< announce a 200ok  */
					//EXOSIP_MESSAGE_REDIRECTED,       /**< announce a failure. */
					//EXOSIP_MESSAGE_REQUESTFAILURE,   /**< announce a failure. */
					//EXOSIP_MESSAGE_SERVERFAILURE,    /**< announce a failure. */
					//EXOSIP_MESSAGE_GLOBALFAILURE,    /**< announce a failure. */

					///* Presence and Instant Messaging */
					//EXOSIP_SUBSCRIPTION_NOANSWER,          /**< announce no answer              */
					//EXOSIP_SUBSCRIPTION_PROCEEDING,        /**< announce a 1xx                  */
					//EXOSIP_SUBSCRIPTION_ANSWERED,          /**< announce a 200ok                */
					//EXOSIP_SUBSCRIPTION_REDIRECTED,        /**< announce a redirection          */
					//EXOSIP_SUBSCRIPTION_REQUESTFAILURE,    /**< announce a request failure      */
					//EXOSIP_SUBSCRIPTION_SERVERFAILURE,     /**< announce a server failure       */
					//EXOSIP_SUBSCRIPTION_GLOBALFAILURE,     /**< announce a global failure       */
					//EXOSIP_SUBSCRIPTION_NOTIFY,            /**< announce new NOTIFY request     */

					//EXOSIP_IN_SUBSCRIPTION_NEW,            /**< announce new incoming SUBSCRIBE.*/

					//EXOSIP_NOTIFICATION_NOANSWER,          /**< announce no answer              */
					//EXOSIP_NOTIFICATION_PROCEEDING,        /**< announce a 1xx                  */
					//EXOSIP_NOTIFICATION_ANSWERED,          /**< announce a 200ok                */
					//EXOSIP_NOTIFICATION_REDIRECTED,        /**< announce a redirection          */
					//EXOSIP_NOTIFICATION_REQUESTFAILURE,    /**< announce a request failure      */
					//EXOSIP_NOTIFICATION_SERVERFAILURE,     /**< announce a server failure       */
					//EXOSIP_NOTIFICATION_GLOBALFAILURE,     /**< announce a global failure       */

					//EXOSIP_EVENT_COUNT                  /**< MAX number of events              */
			default:
				osip_body_t *body;
				osip_message_get_body(ret->request, 0, &body);
				printf("I get the msg is: %s/n", body->body);
				
				std::cout << "message type is " << ret->type << std::endl;
				break;
			}
		}
		else
		{
			std::cout << "ret value is NULL" <<std::endl;

		}
		eXosip_event_free(ret);	
		ret = NULL;
	}
}

int main(int argc, _TCHAR* argv[])
{
	g_eXosip_t  = eXosip_malloc();
	initExosip();
	startListen();
	proMessage();

	system("pause");
	return 0;
}

