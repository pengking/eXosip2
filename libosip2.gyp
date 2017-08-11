# libspeex.gyp
# Author:pengchun
# Data:2017/7/3

{

  'targets':[
    {
       'target_name':'libosip2',
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
               '../../siplib/osip/src/osip2/fsm_misc.c',
               '../../siplib/osip/src/osip2/ict.c',
               '../../siplib/osip/src/osip2/ict_fsm.c',
               '../../siplib/osip/src/osip2/ist.c',
               '../../siplib/osip/src/osip2/ist_fsm.c',
               '../../siplib/osip/src/osip2/nict.c',
               '../../siplib/osip/src/osip2/nict_fsm.c',
               '../../siplib/osip/src/osip2/nist.c',
               '../../siplib/osip/src/osip2/nist_fsm.c',
               '../../siplib/osip/src/osip2/osip.c',
               '../../siplib/osip/src/osip2/osip_dialog.c',
               '../../siplib/osip/src/osip2/osip_event.c',
               '../../siplib/osip/src/osip2/osip_time.c',
               '../../siplib/osip/src/osip2/osip_transaction.c',
               '../../siplib/osip/src/osip2/port_condv.c',
               '../../siplib/osip/src/osip2/port_fifo.c',
               '../../siplib/osip/src/osip2/port_sema.c',
               '../../siplib/osip/src/osip2/port_thread.c',
               '../../siplib/osip/src/osip2/fsm.h',
               '../../siplib/osip/include/osip2/internal.h',
               '../../siplib/osip/include/osip2/osip.h',
               '../../siplib/osip/include/osip2/osip_condv.h',
               '../../siplib/osip/include/osip2/osip_dialog.h',
               '../../siplib/osip/include/osip2/osip_fifo.h',
               '../../siplib/osip/include/osip2/osip_mt.h',
               '../../siplib/osip/src/osip2/xixt.h',

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
