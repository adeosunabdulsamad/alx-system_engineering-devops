# Turn off password authentication in SSH server configuration
file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/sshd_config',        # Path to the SSH server configuration file
  line   => 'PasswordAuthentication no',    # Line to add or modify in the file
  match  => '^#?PasswordAuthentication',    # Regular expression to match the line
}

# Declare the private key file for SSH client
file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',         # Path to the SSH client configuration file
  line   => 'IdentityFile ~/.ssh/school',   # Line to add or modify in the file
  match  => '^#?IdentityFile',              # Regular expression to match the line
}
