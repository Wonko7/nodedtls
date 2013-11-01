# Node Dtls
Supported OS: Linux.
Author: Sayyad Gaffar.
Node Version: >= 0.6.0

## Building:
Node needs to be built against a shared openssl library, nodedtls will use the same.

### Environment:
- `prefix=...`
- `PATH=$prefix/bin:$prefix/sbin:$prefix/lib/node_modules/npm/bin/node-gyp-bin:$PATH`
- `export LD_LIBRARY_PATH=$prefix/lib`

### Building:
- OpenSSL:	`./config shared --prefix=$prefix enable-tlsext enable-dtls enable-ssl; make; make install`
- Node:		`./configure --prefix=$prefix --shared-openssl --shared-openssl-includes $prefix/include --shared-openssl-libpath $prefix/lib; make; make install`
- nodedtls:	Modify `binding.gyp` to use the correct openssl include files then `node-gyp configure build`

### Warnings:
Today this has only been tested with the following program versions, and only on linux:
- Node:		v0.10.12-release:a088cf4f930d3928c97d239adf950ab43e7794aa
- OpenSSl:	1.0.1e

## Testing the dtls on node
- In the node_modules folder, find dtls.
- Inside Demo, one will find the dtlsserver and dtlsclient.
- Run the dtls Server: dtls/demo/dtlsServer/dtlsController.js  
- Connect using the dtls client: dtls/demo/dtlsClient.js
- The certificate and key are generated using openssl to test the dtls client and server.

## To run the Client Install the below modules.
- bindings.
- microtime.
- log4js.
- nodeload.
