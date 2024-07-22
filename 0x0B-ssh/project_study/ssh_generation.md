### To generate an RSA key pair on your local computer, type:
ssh-keygen

### Generate an SSH Key Pair with a Larger Number of Bits
ssh-keygen -b 4096

### Removing or Changing the Passphrase on a Private Key
ssh-keygen -p

### Displaying the SSH Key Fingerprint
ssh-keygen -l

### Copying your Public SSH Key to a Server with SSH-Copy-ID
ssh-copy-id username@remote_hosthttps://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys#basic-connection-instructions


## Basic Connection Instructions
ssh remote_host
ssh username@remote_host

### Running a Single Command on a Remote Server
ssh username@remote_host command_to_run

### Logging in to a Server with a Different Port
By default the SSH daemon on a server runs on port 22. Your SSH client will assume that this is the case when trying to connect. If your SSH server is listening on a non-standard port (this is demonstrated in a later section), you will have to specify the new port number when connecting with your client.

ssh -p port_num username@remote_host
