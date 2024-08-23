# Error: Too many open files
# Check I: current limits
# Command: ulimit -n

# Define an exec resource to update Nginx configuration for handling more connections
exec { 'increase-ulimit-for-nginx':

  # The command to run: use 'sed' to search and replace '15' with '4096'
  # in the /etc/default/nginx file. This file likely contains configuration settings
  # related to file descriptor limits. The change increases the limit from 15 to 4096.

  command => 'sed -i "s/15/4096/" /etc/default/nginx',

  # Specify the directories to search for the 'sed' command.
  # This ensures that Puppet can find 'sed' to execute the command.
  path    => '/usr/local/bin/:/bin/'
}

# Define an exec resource named 'restart-nginx' to restart the Nginx service
exec { 'restart-nginx':

  # Command to execute:
  # Restart the Nginx service to apply the new configuration changes
  # The command 'nginx restart' is used here, but in some systems, 
  # 'nginx -s reload' or a service management command like 'systemctl restart nginx' 
  # might be more appropriate depending on the system's init system.
  command => 'nginx restart',

  # Specify the directory to search for the 'nginx' command.
  # This path is typically where init scripts are located, but you may need to
  # adjust this path based on your system's init system or service management tool.
  path    => '/etc/init.d/'
}
