# This Puppet manifest increases the limit of open files
file { 'limits.conf':
  ensure  => file,
  path    => '/etc/security/limits.conf',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "* soft nofile 4096\n* hard nofile 65535\n",
}

file { 'sysctl.conf':
  ensure  => file,
  path    => '/etc/sysctl.conf',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "fs.file-max = 100000\n",
}

exec { 'reload sysctl':
  command     => 'sysctl -p',
  refreshonly => true,
  subscribe   => File['sysctl.conf'],
};
