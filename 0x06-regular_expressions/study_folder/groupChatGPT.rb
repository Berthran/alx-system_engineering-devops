#!/usr/bin/env ruby
puts ARGV[0].scan(/^(.*)(?=\.pdf$)/).join
