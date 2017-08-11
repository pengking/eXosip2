# libspeex.gyp
# Author:pengchun
# Data:2017/7/3

{

  'targets':[
    {
       'target_name':'libcares',
       'type':'static_library',
       
       # 添加依赖的gypi文件
        'includes':[
          '../buildall/common.gypi',
        ],

       
        'conditions':[
          ['OS=="win"',{

             'defines':[

                'CARES_STATICLIB',
                'CARES_BUILDING_LIBRARY',
                '_CRT_SECURE_NO_DEPRECATE',


              ],

            'variables':{

              'lib_path':'D:/Work/GitWorkwc/ThirdPart',
              'src_path':'../src',
              'include_path':'D:/Work/GitWorkwc/ThirdPart',
             },

             'include_dirs':[

               '../../siplib/c-ares',

             ],

            'sources':[
               #'<!@(dir "<(src_path)" /b /"*.cpp/" | findstr /i/v "AccessFileByMemoryMap.cpp")',
               #'<!@(for %%i in (/'dir "<(src_path)" /b/' ) do echo %%i)',
               #'<!@(dir "<(src_path)/*.cpp" /b /a-d |findstr /v "AccessFileByMemoryMap.cpp")',
               #'<!@(for %i in ("../src/*.cpp") do @( if not "%i"=="AccessFileByMemoryMap.cpp" (@echo %i)))',

               #'<!@(for /r <(src_path) %i in ("./*.cpp","./*.cc","./*.h","./*.properties") do @if not "%i"=="AccessFileByMemoryMap.cpp" @echo <(src_path)/%i)',
               #'<!@(python "getsourc.py")',
               
              '../../siplib/c-ares/ares_create_query.c', 
              '../../siplib/c-ares/ares_platform.c', 
              '../../siplib/c-ares/ares__close_sockets.c', 
              '../../siplib/c-ares/ares__get_hostent.c', 
              '../../siplib/c-ares/ares__read_line.c', 
              '../../siplib/c-ares/ares__timeval.c', 
              '../../siplib/c-ares/ares_cancel.c', 
              '../../siplib/c-ares/ares_data.c', 
              '../../siplib/c-ares/ares_destroy.c', 
              '../../siplib/c-ares/ares_expand_name.c', 
              '../../siplib/c-ares/ares_expand_string.c', 
              '../../siplib/c-ares/ares_fds.c', 
              '../../siplib/c-ares/ares_free_hostent.c', 
              '../../siplib/c-ares/ares_free_string.c', 
              '../../siplib/c-ares/ares_gethostbyaddr.c', 
              '../../siplib/c-ares/ares_gethostbyname.c', 
              '../../siplib/c-ares/ares_getnameinfo.c', 
              '../../siplib/c-ares/ares_getopt.c', 
              '../../siplib/c-ares/ares_getsock.c', 
              '../../siplib/c-ares/ares_init.c', 
              '../../siplib/c-ares/ares_library_init.c', 
              '../../siplib/c-ares/ares_llist.c', 
              '../../siplib/c-ares/ares_mkquery.c', 
              '../../siplib/c-ares/ares_nowarn.c', 
              '../../siplib/c-ares/ares_options.c', 
              '../../siplib/c-ares/ares_parse_a_reply.c', 
              '../../siplib/c-ares/ares_parse_aaaa_reply.c', 
              '../../siplib/c-ares/ares_parse_mx_reply.c', 
              '../../siplib/c-ares/ares_parse_ns_reply.c', 
              '../../siplib/c-ares/ares_parse_ptr_reply.c', 
              '../../siplib/c-ares/ares_parse_srv_reply.c', 
              '../../siplib/c-ares/ares_parse_txt_reply.c', 
              '../../siplib/c-ares/ares_process.c', 
              '../../siplib/c-ares/ares_query.c', 
              '../../siplib/c-ares/ares_search.c', 
              '../../siplib/c-ares/ares_send.c', 
              '../../siplib/c-ares/ares_strcasecmp.c', 
              '../../siplib/c-ares/ares_strdup.c', 
              '../../siplib/c-ares/ares_strerror.c', 
              '../../siplib/c-ares/ares_timeout.c', 
              '../../siplib/c-ares/ares_version.c', 
              '../../siplib/c-ares/ares_writev.c', 
              '../../siplib/c-ares/bitncmp.c', 
              '../../siplib/c-ares/inet_net_pton.c', 
              '../../siplib/c-ares/inet_ntop.c', 
              '../../siplib/c-ares/windows_port.c', 
              '../../siplib/c-ares/ares.h', 
              '../../siplib/c-ares/ares_build.h', 
              '../../siplib/c-ares/ares_data.h', 
              '../../siplib/c-ares/ares_dns.h', 
              '../../siplib/c-ares/ares_getopt.h', 
              '../../siplib/c-ares/ares_ipv6.h', 
              '../../siplib/c-ares/ares_library_init.h', 
              '../../siplib/c-ares/ares_llist.h', 
              '../../siplib/c-ares/ares_nowarn.h', 
              '../../siplib/c-ares/ares_platform.h', 
              '../../siplib/c-ares/ares_private.h', 
              '../../siplib/c-ares/ares_rules.h', 
              '../../siplib/c-ares/ares_setup.h', 
              '../../siplib/c-ares/ares_strcasecmp.h', 
              '../../siplib/c-ares/ares_strdup.h', 
              '../../siplib/c-ares/ares_version.h', 
              '../../siplib/c-ares/ares_writev.h', 
              '../../siplib/c-ares/bitncmp.h', 
              '../../siplib/c-ares/config-dos.h', 
              '../../siplib/c-ares/config-win32.h', 
              '../../siplib/c-ares/inet_net_pton.h', 
              '../../siplib/c-ares/inet_ntop.h', 
              '../../siplib/c-ares/nameser.h', 
              '../../siplib/c-ares/setup_once.h', 

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
