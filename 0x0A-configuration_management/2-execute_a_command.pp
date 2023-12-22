# kills a process named killmenow
exec { 'kill_killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}
