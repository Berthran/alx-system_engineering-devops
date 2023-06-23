# Create a file and configure its properties such as the
# name, permissions, owner, group and contents

file { '/tmp/school':
  ensure  =>  present,
  mode    =>  '0744',
  owner   =>  'www-data',
  group   =>  'www-data',
  content =>  'I love Puppet',
}
