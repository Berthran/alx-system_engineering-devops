# Terminates a running process

exec { 'kill_killmenow':
  command => 'pkill killmenow',
  path    => '/usr/local/bin:/usr/bin:/bin',
}
