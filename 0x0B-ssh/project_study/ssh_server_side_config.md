### Disabling Password Authentication
To do this, connect to your remote server and open the /etc/ssh/sshd_config file with root or sudo privileges:

```sh
sudo nano /etc/ssh/sshd_config
```

Inside of the file, search for the PasswordAuthentication directive. If it is commented out, uncomment it. Set it to no to disable password logins:

```
/etc/ssh/sshd_config
PasswordAuthentication no
```

restart the SSH service.
```sh
sudo service ssh restart
```
