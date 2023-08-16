# This manifest will configure nginx to handle more load
class { 'nginx':
  manage_repo     => true,
  package_ensure  => latest,
}

# Configure nginx
nginx::resource::server { 'localhost':
  listen_port => 80,
  use_default_location => false,
  locations => {
    '/' => {
      proxy => 'http://localhost',
    }
  }
}

nginx::resource::location { '/':
  location      => '/',
  server        => 'localhost',
  proxy         => 'http://localhost',
}

nginx::resource::upstream { 'localhost':
  members => ['localhost'],
}

exec { 'reload-nginx':
  command     => 'systemctl reload nginx',
  refreshonly => true,
  subscribe   => [ Nginx::Resource::Server['localhost'], Nginx::Resource::Location['/'], Nginx::Resource::Upstream['localhost'] ],
};
