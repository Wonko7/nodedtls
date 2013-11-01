{
  'targets': [
    {
      'target_name': 'node_dtls',
      'sources': [
        'src/node_dtls.cc'
      ],

      'defines': [
        'NODE_WANT_INTERNALS=1',
        'ARCH="<(target_arch)"',
        'PLATFORM="<(OS)"',
      ],
      
	# FIXME: remove hardcoded paths. Gyp can probably tell us how node was compiled and use that.
      'include_dirs': [
	      '/home/wjc/work/local/include',
	      '/home/wjc/work/local/include/openssl',
	      ],
 # 'conditions': [
 #        [ 'OS=="win"', {
 #          'conditions': [
 #            # "openssl_root" is the directory on Windows of the OpenSSL files
 #            ['target_arch=="x64"', {
 #              'variables': {
 #                'openssl_root%': 'C:/OpenSSL-Win64'
 #              },
 #            }, {
 #              'variables': {
 #                'openssl_root%': 'C:/OpenSSL-Win32'
 #              },
 #            }],
 #          ],
 #          'defines': [
 #            'uint=unsigned int',
 #          ],
 #          'libraries': [
 #            '-l<(openssl_root)/lib/libeay32.lib',
 #          ],
 #          'include_dirs': [
 #            '<(openssl_root)/include',
 #          ],
 #        }, { # OS!="win"
 #          
 #   'conditions': [
 #        ['node_shared_openssl=="true"', {
 #          # so when "node_shared_openssl" is "false", then OpenSSL has been
 #          # bundled into the node executable. So we need to include the same
 #          # header files that were used when building node.
 #          'include_dirs': [
 #            '/home/wjc/local/include',
 #            '/home/wjc/local/include/openssl',
 #          ],
 #          #"conditions" : [
 #          #  ["target_arch=='ia32'", {
 #          #    "include_dirs": [ "<(node_root_dir)/deps/openssl/config/piii" ]
 #          #  }],
 #          #  ["target_arch=='x64'", {
 #          #    "include_dirs": [ "<(node_root_dir)/deps/openssl/config/k8" ]
 #          #  }],
 #          #  ["target_arch=='arm'", {
 #          #    "include_dirs": [ "<(node_root_dir)/deps/openssl/config/arm" ]
 #          #  }]
 #          #]
 #        }]

 #        ],
 #        }],

 #      ]
    }
  ]
}
