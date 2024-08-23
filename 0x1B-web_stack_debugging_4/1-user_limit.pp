# Increase the limit of files to open for holberton user

#file_line { 'increase-soft-file-limit-for-holberton-user':
#  path  => '/etc/security/limits.conf',
#  line  => 'holberton soft 50000',
#  match => '^holberton soft 4',
#}

# Increase the soft file limit for the Holberton user to 50,000
exec { 'set-holberton-soft-file-limit':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}


#file_line { 'increase-hard-file-limit-for-holberton-user':
#  path  => '/etc/security/limits.conf',
#  line  => 'holberton hard 50000',
#  match => '^holberton hard 5',
#}

# Increase the hard file limit for the Holberton user to 50,000
exec { 'set-holberton-hard-file-limit':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
