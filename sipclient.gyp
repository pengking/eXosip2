# libspeex.gyp
# Author:pengchun
# Data:2017/7/3

{

  'targets':[
    {
       'target_name':'sipclient',
       'type':'executable',

       'dependencies':[
          '../libexosip/libexosip.gyp:*',
          '../libosip2/libosip2.gyp:*',
          '../libosipparser2/libosipparser2.gyp:*',
          '../libcares/libcares.gyp:*',
        ],

      'defines':[
         '',
         'WIN32',
         '',
       ],

      'include_dirs':[
        '../../siplib/exosip',
        '../../siplib/exosip/include/eXosip2',
        '../../siplib/exosip/include',
        '../../siplib/c-ares',
        '../../siplib/osip/include',
      ],

      'sources':[

         '../../src/sipclient/sipclient.cpp', 

      ], # sources

      'link_settings':{

        # 编译时所依赖的具体的库
        'libraries':[

          # '../../../siplib/lib/eXosip.lib',
          # '../../../siplib/lib/osip2.lib',
          # '../../../siplib/lib/osipparser2.lib',
          # '../../../siplib/lib/libcares.lib',
          
          'Ws2_32.lib',
          'Dnsapi.lib',
          'Iphlpapi.lib',
          'delayimp.lib',
          'Qwave.lib',
          'kernel32.lib',
          'user32.lib',
          'gdi32.lib',
          'winspool.lib',
          'comdlg32.lib',
          'advapi32.lib',
          'shell32.lib',
          'ole32.lib',
          'oleaut32.lib',
          'uuid.lib',
          'odbc32.lib',
          'odbccp32.lib',

        ],# libraries

      }, # link_settings


        
     }, # target

   ] # targes

} # total file
