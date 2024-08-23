# Increase the limit of files to open for holberton user

file_line { 'increase-soft-file-limit-for-holberton-user':
  path  => '/etc/security/limits.conf',
  line  => 'holberton soft nofile 50000',
  match => '^holberton soft',
}

file_line { 'increase-hard-file-limit-for-holberton-user':
  path  => '/etc/security/limits.conf',
  line  => 'holberton hard nofile 50000',
  match => '^holberton hard',
}
