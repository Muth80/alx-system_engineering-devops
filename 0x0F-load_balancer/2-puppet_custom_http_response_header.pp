# 2-puppet_custom_http_response_header.pp

# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Configure Nginx with custom HTTP response header
file { '/etc/nginx/conf.d/custom_response_header.conf':
  ensure  => present,
  content => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Restart Nginx to apply the changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/conf.d/custom_response_header.conf'],
}
