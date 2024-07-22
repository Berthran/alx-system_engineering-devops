### Copying your Public SSH Key to a Server with SSH-Copy-ID
ssh-copy-id username@remote_host
ssh-copy -i ~/.ssh/school.pub username@remote_host
To forcefully add a public key to the server use:
ssh-copy -f -i ~/.ssh/school.pub username@remote_host

### Copying your Public SSH Key to a Server Without SSH-Copy-ID
You can output the contents of the key and pipe it into the ssh command. On the remote side, you can ensure that the ~/.ssh directory exists, and then append the piped contents into the ~/.ssh/authorized_keys file:
```sh
cat ~/.ssh/id_rsa.pub | ssh username@remote_host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### Copying your Public SSH Key to a Server Manually
```sh
cat ~/.ssh/id_rsa.pub

mkdir -p ~/.ssh

echo public_key_string >> ~/.ssh/authorized_keys
```


