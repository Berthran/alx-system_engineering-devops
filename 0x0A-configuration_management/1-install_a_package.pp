# Install a specific version of a package - flask
# using a particular package manager - pip3

package { 'flask':
  ensure   =>  '2.1.0',
  provider =>  'pip3',
}
