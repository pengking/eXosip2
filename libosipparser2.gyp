# libspeex.gyp
# Author:pengchun
# Data:2017/7/3

{

  'targets':[
    {
       'target_name':'libosipparser2',
       'type':'static_library',
       
       # 添加依赖的gypi文件
        'includes':[
          '../buildall/common.gypi',
        ],

       
        'conditions':[
          ['OS=="win"',{

             'defines':[

                'ENABLE_TRACE',
                'SYSTEM_LOGGER_ENABLED',
                '_CRT_SECURE_NO_DEPRECATE',


              ],

            'variables':{

              'lib_path':'D:/Work/GitWorkwc/ThirdPart',
              'src_path':'../src',
              'include_path':'D:/Work/GitWorkwc/ThirdPart',
             },

             'include_dirs':[

               '../../siplib/osip/include',

             ],

            'sources':[
               #'<!@(dir "<(src_path)" /b /"*.cpp/" | findstr /i/v "AccessFileByMemoryMap.cpp")',
               #'<!@(for %%i in (/'dir "<(src_path)" /b/' ) do echo %%i)',
               #'<!@(dir "<(src_path)/*.cpp" /b /a-d |findstr /v "AccessFileByMemoryMap.cpp")',
               #'<!@(for %i in ("../src/*.cpp") do @( if not "%i"=="AccessFileByMemoryMap.cpp" (@echo %i)))',

               #'<!@(for /r <(src_path) %i in ("./*.cpp","./*.cc","./*.h","./*.properties") do @if not "%i"=="AccessFileByMemoryMap.cpp" @echo <(src_path)/%i)',
               #'<!@(python "getsourc.py")',
               
               '../../siplib/osip/src/osipparser2/osip_accept.c', 
               '../../siplib/osip/src/osipparser2/osip_accept_encoding.c', 
               '../../siplib/osip/src/osipparser2/osip_accept_language.c', 
               '../../siplib/osip/src/osipparser2/osip_alert_info.c', 
               '../../siplib/osip/src/osipparser2/osip_allow.c', 
               '../../siplib/osip/src/osipparser2/osip_authentication_info.c', 
               '../../siplib/osip/src/osipparser2/osip_authorization.c', 
               '../../siplib/osip/src/osipparser2/osip_body.c', 
               '../../siplib/osip/src/osipparser2/osip_call_id.c', 
               '../../siplib/osip/src/osipparser2/osip_call_info.c', 
               '../../siplib/osip/src/osipparser2/osip_contact.c', 
               '../../siplib/osip/src/osipparser2/osip_content_disposition.c', 
               '../../siplib/osip/src/osipparser2/osip_content_encoding.c', 
               '../../siplib/osip/src/osipparser2/osip_content_length.c', 
               '../../siplib/osip/src/osipparser2/osip_content_type.c', 
               '../../siplib/osip/src/osipparser2/osip_cseq.c', 
               '../../siplib/osip/src/osipparser2/osip_error_info.c', 
               '../../siplib/osip/src/osipparser2/osip_from.c', 
               '../../siplib/osip/src/osipparser2/osip_header.c', 
               '../../siplib/osip/src/osipparser2/osip_list.c', 
               '../../siplib/osip/src/osipparser2/osip_md5c.c', 
               '../../siplib/osip/src/osipparser2/osip_message.c', 
               '../../siplib/osip/src/osipparser2/osip_message_parse.c', 
               '../../siplib/osip/src/osipparser2/osip_message_to_str.c', 
               '../../siplib/osip/src/osipparser2/osip_mime_version.c', 
               '../../siplib/osip/src/osipparser2/osip_parser_cfg.c', 
               '../../siplib/osip/src/osipparser2/osip_port.c', 
               '../../siplib/osip/src/osipparser2/osip_proxy_authenticate.c', 
               '../../siplib/osip/src/osipparser2/osip_proxy_authentication_info.c', 
               '../../siplib/osip/src/osipparser2/osip_proxy_authorization.c', 
               '../../siplib/osip/src/osipparser2/osip_record_route.c', 
               '../../siplib/osip/src/osipparser2/osip_route.c', 
               '../../siplib/osip/src/osipparser2/osip_to.c', 
               '../../siplib/osip/src/osipparser2/osip_uri.c', 
               '../../siplib/osip/src/osipparser2/osip_via.c', 
               '../../siplib/osip/src/osipparser2/osip_www_authenticate.c', 
               '../../siplib/osip/src/osipparser2/sdp_accessor.c', 
               '../../siplib/osip/src/osipparser2/sdp_message.c', 
               '../../siplib/osip/include/osipparser2/headers/osip_accept.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_accept_encoding.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_accept_language.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_alert_info.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_allow.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_authorization.h', 
               '../../siplib/osip/include/osipparser2/internal.h', 
               '../../siplib/osip/include/osipparser2/osip_body.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_call_id.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_call_info.h', 
               '../../siplib/osip/include/osipparser2/osip_const.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_contact.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_content_disposition.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_content_encoding.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_content_length.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_content_type.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_cseq.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_error_info.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_from.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_header.h', 
               '../../siplib/osip/include/osipparser2/osip_headers.h', 
               '../../siplib/osip/include/osipparser2/osip_list.h', 
               '../../siplib/osip/include/osipparser2/osip_md5.h', 
               '../../siplib/osip/include/osipparser2/osip_message.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_mime_version.h', 
               '../../siplib/osip/include/osipparser2/osip_parser.h', 
               '../../siplib/osip/include/osipparser2/osip_port.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_proxy_authenticate.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_proxy_authorization.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_record_route.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_route.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_to.h', 
               '../../siplib/osip/include/osipparser2/osip_uri.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_via.h', 
               '../../siplib/osip/include/osipparser2/headers/osip_www_authenticate.h', 
               '../../siplib/osip/src/osipparser2/parser.h', 
               '../../siplib/osip/include/osipparser2/sdp_message.h', 

             ], # sources

            'link_settings':{

              'configurations': {

                # Debug时的编译链接路径
                'Debug' : {
                    'library_dirs':[
                    ],

                    'msbuild_configuration_attributes': {
                      #'OutputDirectory':'Bin/Debug',
                      #'IntermediateDirectory': '$(OutDir)bin/Debug//',
                    },

                }, # Debug

                # Release时的编译链接路径
                'Release' : {

                    'library_dirs':[
                    ],

                    'msbuild_configuration_attributes': {
                      #'OutputDirectory':'../Bin/Release',
                      #'IntermediateDirectory': '$(OutDir)bin/Release//',
                    },

                     
                }, # Release


                }, # configurations

              # 编译时所依赖的具体的库
              'libraries':[

                #'winmm.lib',

              ],# libraries

            }, # link_settings
            


          }], # OS==win

          # 配置Linux相关内容
          ['OS!="win"',{

            # 配置Linux环境中的编译
            'variables':{

              'lib_path':'../../AVProcessMgr/x86_64_linux',
              'src_path':'../src',
              'include_path':'../../AVProcessMgr/x86_64_linux',

            }, # variables

              # 配置编译源文件
            'sources':[

              '<!@(python "getsourc.py")',

            ], # sources

            'include_dirs':[
               '../../speex/include/speex/unix',
               '../../speex/include',
               '../../speex/libspeex',
            ],

            # Linux编译的时候会用到cflags
            'cflags':[
                '-Wall','-lpthread','-lrt','-g','-std=c++0x','-m64',
            ],

            # Linux编译时链接设置
            'link_settings':{

                'libraries':[
		              #'-ldl','-L','<(lib_path)/svac/lib/x64/','-lpthread','-lintlc','-lsvacdec64','-lsvml','-lwqplaysdk',


                ], # libraries 

              }, # link_settings

          }], # os != win

        ], # conditions
      

        # 配置包含文件路径
        'include_dirs':[

          '../../include',

        ], # include_dirs
        
     }, # target

   ] # targes

} # total file
