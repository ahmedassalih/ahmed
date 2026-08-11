source "https://rubygems.org"

# Static site generator. Run everything through `bundle exec`.
gem "jekyll", "~> 4.4.1"

# Plugins — every gem listed here is declared in _config.yml and actually used.
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.17"          # /feed.xml
  gem "jekyll-seo-tag", "~> 2.8"        # <title>, canonical, Open Graph, JSON-LD
  gem "jekyll-sitemap", "~> 1.4"        # /sitemap.xml
  gem "jekyll-redirect-from", "~> 0.16" # legacy URL preservation
end

# Windows and JRuby do not ship zoneinfo files.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Directory-watch performance booster on Windows.
gem "wdm", "~> 0.1", :platforms => [:mingw, :x64_mingw, :mswin]

gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
