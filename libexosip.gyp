# libspeex.gyp
# Author:pengchun
# Data:2017/7/3

{

  'targets':[
    {
       'target_name':'libexosip',
       'type':'static_library',
       
       # 添加依赖的gypi文件
        'includes':[
          '../buildall/common.gypi',
        ],

       
        'conditions':[
          ['OS=="win"',{

             'defines':[

                'TSC_OPENSSL',
                'TSC_WINDOWS',
                'CARES_STATICLIB',
                'HAVE_CARES_H',
                'SRV_RECORD',
                '_CRT_SECURE_NO_DEPRECATE',
                'ENABLE_TRACE',
                'WIN32',
                'EXOSIP_EXPORTS',
                '_WINDOWS',
                '_USRDLL',
                'NDEBUG',

              ],

            'variables':{

              'lib_path':'D:/Work/GitWorkwc/ThirdPart',
              'src_path':'../src',
              'include_path':'D:/Work/GitWorkwc/ThirdPart',
             },

             'include_dirs':[

               '../../siplib/osip/include',
               '../../siplib/exosip/include',
               '../../siplib/c-ares',

             ],

            'sources':[
               #'<!@(dir "<(src_path)" /b /"*.cpp/" | findstr /i/v "AccessFileByMemoryMap.cpp")',
               #'<!@(for %%i in (/'dir "<(src_path)" /b/' ) do echo %%i)',
               #'<!@(dir "<(src_path)/*.cpp" /b /a-d |findstr /v "AccessFileByMemoryMap.cpp")',
               #'<!@(for %i in ("../src/*.cpp") do @( if not "%i"=="AccessFileByMemoryMap.cpp" (@echo %i)))',

               #'<!@(for /r <(src_path) %i in ("./*.cpp","./*.cc","./*.h","./*.properties") do @if not "%i"=="AccessFileByMemoryMap.cpp" @echo <(src_path)/%i)',
               #'<!@(python "getsourc.py")',

              '../../siplib/exosip/src/eXcall_api.c',
              '../../siplib/exosip/src/eXconf.c',
              '../../siplib/exosip/src/eXinsubscription_api.c',
              '../../siplib/exosip/src/eXmessage_api.c',
              '../../siplib/exosip/src/eXoptions_api.c',
              '../../siplib/exosip/src/eXosip.c',
              '../../siplib/exosip/src/eXpublish_api.c',
              '../../siplib/exosip/src/eXregister_api.c',
              '../../siplib/exosip/src/eXsubscription_api.c',
              '../../siplib/exosip/src/eXtl_dtls.c',
              '../../siplib/exosip/src/eXtl_tcp.c',
              '../../siplib/exosip/src/eXtl_tls.c',
              '../../siplib/exosip/src/eXtl_udp.c',
              '../../siplib/exosip/src/eXtransport.c',
              '../../siplib/exosip/src/eXutils.c',
              '../../siplib/exosip/src/inet_ntop.c',
              '../../siplib/exosip/src/jauth.c',
              '../../siplib/exosip/src/jcall.c',
              '../../siplib/exosip/src/jcallback.c',
              '../../siplib/exosip/src/jdialog.c',
              '../../siplib/exosip/src/jevents.c',
              '../../siplib/exosip/src/jnotify.c',
              '../../siplib/exosip/src/jpipe.c',
              '../../siplib/exosip/src/jpublish.c',
              '../../siplib/exosip/src/jreg.c',
              '../../siplib/exosip/src/jrequest.c',
              '../../siplib/exosip/src/jresponse.c',
              '../../siplib/exosip/src/jsubscribe.c',
              '../../siplib/exosip/src/milenage.c',
              '../../siplib/exosip/src/misc.c',
              '../../siplib/exosip/src/rijndael.c',
              '../../siplib/exosip/src/sdp_offans.c',
              '../../siplib/exosip/src/udp.c',
              '../../siplib/exosip/include/eXosip2/eX_call.h',
              '../../siplib/exosip/include/eXosip2/eX_message.h',
              '../../siplib/exosip/include/eXosip2/eX_options.h',
              '../../siplib/exosip/include/eXosip2/eX_publish.h',
              '../../siplib/exosip/include/eXosip2/eX_register.h',
              '../../siplib/exosip/include/eXosip2/eX_setup.h',
              '../../siplib/exosip/include/eXosip2/eX_subscribe.h',
              '../../siplib/exosip/include/eXosip2/eXosip.h',
              '../../siplib/exosip/src/eXosip2.h',
              '../../siplib/exosip/src/eXtransport.h',
              '../../siplib/exosip/src/inet_ntop.h',
              '../../siplib/exosip/src/jpipe.h',
              '../../siplib/exosip/src/milenage.h',
              '../../siplib/exosip/src/rijndael.h',

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
