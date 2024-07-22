## Defining Server-Specific connection information
On your local computer, you can define individual configurations for some or all of the servers you connect to. These can be stored in the ~/.ssh/config file, which is read by your SSH client each time it is called.

#### INDIVIDUAL CONFIGURATIONS USING `HOST` KEYWORD
Inside, you can define individual configuration options by introducing each with a Host keyword, followed by an alias. Beneath this and indented, you can define any of the directives found in the ssh_config man page:

An example configuration would be:

```sh
~/.ssh/config
Host testhost
    HostName your_domain
    Port 4444
    User demo
```
You could then connect to your_domain on port 4444 using the username demo by simply typing:

```sh
ssh testhost
```


#### MULTIPLE HOST CONFIGURATIONS USING WILDCARD *`*
```sh
~/.ssh/config
Host *
    ForwardX11 no

Host testhost
    HostName your_domain
    ForwardX11 yes
    Port 4444
    User demo
``` 


#### KEEPING CONNECTIONS ALIVE TO AVOID TIMEOUT 
This can be done by setting the `ServerAliveInterval` directive. E.g. Setting the ServerAliveInterval to “120” will send a packet to the server every two minutes. This should be enough to notify the server not to close the connection:

```sh
~/.ssh/config
Host *
    ServerAliveInterval 120
```

#### Disabling Host Checking (Not advisable)
Set the `StrictHostKeyChecking` directive to `no` to add new hosts automatically to the known_hosts file. 
Set the `UserKnownHostsFile` to `/dev/null` to not warn on new or changed hosts:

```sh
~/.ssh/config
Host *
    StrictHostKeyChecking no
    UserKnownHostsFile /dev/null
```

You can enable the checking on a case-by-case basis by reversing those options for other hosts. The default for `StrictHostKeyChecking` is `ask`:

```
~/.ssh/config
Host *
    StrictHostKeyChecking no
    UserKnownHostsFile /dev/null

Host testhost
    HostName your_domain
    StrictHostKeyChecking ask
    UserKnownHostsFile /home/demo/.ssh/known_hosts
```

#### Multiplexing SSH Over a Single TCP Connection
SSH multiplexing re-uses the same TCP connection for multiple SSH sessions. This removes some of the work necessary to establish a new session, possibly speeding things up. Limiting the number of connections may also be helpful for other reasons.
How to configure your client to automatically use multiplexing when available.
- Set the `ControlMaster` value to `auto` to automatically allow multiplexing
- Set the `ControlPath` value. This will establish the path to control socket. The first session will create this socket and subsequent sessions will be able to find it because it is labeled by username, host, and port.
- Set the `ControlPersist` option to 1 to allow the initial master connection to be backgrounded. The 1 specifies that the TCP connection should automatically terminate one second after the last SSH session is closed:

```sh
Host *
    ControlMaster auto
    ControlPath ~/.ssh/multiplex/%r@%h:%p
    ControlPersist 1
```
Now, we need to actually create the directory we specified in the control path:

```sh
mkdir ~/.ssh/multiplex
```

Now, any sessions that are established with the same machine will attempt to use the existing socket and TCP connection. When the last session exists, the connection will be torn down after one second.

If for some reason you need to bypass the multiplexing configuration temporarily, you can do so by passing the -S flag with none:

```sh
ssh -S none username@remote_host
```
