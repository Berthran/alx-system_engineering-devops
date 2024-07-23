## How SSH handles private keys

When attempting to connect to a remote server using ssh, a private key is required. The following cases could occur.

- Case 1: Private key is not added to ssh-agent
By default, the ssh-client searches for specific private keys in the `~/.ssh/` folder such as `id_rsa`, `id_edd5`, etc. If your private key is named `id_web_server` for example, it doesn't find it. Hence you are left with three options.
	1. Add the private key to the ssh-agent
	```sh
	ssh-add ~/.ssh/id_web_server
	```
	Now, when ssh runs, it will provide the server with the `id_web_server` private key.
	2. Provide the private key as an argument
	```sh
ssh -i ~/.ssh/id_web_server ubuntu@100.25.106.343
```
	3. Update the `/etc/ssh/ssh_config` file
Set the `IdentityFile` directive to the prefered private key. That way, the ssh client knows what key to use for authentication.
	```sh
	Host 100.25.106.343
		IdentityFile ~/.ssh/id_web_server
```

Any of these will work for a private key with and without a passphrase. Here's how each method behaves differently for a passphrased private key:
	1. Once added to the ssh-agent, no need to provide passphrase on connection to the remote server.
	2. Will require passphrase
	3. Will require passphrase



